# Calculator Module - Quick Reference

## Overview

A simple, well-tested Python calculator with a **modular architecture**. Each arithmetic operation is implemented in its own isolated module for better maintainability, scalability, and testability.

## Installation

```bash
pip install -e .
# or with dev dependencies
pip install -e ".[dev]"
```

## Import

```python
# Standard import (recommended)
from src.calculator import add, subtract, multiply, divide, calculate

# Alternative: Import from package root
from src import add, subtract, multiply, divide, calculate

# Alternative: Import directly from operations module
from src.operations import add, subtract, multiply, divide
```

## Project Structure

```
src/
├── __init__.py              # Package exports
├── calculator.py            # Main dispatcher with calculate()
└── operations/              # Modular operations package
    ├── __init__.py          # Operations exports
    ├── addition.py          # add() function
    ├── subtraction.py       # subtract() function
    ├── multiplication.py    # multiply() function
    └── division.py          # divide() function
```

### Modular Architecture Benefits

✓ **Isolation** - Each operation is self-contained  
✓ **Maintainability** - Easy to modify individual operations  
✓ **Testability** - Operations can be tested independently  
✓ **Scalability** - New operations can be added as separate modules  
✓ **Backward Compatible** - All existing APIs work unchanged

## API Quick Reference

| Function | Description | Example | Returns |
|----------|-------------|---------|---------|
| `add(a, b)` | Add two numbers | `add(5, 3)` | `8` |
| `subtract(a, b)` | Subtract b from a | `subtract(10, 4)` | `6` |
| `multiply(a, b)` | Multiply two numbers | `multiply(3, 7)` | `21` |
| `divide(a, b)` | Divide a by b | `divide(10, 2)` | `5.0` |
| `calculate(op, a, b)` | Unified interface | `calculate('add', 5, 3)` | `8` |

## Error Handling

- `divide(a, 0)` raises `ValueError: Cannot divide by zero`
- `calculate('invalid', a, b)` raises `ValueError: Unknown operation: invalid`
- Valid operations: `'add'`, `'subtract'`, `'multiply'`, `'divide'` (lowercase only)

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=term-missing
```

## Full Documentation

See [CALCULATOR.md](../CALCULATOR.md) for complete documentation with detailed examples.
