"""
    A Reverse Polish Notation calculator.

    Taking an input from the user via the command line, the program
    calculates the result. For example, "5 2 /" => 2
"""

def _add(num_one: int, num_two: int) -> int:
    """
        The addition function
        :params num_one: an integer which is one part of the sum
        :params num_two: an integer which is the other part of the sum
        :return: the result of adding the two parameters together
    """
    return num_one + num_two


def _subtract(num_one: int, num_two: int) -> int:
    """
        The subtraction function
        :params num_one: an integer which is one part of the subtraction
        :params num_two: an integer which is the other part of the substraction
        :return: the result of subtracting the second parameter from the first
    """
    return num_one - num_two


def _multiply(num_one: int, num_two: int) -> int:
    """
        The multiplication function
        :params num_one: an integer which is one part of the multiplication
        :params num_two: an integer which is the other part of the multiplication
        :return: the result of multiplying the two parameters
    """
    return num_one * num_two


def _division(num_one: int, num_two: int) -> int:
    """
        The division function
        :params num_one: an integer which is one part of the division
        :params num_two: an integer which is the other part of the division
        :return: the result of dividing the first parameter by the second. 
                A whole number is returned, i.e., 5 2 / -> 2 (not 2.5)
    """
    return num_one // num_two


def _modulo(num_one: int, num_two: int) -> int:
    """
        The modulo function
        :params num_one: an integer which is one part of the modulo 
        :params num_two: an integer which is the other part of the modulo
        :return: the remainder
    """
    return num_one % num_two

