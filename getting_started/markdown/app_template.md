# [Astartup Cookbook](../../readme.md)

## [Documentation](../readme.md)

### [Markdown Templates](./readme.md)

#### App Template

The Markdown Software Engineering repository contains the [GitHub templates](./github_templates.md) for:

* [Requirements Analysis Document (RAD)](https://github.com/kabuki-starship/markdown.software_engineering/tree/master/rdd)
* [Software Design Document (SDD)](https://github.com/kabuki-starship/markdown.software_engineering/tree/master/sdd)

**1.**  Clone the repository:

```Bash
git clone https://github.com/kabuki-starship/markdown.software_engineering.git
```

**2.** Rename all files with `markdown.software_engineering` to your cookbook's name.

For windows users use the PowerShell command:

```PowerShell
Dir -recurse | Rename-Item -NewName { $_.Name -replace "markdown.software_engineering","your_project.cookbook" }
```
Mac users will use the command:

```PowerShell
```

**3.** Open the `your_company_name.mdj` file with StarUML, and rename the root node to `your_company_name`, and replace all of the copyright information in the Markdown documentation with to copyright holder's name.

**4.** Find and replace "Markdown Software Engineering" in all files with the name of your Cookbook and `Your Name` with the name of the copyright holder. The license in this book is designed to allow you to sell the Cookbook to fund your project. If you want to change the license just find and replace the entire license line with the desired license.

## License

Copyright 2014-9 (C) [Cale McCollough](https://calemccollough.github.io); all rights reserved (R).

This is an open-source document, the Document, that was written by and contains intellectual property. The Document consists of documents, files, source code, technology design files, art, and other content contained this file, folder and the GitHub repository located at <https://github.com/kabuki-starship/astartup.cookbook>, the Repository. The Document is covered under the Kabuki Strong Source-available License, the License, and is for educational and demonstration purposes only. You may use, reproduce, publicly display, and modify the Document so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repository as an Issue ticket to become part of the Document. You may not sell the Document or otherwise profit from derivative works created from the Document without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Document distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
