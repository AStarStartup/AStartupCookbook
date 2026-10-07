---
layout: page
title: "Problem Solving"
---

# [Astartup Cookbook](../)

## [Engineering](./)

### Problem Solving

Use problem–solution analysis to decide whether to investigate, change a process, buy, build, or stop. The output is a decision with evidence and limits, not a polished description of an idea.

The author's original prompts remain useful: identify the rules, identify the winning condition, and identify the next step. Apply them in that order so the next step is worth taking.

#### 1. Identify the rules and the decision

State the decision owner, deadline, available cash and founder hours, permissions, and constraints. Include operational ownership: who handles a failure or a support ticket on Monday morning? Record regulatory, safety, data, and contractual questions for the appropriate specialist; route legal conclusions to `attorney`.

Define what is outside scope. A problem-analysis mission is not permission to buy software, contact customers, collect sensitive data, or start implementing the most exciting option.

#### 2. Describe the problem without smuggling in a solution

Use this form:

```text
[Specific person / organization] trying to [job] in [situation]
experiences [observable obstacle], which causes [consequence].
They currently [workaround], at [measured or explicitly assumed cost].
Evidence: [records and dates]. Unknowns: [gaps].
```

"Small agencies need an AI invoice app" describes a proposed product. "An agency's owner spends time chasing overdue invoices and cannot plan upcoming payments" describes a possible problem. Neither is established until supported by evidence from the intended context.

Separate the symptom from the proposed cause. Late payment might reflect missing reminders, disputed invoices, procurement rules, or a customer's inability to pay. A reminder app addresses only some of those causes. Ask what observation would distinguish them.

Name the user, buyer, payer, and any approver separately. The person with the problem may not control a budget or have permission to install your product.

#### 3. Build an evidence record

Use [Customer Interviews](../Analytics/CustomerInterviews.md) to investigate a recent real event, the current workaround, frequency, consequences, and buying process. Where permitted, compare the account with records, observation, or a small workflow test.

For each item, record an ID, source location, date, collector, relevant excerpt or measurement, method, and limits. Distinguish:

* Observation: what was actually seen or measured, including the units and denominator.
* Self-report: what a participant said happened; preserve their words separately from your interpretation.
* Inference: your explanation of an observation, with alternatives.
* Assumption or hypothesis: an untested input or proposed relationship.
* Hypothetical example: invented solely to teach or explore a scenario, never entered as customer evidence.

An agent-generated persona, competitor description, or simulated interview is not independent evidence. Repeated summaries of the same interview are still one source. Record negative findings, refusals, and cases where the problem does not occur.

Avoid a universal interview count. Define eligibility and recruitment channels, record the sample and nonresponses, and judge whether it covers the decision's uncertainty. A convenience sample can reveal mechanisms and useful questions; it does not establish market prevalence or justify population percentages.

Keep private identities and raw records in an approved store. Use anonymized IDs in shared Markdown, and link rather than copy sensitive material into every task packet.

#### 4. Identify the winning condition

Define the outcome independently of the product. Establish a baseline, measure, unit, population, time horizon, and acceptance threshold. For example, measure staff minutes per invoice and error rate over a specified billing cycle, not whether a prototype has a reminder button.

Agree on a guardrail: errors, cash exposure, support burden, privacy, safety, or customer response commitments that must not get worse. Record how the baseline was obtained. If it is unavailable, the next task may be measuring it, not building.

Do not treat stated enthusiasm as willingness to pay. A paid trial or repeated use is stronger behavioral evidence for that limited offer, but still does not prove a large market, retention, or scalable economics.

#### 5. Compare alternatives, including not building

At minimum compare the current workaround/do nothing, a manual or process change, an existing product or partner, and a new build when relevant. Define the same outcome for every option.

| Dimension | What to record |
|---|---|
| Evidence | Which problem or feasibility claim this option addresses, and what remains untested |
| Cash | One-time and recurring cash costs, collection timing, commitments, and downside exposure |
| Founder capacity | Setup, review, sales, delivery, support, and coordination hours; opportunity cost |
| Adoption | User effort, migration, buyer approval, incentives, and switching costs |
| Operations | Named operator, exceptions, failure recovery, vendor dependency, and maintainability |
| Reversibility | How cheaply you can stop, undo, or change direction |

