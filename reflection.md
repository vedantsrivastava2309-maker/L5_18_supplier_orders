# Lab 5: Static Code Analysis — Reflection

## 1. What did you learn from static code analysis?
I learned that static code analysis tools can detect coding mistakes, style issues, and security risks without executing the program. Pylint checks code quality, Flake8 checks coding style, and Bandit identifies common security problems.

## 2. Which security issues did you find?
The original program had an SQL injection risk because SQL queries used string formatting. It also used os.system() to execute a shell command containing supplier input. I fixed these issues by using parameterized SQL queries and replacing the shell command with a Python print statement.

## 3. Which tool was most useful, and why?
Bandit was useful for identifying security risks such as SQL injection and unsafe shell execution. Pylint helped improve code quality and documentation, while Flake8 identified formatting and spacing problems.

## 4. What did you learn from fixing the issues?
I learned to use parameterized SQL queries, avoid unnecessary shell commands, handle errors properly, use descriptive function names, and add docstrings. After fixing the issues, the program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no errors.
