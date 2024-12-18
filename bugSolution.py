def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 1
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None  # or raise the exception, or return a default value