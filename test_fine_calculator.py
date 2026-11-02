import pytest
from fine_calculator import calculate_fine

# 1. Zero input
@pytest.mark.parametrize("days, expected", [
    (0, 0),
])
def test_zero_days(days, expected):
    assert calculate_fine(days) == expected

# 2. Valid inputs
@pytest.mark.parametrize("days, expected", [
    (3, 3),
    (8, 11),
    (15, 40),
])
def test_valid_days(days, expected):
    assert calculate_fine(days) == expected

# 3. Boundary inputs
@pytest.mark.parametrize("days, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (6, 7),
    (10, 15),
    (11, 20),
])
def test_boundary_days(days, expected):
    assert calculate_fine(days) == expected

# 4. Invalid inputs
@pytest.mark.parametrize("days, exception", [
    (-1, ValueError),
    ("5", TypeError),
    (3.5, TypeError),
    (None, TypeError),
])
def test_invalid_days(days, exception):
    with pytest.raises(exception):
        calculate_fine(days)
