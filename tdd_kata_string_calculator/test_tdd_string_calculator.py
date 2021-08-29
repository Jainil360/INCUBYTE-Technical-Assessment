import tdd_string_calculator as calc

def test_empty_string():
    assert calc.add('') == 0

def test_single_number_string():
    assert calc.add('6') == 6
    assert calc.add('0') == 0