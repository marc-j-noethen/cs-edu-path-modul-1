def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return sum(1 for _ in file)
    except OSError:
        return 0
