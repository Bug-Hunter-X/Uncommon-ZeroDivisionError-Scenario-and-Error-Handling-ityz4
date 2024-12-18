def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but also demonstrates an uncommon error handling scenario
    else:
        return x + 1