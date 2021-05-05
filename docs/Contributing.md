## Contributing Guide

### Submitting Bugs

**1.** Ensure the bug was not already reported by by reading the [Issues](https://github.com/abc_org/xyz_project/issues).

**2.** Open `/docs/bug_report_template.md` and copy it's contents to the clipboard.

**3.** Create an issue, paste the template into the Issue body and fill it out.

## Feature Requests

**1.** Same as the instructions for submitting a bug report except with using `/docs/feature_request.md`.

### Completing Issues

**1.** Clone the repo and create a branch for the IssueNumber:

```Console
git clone https://github.com/CookingWithCale/AStartupCookbook.git
cd AStartupCookbook
git checkout -b Issue123
```

**2.** Complete the issue with passing unit tests and submit the completed issue:

```Console
git add --all
git commit -m "ModuleID.Add feature XYZ. #123"
git push origin Issue123
```

**3.** Create a Pull Requesting using the `/docs/PULL_REQUEST_TEMPLATE.md`

**4.** Get others to inspect your changes and merge the branch to the master.

**5.** Merge the branch, complete another ticket, and delete the old branch.

```Console
git branch -m Issue123 Issue125
git add --all
git commit "ModuleID.Fix feature ABC. #125"
```

**6.** Create a GitHub Pull Request to merge the new branch with the master at <https://github.com/CookingWithCale/AStartupCookbook/pulls>.

## License

Copyright 2021 © [Cale McCollough](https://cookingwithcale.org); most rights reserved, Third-party commercialization prohibited, mandatory improvement donations, licensed under the Kabuki Strong Source-available License that YOU MUST CONSENT TO at <https://github.com/CookingWithCale/AStartupCookbook>.
