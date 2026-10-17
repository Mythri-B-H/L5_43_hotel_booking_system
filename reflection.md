@'
# Lab 5 Reflection

Static code analysis helped identify code-quality, security, and formatting problems in the hotel booking system.

Pylint helped improve naming, documentation, exception handling, and overall code quality. The final score was 10.00/10.

Bandit identified security risks such as unsafe expression evaluation, weak hashing, predictable random values, shell execution, and hardcoded secrets. These were addressed, and the final scan reported no issues.

Flake8 identified formatting violations, unused imports and variables, and other style problems. The final scan reported no violations.

This lab demonstrated that using multiple static analysis tools helps improve code readability, maintainability, and security.
'@ | Set-Content -Encoding utf8 reflection.md