Use scores only when their scales and weights are explicit. A weighted average must not override a hard safety or cash constraint. A complex operating model is a cost even if its API bill is small.

#### 6. Model viability with units and scenarios

Separate customer benefit from your ability to capture it. Time saved may free capacity without reducing payroll. Faster cash collection is not additional revenue. Bookings, recognized revenue, profit, and money in the bank are different measures.

Record formulas and input provenance. Use downside, base, and upside assumptions; do not call them measured forecasts. Include founder labor, review time, acquisition, retention, support, fixed obligations, and working-capital timing where material. Distinguish variable costs from fixed costs, and contribution from gross margin.

Identify the assumption that can reverse the recommendation. Calculate a break-even or capacity threshold where useful. If the result depends on ignoring support or assuming instant sales, change the plan before asking an agent to build it.

#### 7. Test the most consequential uncertainty

Choose a bounded experiment that can change the decision. State it before observing results:

```text
Question ID / hypothesis ID:
Claim and plausible alternative explanations:
Eligible participants and recruitment method:
Observed behavior or measurement:
Baseline / comparator:
Pass, fail, and inconclusive rules:
Time, cash, and founder-hour caps:
Permissions, data handling, and safety guardrails:
Owner and observation window:
Action for each possible outcome:
```

Use the method's `QnHm` references when the project uses them. Test problem frequency, payment, usability, technical feasibility, and operational cost separately; one successful demo cannot settle all of them.

A technical test can fail because of an implementation error without disproving demand. An interview can support a problem without supporting your preferred solution. Check the mechanism and confounders before interpreting a result. Missing data is inconclusive, not a pass.

#### 8. Choose the next step and an accountable handoff

Choose proceed to another bounded test, revise the hypothesis, defer, buy/use the workaround, or stop. State what evidence would change the decision and when it will be reviewed.

Only then create an implementation mission. Link its Problem and Solution to the decision record, list the affected files, and define executable acceptance checks. See [Mission Tickets](../Dev/IDD/MissionTickets.md) and [Agent Operations](../Dev/AgentOperations.md). Do not let an issue title turn a hypothesis into a confirmed requirement.

#### Copyable decision record

Use the following headings in a project record. Replace the prompts with evidence or explicit unknowns; this fenced worksheet is a template, not a completed analysis.

```markdown
# Decision: <investigate / change / buy / build / stop>

## Owner, deadline, and constraints
<Cash, hours, permissions, excluded scope, operational owner.>

## Problem and current workaround
<User, buyer, payer, job, situation, obstacle, consequence.>

## Evidence
| ID | Type | Source and date | Observation / excerpt | Limits |
|---|---|---|---|---|

## Baseline and winning condition
<Measure, units, denominator, period, target, and guardrails.>

## Competing explanations and alternatives
<Include do nothing, manual/process, buy/partner, and build.>

## Economics and capacity
<Input provenance, formulas, downside/base/upside, cash vs opportunity cost.>

## Next experiment and stop rule
<QnHm, eligible sample, pass/fail/inconclusive, owner, budget, window.>

## Recommendation and sensitivity
<Reason, weakest assumption, what would reverse it, and next review.>

## Implementation handoff
<Approved scope, issue links, files, checks, and permissions still needed.>
```

#### Worked example: invoice follow-up service

This entire example is hypothetical. No interviews, paid pilots, savings, or sales reported here occurred. The numbers are teaching assumptions, not benchmarks or the author's founder-interview results.

Decision: do not build an automated product yet. If the founder authorizes it, test a manual workflow with intended buyers and measure the cause of delays, payment, and support effort. The operating model has little margin for founder time in the base case.

Problem hypothesis: small design agencies spend avoidable staff time following up invoices. Competing explanation: customers pay late because of disputes or cash constraints, so reminders may not help. Alternatives are the current process, a manual follow-up service, an existing invoicing tool, and a new automated product.

Illustrative customer benefit: assume 60 invoices per month, 8 minutes of current follow-up per invoice, 2 minutes after the change, and staff time valued at USD 35/hour.

```text
Freed capacity = 60 invoices/month × (8 − 2) minutes/invoice ÷ 60 minutes/hour
               = 6 hours/month
Illustrative capacity value = 6 hours/month × USD 35/hour = USD 210/month
```

