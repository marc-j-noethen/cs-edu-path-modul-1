def safe_int_convert(input_string):
    try:
        return int(input_string)
    except (ValueError, TypeError):
        return None
