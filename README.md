# String Calculator TDD Kata

A simple string calculator implementation following Test-Driven Development principles.

## Features

The calculator can:

- Handle empty strings (returns 0)
- Add up to 1-2 numbers separated by commas (e.g., "1" or "1,2")
- Handle an unknown amount of numbers (e.g., "1,2,3,4,5")
- Allow new lines between numbers as an alternative delimiter (e.g., "1\n2,3")
- Support custom delimiters defined as `//[delimiter]\n[numbers]` (e.g., "//;\n1;2")
- Throw exceptions for negative numbers with appropriate error messages
- Ignore numbers larger than 1000 (e.g., "2,1001" returns 2)
- Support delimiters of any length with format `//[delimiter]\n` (e.g., "//[***]\n1***2***3")
- Allow multiple delimiters with format `//[delim1][delim2]\n` (e.g., "//[*][%]\n1*2%3")

## How to Run Tests

```bash
python3 -m unittest test_string_calculator.py
```

Use the `-v` flag for more verbose output:

```bash
python3 -m unittest test_string_calculator.py -v
```

## Development Approach

This project was developed following TDD (Test-Driven Development) principles:

1. Write a failing test for a specific functionality
2. Write the minimal code to make the test pass
3. Refactor the code while ensuring tests still pass
4. Repeat for each new feature

Each feature was implemented incrementally, with tests driving the design and implementation decisions.

## Code Structure

- `string_calculator.py` - Contains the StringCalculator class with the add method
- `test_string_calculator.py` - Contains the unit tests for verifying functionality
