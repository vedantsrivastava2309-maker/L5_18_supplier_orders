# Lab 5: Static Code Analysis — Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security — Medium | Original line 11 | SQL values were inserted using string formatting, which could allow malicious input to alter the query. | Used parameterized SQL queries with placeholders. |
| Unsafe shell execution | Security — High | Original line 21 | `os.system()` executed a shell command containing a concatenated supplier value. | Replaced shell execution with a Python `print()` statement. |
| Suppressed exceptions | Code quality / reliability — Low | Original lines 25–28 | A broad exception handler silently ignored errors, making failures difficult to detect. | Removed the unnecessary try/except block. |
| Missing documentation | Maintainability | Throughout original file | The module and functions lacked docstrings explaining their purpose. | Added module and function docstrings. |
| Non-standard function names | Style | Original lines 9, 16, 20, 31 | CamelCase function names did not follow Python's snake_case convention. | Renamed functions using snake_case. |
| Global mutable state | Code quality | Original lines 6, 10 | A global variable and `global` statement made the order total harder to maintain. | Calculated the order total locally in `main()`. |
| Long lines and spacing | Style | Original lines 5, 11, 32 | Several lines exceeded the recommended length, and an operator lacked surrounding spaces. | Reformatted statements across multiple lines and corrected spacing. |
| Unused remarks parameter | Code quality | Original line 16 | The `remarks` argument was accepted but not saved to the database. | Added a `remarks` column and stored the value when marking an order received. |
