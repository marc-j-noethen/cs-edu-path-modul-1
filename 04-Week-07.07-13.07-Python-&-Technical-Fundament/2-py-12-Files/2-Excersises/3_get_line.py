def get_line(filename, line_number):
    if line_number < 1:
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for current_line_number, line in enumerate(file, start=1):
                if current_line_number == line_number:
                    return line.strip()
        return None
    except OSError:
        return None
