# String Calculator TDD Kata

A string calculator implementation following Test-Driven Development principles. This project demonstrates a step-by-step TDD approach with commits at each stage to show the code evolution.

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

## TDD Approach

This project was developed using a strict TDD approach, with the following steps for each feature:

1. **RED**: Write a failing test
2. **GREEN**: Write the minimal code to make the test pass
3. **REFACTOR**: Refactor the code while ensuring tests still pass

### Commit History

Each step has been committed separately to show the evolution:

1. TDD Step 1: Empty string returns 0
2. TDD Step 2: Handle single number
3. TDD Step 3: Handle two numbers
4. TDD Step 4: Handle unknown amount of numbers
5. TDD Step 5: Handle new lines between numbers
6. TDD Step 6: Handle custom delimiters
7. TDD Step 7: Handle negative numbers - throw exception
8. TDD Step 8: Ignore numbers bigger than 1000
9. TDD Step 9: Handle delimiters of any length
10. TDD Step 10: Handle multiple delimiters

## Running the Tests

```bash
python3 -m unittest test_string_calculator.py
```

For verbose output:

```bash
python3 -m unittest test_string_calculator.py -v
```

## Files

- `string_calculator.py`: The string calculator implementation
- `test_string_calculator.py`: The test cases for the string calculator
