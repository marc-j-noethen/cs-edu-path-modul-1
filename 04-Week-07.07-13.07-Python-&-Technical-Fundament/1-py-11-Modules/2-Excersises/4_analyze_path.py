import os


def analyze_path(file_path_string):
    directory, filename = os.path.split(file_path_string)
    if directory == "":
        directory = "."
    name, extension = os.path.splitext(filename)
    return {
        "directory": directory,
        "filename": filename,
        "extension": extension,
    }
