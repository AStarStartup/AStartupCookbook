# [Astartup Cookbook](../)

## [Documentation](./)

### Cookbooks

Creating a cookbook can increase your project's chance of success by creating the Honey pot to attract users to your products by providing the user with free documentation, and the documentation will also have the affect of increasing the quality of your product with Don't Repeat Yourself (DRY) documentation. This chapter will cover the creation of a Cookbook using the Markdown Cookbook.

#### Markdown Cookbook Template

The Markdown Cookbook is a template used to create this Cookbook.

**1.**  Clone the Markdown Cookbook recursively.

```Bash
git clone --recursive <https://github.com/AStarStartup/AstartupCookbook>
```

**2.** Rename all files with `markdown.cookbook` to your cookbook's name.

For windows users use the PowerShell command:

```PowerShell
Dir -recurse | Rename-Item -NewName { $_.Name -replace "markdown.cookbook","your_project.cookbook" }
```
Mac users will use the command:

```PowerShell
```

**3.** Download and install [StarUML](staruml.io), open the `your_project.cookbook.mdj` file, and rename the root to `your_company_name`, and replace all of the copyright information in the Markdown documentation with to copyright holder's name.

**4.** Download and install [Visual Studio Code](https://code.visualstudio.com).

**5.** Open Visual Studio, right click on the workspace and click on `Add Folder to Workspace`, navigate to the clone of this repo and click `Add`.

**6.** Find and replace "Markdown Cookbook" in all files with the name of your Cookbook and `Your Name` with the name of the copyright holder. The license in this book is designed to allow you to sell the Cookbook to fund your project. If you want to change the license just find and replace the entire license line with the desired license.

## License

Copyright 2014-20 (C) [Cale McCollough](https://cookingwithcale.org).

This is an open-source document, the Document, that was written by and contains intellectual property. The Document consists of documents, files, source code, technology design files, art, and other content contained this file, folder and the GitHub repository located at <https://github.com/AStarStartup/AstartupCookbook>, the Repository. The Document is published under a generic non-commercial open-source license, the License, and is for educational and demonstration purposes only. You may use, reproduce, publicly display, and modify the Document so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repository as an Issue ticket to become part of the Document. You may not sell the Document or otherwise profit from derivative works created from the Document without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Document distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
