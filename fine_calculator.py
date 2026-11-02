"""
Library Management System - Overdue Fine Calculator Module
"""

def calculate_fine(days: int) -> float:
    """
    Calculates the overdue fine for a library book based on the number of overdue days.
    
    Fine Schedule:
      - 0 days: $0.00 (No fine)
      - 1 to 5 days: $1.00 per day
      - 6 to 10 days: $5.00 base (first 5 days) + $2.00 per additional day (days 6-10)
      - Above 10 days: $15.00 base (first 10 days) + $5.00 per additional day (days 11+)
      
    Args:
      days (int): Number of overdue days. Must be a non-negative integer.
      
    Returns:
      float: The total calculated fine.
      
    Raises:
      TypeError: If 'days' is not an integer or is a boolean.
      ValueError: If 'days' is negative.
    """
    if isinstance(days, bool) or not isinstance(days, int):
        raise TypeError(f"Overdue days must be an integer, got {type(days).__name__}.")
    
    if days < 0:
        raise ValueError(f"Overdue days cannot be negative, got {days}.")
    
    if days == 0:
        return 0.0
    elif 1 <= days <= 5:
        return float(days * 1.0)
    elif 6 <= days <= 10:
        return float(5 * 1.0 + (days - 5) * 2.0)
    else:
        return float(5 * 1.0 + 5 * 2.0 + (days - 10) * 5.0)
