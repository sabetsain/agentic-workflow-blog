# Calculator Module Documentation

A simple, well-tested Python calculator module providing basic arithmetic operations.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
  - [add()](#add)
  - [subtract()](#subtract)
  - [multiply()](#multiply)
  - [divide()](#divide)
  - [calculate()](#calculate)
- [Usage Examples](#usage-examples)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Overview

The calculator module provides five functions for performing basic arithmetic operations:

- **Individual operation functions**: `add()`, `subtract()`, `multiply()`, `divide()`
- **Unified interface**: `calculate()` - accepts operation name as a string

All functions support both integers and floating-point numbers, handle edge cases gracefully, and include comprehensive error handling.

### Features

✓ Simple, intuitive API  
✓ Support for integers and floats  
✓ Handles negative numbers and zero  
✓ Division by zero protection  
✓ Type-flexible (works with mixed int/float inputs)  
✓ 100% test coverage  
✓ Well-documented with docstrings  

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Basic Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd agentic-workflow-blog
   ```

2. **Install the package** (optional, for importing as a package):
   ```bash
   pip install -e .
   ```

3. **Install development dependencies** (for testing):
   ```bash
   pip install -e ".[dev]"
   ```
   
   Or manually:
   ```bash
   pip install pytest pytest-cov
   ```

## Quick Start

```python
from src.calculator import add, subtract, multiply, divide, calculate

# Using individual functions
result = add(10, 5)          # Returns: 15
result = subtract(10, 5)     # Returns: 5
result = multiply(10, 5)     # Returns: 50
result = divide(10, 5)       # Returns: 2.0

# Using the unified calculate function
result = calculate('add', 10, 5)        # Returns: 15
result = calculate('subtract', 10, 5)   # Returns: 5
result = calculate('multiply', 10, 5)   # Returns: 50
result = calculate('divide', 10, 5)     # Returns: 2.0
```

## API Reference

### add()

Add two numbers together.

**Signature:**
```python
add(a, b)
```

**Parameters:**
- `a` (int or float): First number
- `b` (int or float): Second number

**Returns:**
- `int or float`: Sum of a and b

**Example:**
```python
add(5, 3)        # Returns: 8
add(-2, 7)       # Returns: 5
add(2.5, 3.5)    # Returns: 6.0
add(10, -4)      # Returns: 6
```

---

### subtract()

Subtract the second number from the first number.

**Signature:**
```python
subtract(a, b)
```

**Parameters:**
- `a` (int or float): First number (minuend)
- `b` (int or float): Second number (subtrahend)

**Returns:**
- `int or float`: Difference of a and b (a - b)

**Example:**
```python
subtract(10, 3)      # Returns: 7
subtract(5, 10)      # Returns: -5
subtract(7.5, 2.5)   # Returns: 5.0
subtract(-3, -5)     # Returns: 2
```

---

### multiply()

Multiply two numbers.

**Signature:**
```python
multiply(a, b)
```

**Parameters:**
- `a` (int or float): First number
- `b` (int or float): Second number

**Returns:**
- `int or float`: Product of a and b

**Example:**
```python
multiply(4, 5)       # Returns: 20
multiply(-3, 6)      # Returns: -18
multiply(2.5, 4)     # Returns: 10.0
multiply(-2, -3)     # Returns: 6
```

---

### divide()

Divide the first number by the second number.

**Signature:**
```python
divide(a, b)
```

**Parameters:**
- `a` (int or float): Numerator (dividend)
- `b` (int or float): Denominator (divisor)

**Returns:**
- `float`: Quotient of a divided by b

**Raises:**
- `ValueError`: If b is zero (division by zero)

**Example:**
```python
divide(10, 2)        # Returns: 5.0
divide(7, 2)         # Returns: 3.5
divide(-10, 5)       # Returns: -2.0
divide(0, 5)         # Returns: 0.0

# Error case
divide(10, 0)        # Raises: ValueError: Cannot divide by zero
```

---

### calculate()

Perform a calculation based on the specified operation string.

**Signature:**
```python
calculate(operation, a, b)
```

**Parameters:**
- `operation` (str): The operation to perform. Must be one of: `'add'`, `'subtract'`, `'multiply'`, `'divide'`
- `a` (int or float): First number
- `b` (int or float): Second number

**Returns:**
- `int or float`: Result of the calculation

**Raises:**
- `ValueError`: If operation is not recognized
- `ValueError`: If division by zero (when operation is 'divide' and b is zero)

**Example:**
```python
calculate('add', 5, 3)          # Returns: 8
calculate('subtract', 10, 4)    # Returns: 6
calculate('multiply', 3, 7)     # Returns: 21
calculate('divide', 15, 3)      # Returns: 5.0

# Error cases
calculate('power', 2, 3)        # Raises: ValueError: Unknown operation: power
calculate('divide', 5, 0)       # Raises: ValueError: Cannot divide by zero
```

**Note:** Operation names are case-sensitive. Use lowercase strings: `'add'`, not `'Add'` or `'ADD'`.

## Usage Examples

### Basic Arithmetic

```python
from src.calculator import add, subtract, multiply, divide

# Addition
total = add(100, 50)              # 150
balance = add(-25, 100)           # 75

# Subtraction
difference = subtract(100, 30)    # 70
debt = subtract(50, 100)          # -50

# Multiplication
area = multiply(5, 8)             # 40
product = multiply(-4, 3)         # -12

# Division
average = divide(100, 4)          # 25.0
ratio = divide(7, 2)              # 3.5
```

### Working with Decimals

```python
from src.calculator import add, subtract, multiply, divide

# Financial calculations
price = 19.99
tax = 2.50
total = add(price, tax)           # 22.49

# Percentage calculations
original = 100.0
discount = multiply(original, 0.15)  # 15.0
final_price = subtract(original, discount)  # 85.0

# Precise division
result = divide(1.0, 3.0)         # 0.333333...
```

### Using the Unified Interface

```python
from src.calculator import calculate

# Build a simple calculator function
def perform_calculation(op, x, y):
    try:
        result = calculate(op, x, y)
        print(f"{x} {op} {y} = {result}")
        return result
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Use it
perform_calculation('add', 10, 5)       # Output: 10 add 5 = 15
perform_calculation('multiply', 7, 8)   # Output: 7 multiply 8 = 56
perform_calculation('divide', 10, 0)    # Output: Error: Cannot divide by zero
```

### Chaining Operations

```python
from src.calculator import add, multiply, divide

# Calculate: (10 + 5) * 2 / 3
step1 = add(10, 5)           # 15
step2 = multiply(step1, 2)   # 30
result = divide(step2, 3)    # 10.0
```

## Error Handling

The calculator module includes robust error handling for common edge cases.

### Division by Zero

```python
from src.calculator import divide, calculate

# Direct division function
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error caught: {e}")
    # Output: Error caught: Cannot divide by zero

# Using calculate function
try:
    result = calculate('divide', 5, 0)
except ValueError as e:
    print(f"Error caught: {e}")
    # Output: Error caught: Cannot divide by zero
```

### Invalid Operations

```python
from src.calculator import calculate

# Invalid operation name
try:
    result = calculate('power', 2, 3)
except ValueError as e:
    print(f"Error caught: {e}")
    # Output: Error caught: Unknown operation: power. Valid operations are: add, subtract, multiply, divide

# Case sensitivity
try:
    result = calculate('ADD', 5, 3)  # Must be lowercase
except ValueError as e:
    print(f"Error caught: {e}")
    # Output: Error caught: Unknown operation: ADD. Valid operations are: add, subtract, multiply, divide
```

### Best Practices for Error Handling

```python
from src.calculator import calculate

def safe_calculate(operation, a, b):
    """
    Wrapper function with comprehensive error handling.
    """
    try:
        result = calculate(operation, a, b)
        return {'success': True, 'result': result}
    except ValueError as e:
        return {'success': False, 'error': str(e)}

# Usage
response = safe_calculate('divide', 10, 2)
if response['success']:
    print(f"Result: {response['result']}")
else:
    print(f"Error: {response['error']}")
```

## Testing

The calculator module includes comprehensive tests with 100% code coverage.

### Running Tests

**Run all tests:**
```bash
pytest tests/ -v
```

**Run with coverage report:**
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

**Run specific test class:**
```bash
pytest tests/test_calculator.py::TestAddition -v
```

**Run a specific test:**
```bash
pytest tests/test_calculator.py::TestAddition::test_add_positive_integers -v
```

### Test Coverage

The test suite includes 45 comprehensive tests covering:

- ✓ Positive integers
- ✓ Negative integers
- ✓ Zero handling
- ✓ Floating-point numbers
- ✓ Mixed integer/float operations
- ✓ Large numbers
- ✓ Very small numbers (scientific notation)
- ✓ Floating-point precision edge cases
- ✓ Division by zero error handling
- ✓ Invalid operation error handling
- ✓ Case sensitivity
- ✓ Package imports
- ✓ Stateless operation verification

### Test Output Example

```
tests/test_calculator.py::TestAddition::test_add_positive_integers PASSED
tests/test_calculator.py::TestAddition::test_add_negative_integers PASSED
tests/test_calculator.py::TestAddition::test_add_with_zero PASSED
tests/test_calculator.py::TestAddition::test_add_floats PASSED
...

---------- coverage: platform linux, python 3.x -----------
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
src/__init__.py             3      0   100%
src/calculator.py          26      0   100%
-----------------------------------------------------
TOTAL                      29      0   100%

===================== 45 passed in 0.15s =====================
```

## Project Structure

```
agentic-workflow-blog/
├── src/
│   ├── __init__.py          # Package initialization, exports all functions
│   └── calculator.py        # Main calculator implementation
├── tests/
│   └── test_calculator.py   # Comprehensive test suite (45 tests)
├── .gitignore               # Python-specific ignore patterns
├── pyproject.toml           # Package configuration and metadata
├── requirements.txt         # Dependencies (currently empty - no external deps)
├── CALCULATOR.md            # This documentation file
└── README.md                # Main repository README
```

### Key Files

**src/calculator.py**
- Contains all five calculator functions
- Includes comprehensive docstrings
- Implements error handling for edge cases
- No external dependencies

**src/__init__.py**
- Exports all calculator functions for easy importing
- Defines package version (`__version__ = '0.1.0'`)
- Lists public API in `__all__`

**tests/test_calculator.py**
- 45 comprehensive test cases
- Organized into 6 test classes by functionality
- Uses pytest framework
- Achieves 100% code coverage

**pyproject.toml**
- Modern Python package configuration
- Defines project metadata
- Specifies Python version requirement (>=3.8)
- Lists development dependencies (pytest, pytest-cov)

### Package Information

- **Name**: calculator
- **Version**: 0.1.0
- **Python Required**: 3.8 or higher
- **Dependencies**: None (core functionality)
- **Dev Dependencies**: pytest (>=7.0), pytest-cov (>=4.0)
- **License**: MIT

## Additional Resources

- **Source Code**: See `src/calculator.py` for implementation details
- **Tests**: See `tests/test_calculator.py` for usage examples and edge cases
- **Package Config**: See `pyproject.toml` for package metadata

## Contributing

When contributing to the calculator module:

1. Maintain backward compatibility
2. Add tests for new features
3. Update this documentation
4. Ensure 100% test coverage
5. Follow existing code style and conventions
6. Add docstrings to all new functions

## Support

For issues, questions, or contributions, please refer to the main repository README.
