def calculate_fine(days):
    if type(days) is not int:
        raise TypeError("Days must be an integer")
    if days < 0:
        raise ValueError("Days cannot be negative")

    if days == 0:
        return 0
    elif days <= 5:
        return days * 1
    elif days <= 10:
        return 5 + (days - 5) * 2
    else:
        return 15 + (days - 10) * 5