That is capacity value, not measured cash savings or proof the buyer will pay. Check reminder errors and relationship damage as well as staff time.

For the proposed service, assume USD 300/month fixed cash expense, 8 fixed founder hours/month, and founder time valued at USD 40/hour. Assume subscription receipts and variable cash payments occur within the same month, solely to simplify this operating model. Upfront setup is USD 500 cash plus 40 founder hours, or USD 2,100 including opportunity cost. Acquisition, onboarding, churn, taxes, financing, and collection delays are excluded and must be added before a launch decision.

```text
Cash contribution/customer/month = price − variable cash cost
Economic contribution/customer/month = cash contribution − support hours × USD 40/hour
Monthly operating cash balance = customers × cash contribution − USD 300
Monthly balance including opportunity cost = customers × economic contribution − USD 620
Founder operating hours/month = customers × support hours + 8 hours
```

USD 620 includes USD 300 fixed cash plus USD 320 fixed founder opportunity cost. The cash balance is not accounting profit or gross margin; the economic balance is not additional cash spent. Neither includes the upfront investment.

| Assumption / result | Downside | Base | Upside |
|---|---:|---:|---:|
| Active paying customers | 5 | 12 | 25 |
| Price, USD/customer/month | 60 | 80 | 95 |
| Variable cash cost, USD/customer/month | 18 | 12 | 10 |
| Support, hours/customer/month | 1.00 | 0.50 | 0.25 |
| Cash contribution, USD/customer/month | 42 | 68 | 85 |
| Economic contribution, USD/customer/month | 2 | 48 | 75 |
| Monthly operating cash balance, USD | -90 | 516 | 1,825 |
| Monthly balance including opportunity cost, USD | -610 | -44 | 1,255 |
| Founder operating hours/month | 13.00 | 14.00 | 14.25 |

The base case produces USD 516/month before excluded items but loses USD 44/month after valuing the stated founder hours. It is not automatically an attractive business because cash is positive.

At base assumptions, recurring cash break-even is `ceil(300 / 68) = 5` customers. Including fixed and variable founder time, break-even is `ceil(620 / 48) = 13` customers. These thresholds exclude acquisition and setup. At 12 customers, support must be below 24.5 minutes/customer/month for a positive recurring balance including opportunity cost, with the other base inputs unchanged. The assumed 30 minutes exceeds that threshold.

A prospective test could recruit five eligible agencies, offer a clearly defined USD 80/month manual trial, and observe two billing cycles within an eight-week cap. The founder must approve outreach, payment terms, data access, refunds, and a budget of no more than USD 200 extra cash and 20 founder hours before it starts. This manual test uses existing approved tools, not the modeled production setup; the USD 500 setup and USD 300/month production expense are not authorized by these caps. If the manual scope cannot fit the caps, revise it before starting. These caps and counts are illustrative choices, not a statistical proof or universal startup rule.

Predeclare a gate for a larger pilot: at least three eligible agencies actually pay, at least two choose to continue into the second cycle, relevant follow-up time falls against their measured baselines, support averages no more than 20 minutes/customer/month, and no material reminder error or data incident occurs. Track per-agency results, refusals, missing observations, and total founder hours; do not average away an unsafe case. Hitting a resource cap stops the experiment. The cash cap excludes customer receipts and applies to additional outlays; the hours cap includes recruitment and observation, not just delivery.

Fail or inconclusive results lead to a cause investigation, process change, different offer, or stopping. Passing this small gate supports only a larger bounded pilot, not market-size estimates or a production launch. Review excluded acquisition costs and actual collection timing before committing to automation.

#### Agent and local-model use

Give the model the decision, this procedure, the approved constraints, and sanitized source records. Ask for an evidence ledger, missing inputs, competing explanations, options, a calculation plan, and a proposed experiment. Require source IDs for factual assertions and explicit labels on assumptions.

Do the arithmetic in a calculator or code, then compare the generated recommendation with the actual evidence. Check citations and preserve disconfirming records. If primary inputs are missing, the correct output is a research task or an inconclusive decision, not invented findings.

Use [Local LLM Tasks](../Dev/LocalLLM.md) for read-only drafting. The model can explain the result in the human's language and skill level without translating identifiers, changing units, or weakening warnings and approval gates.
