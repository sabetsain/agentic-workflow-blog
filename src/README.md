# Calculator Module - Quick Reference

## Installation

```bash
pip install -e .
# or with dev dependencies
pip install -e ".[dev]"
```

## Import

```python
from src.calculator import add, subtract, multiply, divide, calculate
# or
from src import add, subtract, multiply, divide, calculate
```

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
