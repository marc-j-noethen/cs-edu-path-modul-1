def write_lines(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
