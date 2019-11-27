# [Astartup Cookbook](./readme.md)

## [Development](./readme.md)

### Revision Control Systems

The goal of this case study is to highlight an entrepreneur who does not program computers who has failed without using revision control, and who now could not live without it. The study should highlight how you should only do work in digestible chunks where you have a clear planned goal, and then synchronize their settings to

This chapter talks about revision control systems and how they are used on projects. The aim of this chapter is to get people who do not use revision control systems on their projects.

#### Git

Git is a RCS programmed in C that is the gold standard for RCS. Git is very easy to use when working by yourself. You can get away with only knowing a handful of commands. Reverting changes does take a little bit of a learning curve but if you use a web-based Git tool like GitHub you may use the website to look at past changes and copy and paste or download the original raw data. Git is the primary revision control system that shall be used throughout this book.

```
git init
git add --all
git commit -m "First commit."
git push
```

This works great when you're working by yourself as long as you keep your code working and documented, but it will not fly when working with others. When working with others you will need to use an Issue Tracking System and make a Pull Request for an Issue which you then merge back into the Master branch; we'll cover this more below.

#### Mercurial

Mercurial is programmed in Python and is similar to Git in functionality but provides a higher level command line interface. Mercurial distinguishes itself from git in how it manages revision history. Mercurial only allows users to roll back changes and not to modify the history. This may be more useful for more useful for documentation purposes.

## License

Copyright 2014-9 © the [Kabuki Starship™](https://kabukistarship.com).

This source code form is an open-source document, the Document, that was written by and contains intellectual property. The Document consists of documents, files, source code, technology design files, art, and other content contained this file, folder and the GitHub repository located at the Repository. The Document is published under the Kabuki Strong Source-available License, the License, which is a non-commercial open-source license and is for educational and demonstration purposes only. You may use, reproduce, publicly display, and modify the Document so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repository as an Issue ticket to become part of the Document. You may not sell the Document or otherwise profit from derivative works created from the Document without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Document distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
