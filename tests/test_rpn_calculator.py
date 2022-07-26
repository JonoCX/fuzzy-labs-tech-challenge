"""
    Tests for the calculator/rpn_calculator.py file.
"""

import pytest
import calculator.rpn_calculator as rpn 


class TestCalculations:

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
