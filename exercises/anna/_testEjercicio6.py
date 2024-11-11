import pytest
import exercise6
# from exercise6 import exercise6

def test_ordinal_suffix(): 
  assert exercise6.ordinalSuffix(3) == '3rd'
  assert exercise6.ordinalSuffix(55) == '55toh'
  assert exercise6.ordinalSuffix(311) == '311th'
  assert exercise6.ordinalSuffix(18) == '18th'
