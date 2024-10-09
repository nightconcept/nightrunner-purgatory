# How to contribute

This document is a guide to contributing to NightRunner Purgatory. It is/will be a compilation of advice from various authors, updated as needed.

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
* Commits should not break on run or tests (if they exist).
* Changes in one commit should not be too extensive, unless necessary.

## Submitting pull requests

After you finish working on your issue and want your code to be merged into the main repository, you should submit a **pull request**. Go to [this page](https://github.com/nightconcept/nightrunner-purgatory/pulls) and select "New pull request".
If you need more help, see [GitHub's help page on Pull Requests](https://help.github.com/articles/using-pull-requests/).

## Need help?

Ask in #code-help on our Discord!