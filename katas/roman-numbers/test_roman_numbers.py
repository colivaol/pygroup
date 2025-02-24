import pytest
from roman_numbers import roman_numbers_conversion


@pytest.mark.parametrize("input_num, expected_output", [
  (1, 'I'),
  (2, 'II'),
  (3, 'III'),
  (4, 'IV'),
  (5, 'V'),
  (9, 'IX'),
  (10, 'X'),
  (21, 'XXI'),
  (50, 'L'),
  (100, 'C'),
  (500, 'D'),
  (1000, 'M')
])

def test_roman_numbers_conversion(input_num, expected_output):
  assert roman_numbers_conversion(input_num) == expected_output