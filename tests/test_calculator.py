"""
Comprehensive test suite for the calculator module.

This module tests all arithmetic operations with various input types
including integers, floats, negative numbers, zero, and edge cases.
"""

import pytest
from src.calculator import add, subtract, multiply, divide, calculate


class TestAddition:
    """Test cases for the add function."""

    def test_add_positive_integers(self):
        """Test addition of two positive integers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(100, 1) == 101

    def test_add_negative_integers(self):
        """Test addition with negative integers."""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5
        assert add(10, -5) == 5

    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
        assert add(-1.5, 2.5) == 1.0

    def test_add_mixed_types(self):
        """Test addition of integers and floats."""
        assert add(5, 2.5) == 7.5
        assert add(2.5, 5) == 7.5
        assert add(-3, 1.5) == -1.5

    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(1e10, 2e10) == 3e10


class TestSubtraction:
    """Test cases for the subtract function."""

    def test_subtract_positive_integers(self):
        """Test subtraction of two positive integers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 2) == 8
        assert subtract(100, 50) == 50

    def test_subtract_negative_integers(self):
        """Test subtraction with negative integers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, 5) == -15
        assert subtract(10, -5) == 15

    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(-5, 0) == -5

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(3.3, 1.1) == pytest.approx(2.2)
        assert subtract(-1.5, 2.5) == -4.0

    def test_subtract_mixed_types(self):
        """Test subtraction of integers and floats."""
        assert subtract(5, 2.5) == 2.5
        assert subtract(2.5, 5) == -2.5
        assert subtract(-3, 1.5) == -4.5

    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative numbers."""
        assert subtract(3, 5) == -2
        assert subtract(0, 10) == -10


class TestMultiplication:
    """Test cases for the multiply function."""

    def test_multiply_positive_integers(self):
        """Test multiplication of two positive integers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20
        assert multiply(10, 10) == 100

    def test_multiply_negative_integers(self):
        """Test multiplication with negative integers."""
        assert multiply(-5, -3) == 15
        assert multiply(-10, 5) == -50
        assert multiply(10, -5) == -50

    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(-5, 0) == 0
        assert multiply(0, -5) == 0

    def test_multiply_with_one(self):
        """Test multiplication with one (identity)."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5
        assert multiply(-5, 1) == -5
        assert multiply(1, -5) == -5

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 2.0) == 5.0
        assert multiply(1.5, 3.0) == 4.5
        assert multiply(-2.5, 2.0) == -5.0

    def test_multiply_mixed_types(self):
        """Test multiplication of integers and floats."""
        assert multiply(5, 2.5) == 12.5
        assert multiply(2.5, 4) == 10.0
        assert multiply(-3, 1.5) == -4.5

    def test_multiply_large_numbers(self):
        """Test multiplication of large numbers."""
        assert multiply(1000, 1000) == 1000000
        assert multiply(1e5, 1e5) == 1e10


