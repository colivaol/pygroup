import pytest
from leap_year import is_leap_year

@pytest.mark.parametrize("input_num, expected_output", [
  (2000, True),
  (1700, False),
  (2008, True),
  (2017, False)
])

def test_is_leap_year(input_num, expected_output):
  assert is_leap_year(input_num) == expected_output
