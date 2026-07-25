def safe_divide(numerator_str, denominator_str):
    try:
        numerator = float(numerator_str)
        denominator = float(denominator_str)
    except ValueError:
        return "Invalid number format"
    else:
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return "Cannot divide by zero"
