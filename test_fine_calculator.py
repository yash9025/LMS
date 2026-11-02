"""
Pytest Test Suite for Library Fine Calculator
Covers: Zero, Valid, Boundary, and Invalid input cases using parametrization and assertions.
"""

import pytest
from fine_calculator import calculate_fine


# Case 1: Zero Overdue Days
@pytest.mark.parametrize("days, expected_fine", [
    (0, 0.0),
])
def test_fine_zero_input(days, expected_fine):
    """Verifies that 0 overdue days incurs zero fine."""
    actual_fine = calculate_fine(days)
    assert actual_fine == expected_fine, f"Expected fine {expected_fine} for {days} days, got {actual_fine}"
    assert isinstance(actual_fine, float)


# Case 2: Valid Typical Overdue Days (Tier 1, Tier 2, and Tier 3)
@pytest.mark.parametrize("days, expected_fine", [
    (3, 3.0),     # Tier 1: 3 days * $1 = $3.0
    (8, 11.0),    # Tier 2: 5*1 + 3*2 = $11.0
    (15, 40.0),   # Tier 3: 5*1 + 5*2 + 5*5 = $40.0
    (20, 65.0),   # Tier 3: 5*1 + 5*2 + 10*5 = $65.0
])
def test_fine_valid_inputs(days, expected_fine):
    """Verifies calculated fine for typical valid overdue days across all rate tiers."""
    actual_fine = calculate_fine(days)
    assert actual_fine == expected_fine, f"Failed for {days} days. Expected {expected_fine}, got {actual_fine}"


# Case 3: Boundary Inputs
# Threshold boundaries:
# 0 (no fine)
# 1 (start of tier 1: $1)
# 5 (end of tier 1: 5 * $1 = $5)
# 6 (start of tier 2: 5 + 1*2 = $7)
# 10 (end of tier 2: 5 + 5*2 = $15)
# 11 (start of tier 3: 15 + 1*5 = $20)
@pytest.mark.parametrize("days, expected_fine", [
    (0, 0.0),
    (1, 1.0),
    (5, 5.0),
    (6, 7.0),
    (10, 15.0),
    (11, 20.0),
])
def test_fine_boundary_inputs(days, expected_fine):
    """Verifies fine calculations at exact tier transition boundaries."""
    actual_fine = calculate_fine(days)
    assert actual_fine == expected_fine, f"Boundary check failed for {days} days. Expected {expected_fine}, got {actual_fine}"


# Case 4: Invalid Inputs (Negative numbers and wrong data types)
@pytest.mark.parametrize("invalid_days, expected_exception", [
    (-1, ValueError),         # Negative boundary
    (-15, ValueError),        # Negative integer
    ("5", TypeError),         # String instead of int
    (4.5, TypeError),         # Float instead of int
    (None, TypeError),        # NoneType
    (True, TypeError),        # Boolean (bool is subclass of int in Python)
    ([3], TypeError),         # List
])
def test_fine_invalid_inputs(invalid_days, expected_exception):
    """Verifies that invalid input values and types raise appropriate exceptions."""
    with pytest.raises(expected_exception):
        calculate_fine(invalid_days)
