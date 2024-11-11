import pytest
import exercise5

@pytest.mark.parametrize("input_num, expected_output", [
    (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
    (5, ['1', '2', 'Fizz', '4', 'Buzz']),
    (3, ['1', '2', 'Buzz']),
    (7, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7'])
])
def test_fizzBuzz(input_num, expected_output):
    assert exercise5.fizzBuzz(input_num) == expected_output