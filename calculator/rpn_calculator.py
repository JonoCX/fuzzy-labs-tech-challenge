"""
    A Reverse Polish Notation calculator.

    Taking an input from the user via the command line, the program
    calculates the result. For example, "5 2 /" => 2
"""
import sys

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


"""
    Create a mapping between the operations that are allowed to be 
    inputted by the user and their corresponding functions. 
    Also acts as a way to check for valid input.
"""
operations = {
    '+': _add, 
    '-': _subtract, 
    '*': _multiply, 
    '/': _division, 
    '%': _modulo
}


def _calculator(in_expression):
    """
        The RPN calculator. 
        Given an input, e.g. "5 2 /", the calcuator returns the result, e.g. 2
        :params in_expression: the input into the calculator - the expression that 
                                is to be calculated
        :return: the result of carrying out the expression
    """
    # split the input into its components, e.g., "5 2 /" -> [5, 2, /]
    expression_components = in_expression.split()

    if len(expression_components) == 1:
        print(f"Only a single value has been inputted: '{expression_components[0]}'; this could" \
            " be due to a lack of spaces in the expression.")
        sys.exit()

    stack = []
    for part in expression_components:
        # if the part is an operation (e.g. /)
        if part in operations.keys():
            
            # get the second number (e.g., 2)
            num_two = stack.pop()

            # get the first number (e.g., 5)
            num_one = stack.pop()

            # use the operator to get the correct function and pass the two numbers
            result = operations[part](num_one, num_two)

            # add the result to the stack
            stack.append(result)
        # otherwise it's a number
        else: 
            # try to convert the input into an integer
            try:
                # and add to the stack
                stack.append(int(part))
            # if it is anything other than a whole number (float or text), 
            # an exception is thrown and caught
            except ValueError:
                # Report back the suspected error to the user and terminate the program
                print(f"Invalid input given: '{part}'; only whole numbers are accepted " \
                    "and (+ - * / %) are the only operators allowed.")
                sys.exit()
    
    # return the result
    return stack.pop()

            
def main(in_expression):
    """
        The main function where the calculator is called based on the input from the
        user
        :params in_expression: the input from the user
    """
    # the user has supplied an empty input
    if not in_expression:
        print('No RPN expression provided.')
        sys.exit()

    # fetch the result and print it
    result = _calculator(in_expression)
    print(result)


if __name__ == '__main__':
    in_expression = input()
    main(in_expression)