def even_numbers(numbers: list) -> list:
    """Given a list of numbers, this function returns a new list containing only the even numbers from the original list.

    Args:
        numbers(list): A list of integers,e.g. [1,2,3,4]

    Returns:
        result (list): A list of even integers,e.g. [2,4]
    """
    result = [x for x in numbers if x % 2 == 0]

    return result