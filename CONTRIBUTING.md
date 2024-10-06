# How to contribute

This document is a guide to contributing to NightRunner Purgatory. It is/will be a compilation of advice from various authors, updated as needed.

## Onboarding

Hello! So you've decided you want to do gamedev? Well, here's your onboarding that you should go through as you need to be familiar with the entirety of the project.

This onboarding section will help you get familiar with the genre, provide a roguelike development crash course, and set up your tooling for programming.

### Beginner Tutorials

This game was really inspired by [Roguelike Tutorials](https://rogueliketutorials.com/) which contains a tutorial in Python using the TCOD library. I would highly suggest **highly** suggest working through the entirety of this tutorial. This tutorial will help you learn a lot of basics of Python, your favorite IDE, and fundamental features of roguelikes. This tutorial will only cover Python and TCOD. Pygame usage is not covered.

*Note:* The setup instructions in this tutorial may conflict with the tools suggested below. That is because the tooling set up for this project is geared to be more repeatable/reproducible across multiple developers. I promise, it will be less painful in the long run with a little pain at the beginning.

### Tools

For this project, here's a list of tools that you should use:
- [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm Community Edition](https://www.jetbrains.com/pycharm/) for editing code
- [Scoop](https://scoop.sh/) for a command-line installer
- [pipx](https://github.com/pypa/pipx) *(skip for now)* as another command-line installer
- [Poetry](https://python-poetry.org/) as a dependency manager used for this project
- [Git](https://git-scm.com/) as the change management software
- [GitHub Desktop](https://github.com/apps/desktop) for easier commits/interfacing with GitHub

### Tool Setup Instructions

1. Open a PowerShell terminal.
2. Run the following commands to install Scoop (allow whatever permissions PowerShell asks for):
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
3. Upon successful installation of Scoop, run the following commands (you may need to close and open a new instance of PowerShell):
```
scoop install main/poetry
scoop install main/git
scoop install extras/github
```
4. Log into GitHub. (Register if you do not have an account)
5. Let me know what your account name is so I can grant you permissions to view the repository.
6. After you have been granted permissions, open GitHub desktop. After logging in, click "Add" -> "Clone Repository". Under URL, input: `https://github.com/nightconcept/nightrunner-purgatory.git` and click "Clone".
7. Congrats, you now have a local copy to work with! All of your work should be done on a branch. I won't be teaching git basics, so you can refer to a video like this one: [Git and GitHub for Beginners - Crash Course - YouTube](https://www.youtube.com/watch?v=RGOj5yH7evk).

## Coding style

When writing code, please adhere to the following rules:

* Indent with spaces, 1 indentation level = 4 spaces. And don't leave whitespace at the end of lines.
* Following [PEP-8](https://pep8.org/) styling where possible. A few of them will also be called out here.
* Limit all lines to a maximum of 79 characters for python files. Use a ruler in your IDE to help you.
* [Within each grouping, imports should be sorted lexicographically, ignoring case, according to each module’s full package path](https://google.github.io/styleguide/pyguide.html#313-imports-formatting). For example:
```
from collections.abc import Mapping, Sequence
import os
import sys
from typing import Any, NewType
```
* Use reStructuredText (reST) docstrings to label functions. Example:
```
"""
This is a reST style. This is the function description.

:param param1: This is a first param description.
:param param2: This is a second param description.
:returns: This is a description of what is returned.
:raises keyError: Raises an exception.
"""
```
* Provide typing hints for parameters and function returns. Use `Optional` and `Required` typings as needed.

## Commiting rules

Please adhere to the following rules:
* Commits should follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) standard.
* Commits should not break on run or tests (if they exist).
* Changes in one commit should not be too extensive, unless necessary.

## Submitting pull requests

After you finish working on your issue and want your code to be merged into the main repository, you should submit a **pull request**. Go to [this page](https://github.com/nightconcept/nightrunner-purgatory/pulls) and select "New pull request".
If you need more help, see [GitHub's help page on Pull Requests](https://help.github.com/articles/using-pull-requests/).

## Need help?

Ask in #code-help on our Discord!