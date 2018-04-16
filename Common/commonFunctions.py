def validate_numbers(list_of_numbers):
    for x in list_of_numbers:
        if not isinstance(x, int) and not isinstance(x, float):
            return False
    return True

