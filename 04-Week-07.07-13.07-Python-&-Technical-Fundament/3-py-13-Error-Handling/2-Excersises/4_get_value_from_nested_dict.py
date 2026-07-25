def get_value_from_nested_dict(data_dict, keys):
    current = data_dict
    last_key = None

    for key in keys:
        if not isinstance(current, dict):
            return f"Invalid path: Not a dictionary at key {last_key}"
        try:
            current = current[key]
        except KeyError as error:
            return f"Key not found: {repr(error.args[0])}"
        last_key = key

    return current
