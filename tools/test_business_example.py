# Copyright AStarship <https://astarship.net>.
"""Recalculate the hypothetical example from the published Markdown inputs."""

from decimal import Decimal, ROUND_CEILING
from fractions import Fraction
from pathlib import Path
import re
import unittest


GuidePath = Path(__file__).resolve().parents[1] / "Engineering" / "ProblemSolving.md"


def TExampleNumber(pattern, text):
  match = re.search(pattern, text)
  if match is None:
    raise AssertionError(f"Missing worked-example input: {pattern}")
  return Decimal(match.group(1).replace(",", ""))


def TExampleRead():
  text = GuidePath.read_text(encoding="utf-8")
  start = text.index("| Assumption / result |")
  table = {}
  for line in text[start:].splitlines()[2:]:
    if not line.startswith("|"):
      break
    cells = [cell.strip() for cell in line.strip("|").split("|")]
    table[cells[0]] = [Decimal(value.replace(",", "")) for value in cells[1:]]
  cash_fixed = TExampleNumber(r"assume USD ([\d,]+)/month fixed cash expense", text)
  hours_fixed = TExampleNumber(r"(\d+) fixed founder hours/month", text)
  hourly = TExampleNumber(r"founder time valued at USD ([\d,]+)/hour", text)
  return text, table, cash_fixed, hours_fixed, hourly


class TBusinessExampleTests(unittest.TestCase):
  def test_scenario_table_matches_input_formulas(self):
    text, table, cash_fixed, hours_fixed, hourly = TExampleRead()
    self.assertIn("This entire example is hypothetical.", text)
    for index, scenario in enumerate(("Downside", "Base", "Upside")):
      with self.subTest(scenario=scenario):
        customers = table["Active paying customers"][index]
        price = table["Price, USD/customer/month"][index]
        variable = table["Variable cash cost, USD/customer/month"][index]
        support = table["Support, hours/customer/month"][index]
        cash_contribution = price - variable
        economic_contribution = cash_contribution - support * hourly
        self.assertEqual(table["Cash contribution, USD/customer/month"][index], cash_contribution)
        self.assertEqual(table["Economic contribution, USD/customer/month"][index], economic_contribution)
        self.assertEqual(table["Monthly operating cash balance, USD"][index], customers * cash_contribution - cash_fixed)
        self.assertEqual(table["Monthly balance including opportunity cost, USD"][index], customers * economic_contribution - cash_fixed - hours_fixed * hourly)
        self.assertEqual(table["Founder operating hours/month"][index], customers * support + hours_fixed)

  def test_break_even_and_support_threshold_match_base_inputs(self):
    text, table, cash_fixed, hours_fixed, hourly = TExampleRead()
    cash_contribution = table["Cash contribution, USD/customer/month"][1]
    economic_contribution = table["Economic contribution, USD/customer/month"][1]
    economic_fixed = cash_fixed + hours_fixed * hourly
    cash_break_even = (cash_fixed / cash_contribution).to_integral_value(rounding=ROUND_CEILING)
    economic_break_even = (economic_fixed / economic_contribution).to_integral_value(rounding=ROUND_CEILING)
    self.assertIn(f"ceil({cash_fixed} / {cash_contribution}) = {cash_break_even}", text)
    self.assertIn(f"ceil({economic_fixed} / {economic_contribution}) = {economic_break_even}", text)
    customers = table["Active paying customers"][1]
    threshold = (Fraction(cash_contribution) - Fraction(economic_fixed) / Fraction(customers)) / Fraction(hourly) * 60
    stated = Fraction(TExampleNumber(r"support must be below ([\d.]+) minutes/customer/month", text))
    self.assertEqual(stated, threshold)


if __name__ == "__main__":
  unittest.main()