class TestDivision:
    """Test cases for the divide function."""

    def test_divide_positive_integers(self):
        """Test division of two positive integers."""
        assert divide(6, 3) == 2.0
        assert divide(10, 2) == 5.0
        assert divide(100, 4) == 25.0

    def test_divide_negative_integers(self):
        """Test division with negative integers."""
        assert divide(-6, -3) == 2.0
        assert divide(-10, 5) == -2.0
        assert divide(10, -5) == -2.0

    def test_divide_with_result_fraction(self):
        """Test division resulting in fractional numbers."""
        assert divide(5, 2) == 2.5
        assert divide(7, 4) == 1.75
        assert divide(1, 3) == pytest.approx(0.333333, rel=1e-5)

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(5.0, 2.5) == 2.0
        assert divide(7.5, 2.5) == 3.0
        assert divide(-10.0, 2.5) == -4.0

    def test_divide_mixed_types(self):
        """Test division of integers and floats."""
        assert divide(10, 2.5) == 4.0
        assert divide(7.5, 3) == 2.5
        assert divide(-9, 1.5) == -6.0

    def test_divide_by_zero_integer(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_by_zero_float(self):
        """Test division by zero float raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0.0)

    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        assert divide(0, 5) == 0.0
        assert divide(0, -5) == 0.0
        assert divide(0, 2.5) == 0.0

    def test_divide_by_one(self):
        """Test division by one (identity)."""
        assert divide(5, 1) == 5.0
        assert divide(-5, 1) == -5.0
        assert divide(2.5, 1) == 2.5

    def test_divide_large_numbers(self):
        """Test division of large numbers."""
        assert divide(1000000, 1000) == 1000.0
        assert divide(1e10, 1e5) == 1e5


class TestCalculateFunction:
    """Test cases for the unified calculate function."""

    def test_calculate_add(self):
        """Test calculate function with add operation."""
        assert calculate('add', 2, 3) == 5
        assert calculate('add', -5, 3) == -2
        assert calculate('add', 2.5, 3.5) == 6.0

    def test_calculate_subtract(self):
        """Test calculate function with subtract operation."""
        assert calculate('subtract', 5, 3) == 2
        assert calculate('subtract', -5, -3) == -2
        assert calculate('subtract', 5.5, 2.5) == 3.0

    def test_calculate_multiply(self):
        """Test calculate function with multiply operation."""
        assert calculate('multiply', 2, 3) == 6
        assert calculate('multiply', -5, 3) == -15
        assert calculate('multiply', 2.5, 4) == 10.0

    def test_calculate_divide(self):
        """Test calculate function with divide operation."""
        assert calculate('divide', 6, 3) == 2.0
        assert calculate('divide', -10, 5) == -2.0
        assert calculate('divide', 5, 2) == 2.5

    def test_calculate_divide_by_zero(self):
        """Test calculate function with divide by zero."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculate('divide', 5, 0)

    def test_calculate_invalid_operation(self):
        """Test calculate function with invalid operation name."""
        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('modulo', 5, 3)

        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('power', 2, 3)

        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('', 5, 3)

    def test_calculate_invalid_operation_shows_valid_operations(self):
        """Test that error message includes valid operations."""
        with pytest.raises(ValueError, match="Valid operations are"):
            calculate('invalid', 5, 3)

    def test_calculate_case_sensitive(self):
        """Test that operation names are case-sensitive."""
        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('Add', 2, 3)

        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('ADD', 2, 3)

        with pytest.raises(ValueError, match="Unknown operation"):
            calculate('SUBTRACT', 5, 3)

    def test_calculate_all_operations_comprehensive(self):
        """Comprehensive test of all operations through calculate."""
        # Test various edge cases through the unified interface
        assert calculate('add', 0, 0) == 0
        assert calculate('subtract', 0, 0) == 0
        assert calculate('multiply', 0, 5) == 0
        assert calculate('divide', 0, 5) == 0.0

        # Test with negative numbers
        assert calculate('add', -10, -5) == -15
        assert calculate('subtract', -10, -5) == -5
        assert calculate('multiply', -10, -5) == 50
        assert calculate('divide', -10, -5) == 2.0


class TestPackageImport:
    """Test cases for package-level imports."""

    def test_import_from_package(self):
        """Test that functions can be imported from the package."""
        from src import add, subtract, multiply, divide, calculate

        # Test that imported functions work correctly
        assert add(2, 3) == 5
        assert subtract(5, 3) == 2
        assert multiply(2, 3) == 6
        assert divide(6, 3) == 2.0
        assert calculate('add', 2, 3) == 5

    def test_package_version(self):
        """Test that package has a version attribute."""
        import src
        assert hasattr(src, '__version__')
        assert src.__version__ == '0.1.0'

    def test_package_all_attribute(self):
        """Test that package __all__ contains expected functions."""
        import src
        assert hasattr(src, '__all__')
        expected_exports = ['add', 'subtract', 'multiply', 'divide', 'calculate']
        assert set(src.__all__) == set(expected_exports)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        assert add(1e-10, 1e-10) == pytest.approx(2e-10)
        assert subtract(1e-10, 1e-11) == pytest.approx(9e-11, rel=1e-5)
        assert multiply(1e-5, 1e-5) == pytest.approx(1e-10)
        assert divide(1e-10, 1e-5) == pytest.approx(1e-5)

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        assert add(1e15, 1e15) == 2e15
        assert subtract(1e15, 1e14) == 9e14
        assert multiply(1e10, 1e5) == 1e15
        assert divide(1e15, 1e10) == 1e5

    def test_floating_point_precision(self):
        """Test floating point arithmetic precision."""
        # Test cases where floating point precision matters
        result = add(0.1, 0.2)
        assert result == pytest.approx(0.3)

        result = subtract(0.3, 0.1)
        assert result == pytest.approx(0.2)

        result = multiply(0.1, 0.1)
        assert result == pytest.approx(0.01)

    def test_operations_order_independence(self):
        """Test that operations can be called in any order (stateless)."""
        # These tests ensure functions are stateless and independent
        result1 = add(5, 3)
        result2 = multiply(2, 4)
        result3 = subtract(10, 5)
        result4 = divide(20, 4)

        assert result1 == 8
        assert result2 == 8
        assert result3 == 5
        assert result4 == 5.0

        # Reverse order
        result4b = divide(20, 4)
        result3b = subtract(10, 5)
        result2b = multiply(2, 4)
        result1b = add(5, 3)

        assert result1b == result1
        assert result2b == result2
        assert result3b == result3
        assert result4b == result4
