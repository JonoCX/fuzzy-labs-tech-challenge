"""
    Tests for the calculator/rpn_calculator.py file.
"""

import pytest
import calculator.rpn_calculator as rpn 


class TestCalculations:

    @pytest.fixture(autouse = True)
    def capsys(self, capsys):
        """ This fixture enables us to capture the output to the terminal """
        self.capsys = capsys


    def test_addition_func(self):
        """ Test that the addition function is working as expected """
        assert rpn._add(5, 2) == 7


    def test_subtraction_func(self):
        """ Test that the subtraction function is working as expected """
        assert rpn._subtract(5, 2) == 3


    def test_multiplication_func(self):
        """ Test that the multiplication function is working as expected """
        assert rpn._multiply(5, 2) == 10


    def test_division_func(self):
        """ Test that the division function is working as expected """
        assert rpn._division(5, 2) == 2 


    def test_modulo_func(self):
        """ Test that the modulo function is working as expected """
        assert rpn._modulo(5, 2) == 1


    def test_addition(self):
        """ Test the addition function with an RPN expression """
        # call the main function to mock input into the calculator
        rpn.main('10 5 +')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 15
        assert int(out) == 15 


    def test_substraction(self):
        """ Test the subtraction function with an RPN expression """
        # call the main function to mock input 
        rpn.main('10 5 -')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 5
        assert int(out) == 5


    def test_multiplication(self):
        """ Test the multiplication function an RPN expression """
        # call the main function to mock input
        rpn.main('10 5 *')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 50
        assert int(out) == 50


    def test_division(self):
        """ Test the divison function an RPN expression """
        # call the main function to mock input
        rpn.main('5 2 /')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 2
        assert int(out) == 2


    def test_modulo(self):
        """ Test the modulo function an RPN expression """
        # call the main function to mock input
        rpn.main("5 2 %")

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 1
        assert int(out) == 1


    def test_multiple_operation_expression(self):
        """ Test a slightly more complicated expression with multiple operations """
        # call the main function to mock input
        rpn.main('4 7 + 2 *')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 22
        assert int(out) == 22


    def test_multiple_operation_expression_complex(self):
        """ Test a complex expression with multiple operations """
        # call the main function to mock input
        rpn.main('2 3 * 11 14 * +')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 160
        assert int(out) == 160        


    def test_multiple_operation_expression_complex_equal_zero(self):
        """ Test a complex expression where the answer should be 0 (but is 0.33 with infix) """
        # call the main function to mock input
        rpn.main('5 4 * 2 3 * / 7 2 % 4 - +')

        # capture the output to the terminal
        out, _ = self.capsys.readouterr()

        # the result should be 0
        assert int(out) == 0


class TestInput:

    @pytest.fixture(autouse = True)
    def capsys(self, capsys):
        """ This fixture enables us to capture the output to the terminal """
        self.capsys = capsys

    
    def test_input_works_as_expected(self):
        """ Test that the input works as expected before testing for other things """
        # this will trigger the calculator to perform the calculation
        rpn.main('5 2 /')

        # capture the output of the program
        out, _ = self.capsys.readouterr()

        # the result should be 2
        assert int(out) == 2

    def test_empty_input(self):
        """ 
            Test that the calculator prints an appropriate message and 
            exits when an empty input is passed.
        """
        with pytest.raises(SystemExit) as empty_exit:
            # this will trigger the message to be printed and a sys.exit to occur
            rpn.main('') 

            # capture that commandline output and assert that it's what we expect
            out, _ = self.capsys.readouterr()

            assert out == 'No RPN expression provided.'
        
        # check that the type of exception through is correct
        assert empty_exit.type == SystemExit


    def test_that_system_exits_when_single_input_given(self):
        """
            Test that the appropriate error message is present to the user and
            that the system exits when only a single input is given, i.e., '5'
        """
        with pytest.raises(SystemExit) as single_input_error:
            # this will trigger the error message to appear and the system to exit
            rpn.main('5')

            # capture the output to the command line
            out, _ = self.capsys.readouterr()

            # assert that the it is the correct error message
            assert out == "Only a single value has been inputted: '5'; " \
                            "this could be due to the lack of of spaces in the expression"

        # check that the type of error is correct
        assert single_input_error.type == SystemExit


    
    def test_that_input_with_no_spaces_is_rejected(self):
        """
            Test that when the user provides an expression where there are no spaces,
            the calculator detects it, prints the error message, and exists
        """
        with pytest.raises(SystemExit) as no_spaces_error:
            # this will trigger the error message to appear and the system to exit
            rpn.main('52/')

            # capture the output to the command line
            out, _ = self.capsys.readouterr()

            # assert that it is the correct error message
            assert out == "Only a single value has been inputted: '52/'; " \
                        "this could be due to the lack of of spaces in the expression.\n"

        # check that the type of error is correct
        assert no_spaces_error.type == SystemExit


    def test_that_only_allowed_operations_can_be_provided(self):
        """
            Test that the calculator only accepts the operators (+ - * / %). For example, 
            it isn't suppose to accept expressions with exponentiation.
        """
        with pytest.raises(SystemExit) as invalid_operator_error:
            # this will trigger the error message to appear as it's attempting to calculate
            # an exponentiation.
            rpn.main('5 2 **')

            # capture the output to the command line
            out, _ = self.capsys.readouterr()

            # assert that it is the correct error message
            assert out == "Invalid input given: '**'; only whole numbers are accepted " \
                            "and (+ - * / %) are the only operators allowed.\n"

        # check that the type of error is correct
        assert invalid_operator_error.type == SystemExit


    def test_that_text_instead_of_numbers_is_rejected(self):
        """
            Test that when the user provides an expression which includes something
            that is not a number, i.e., 'two' instead of 2, that an appropriate
            message is displayed and that the system exits
        """
        with pytest.raises(SystemExit) as inappropriate_input_exit:
            # this will trigger an output which tells the user they cannot have 'two' in the input
            rpn.main('5 two /')

            # capture the commandline output
            out, _ = self.capsys.readouterr()

            # assert that the output matches what we would expect
            assert out == "Invalid input given: 'two'; only whole numbers are accepted " \
                            "and (+ - * / %) are the only operators allowed.\n"
        
        # check that the system exits
        assert inappropriate_input_exit.type == SystemExit


    def test_that_only_whole_numbers_are_accepted(self):
        """
            Test that only whole numbers are accepted, i.e., 2.5 should not be accepted as
            part of an expression.
        """
        with pytest.raises(SystemExit) as inappropriate_input_exit:
            # this will trigger an output which tells the users they cannot have 2.5 in the input
            rpn.main('5 2.5 /')
            
            # capture the commandline output
            out, _ = self.capsys.readouterr()

            # assert that the output matches what we would expect
            assert out == "Invalid input given: '2.5'; only whole numbers are accepted.\n"

        # assert that system exits under type of input
        assert inappropriate_input_exit.type == SystemExit
