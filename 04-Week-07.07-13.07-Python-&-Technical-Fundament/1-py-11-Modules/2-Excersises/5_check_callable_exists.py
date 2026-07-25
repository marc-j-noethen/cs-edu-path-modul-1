import importlib


def check_callable_exists(module_name_string, callable_name_string):
    try:
        module = importlib.import_module(module_name_string)
    except ImportError:
        return False

    if not hasattr(module, callable_name_string):
        return False

    member = getattr(module, callable_name_string)
    return callable(member) and not callable_name_string.startswith("_")
