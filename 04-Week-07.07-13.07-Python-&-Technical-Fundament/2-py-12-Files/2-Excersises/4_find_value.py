def find_value(filename, key):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith(key + ":"):
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        value_part = parts[1].strip()
                        try:
                            return int(value_part)
                        except ValueError:
                            return None
        return None
    except OSError:
        return None
