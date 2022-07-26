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