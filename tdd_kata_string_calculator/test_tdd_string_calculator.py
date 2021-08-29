import tdd_string_calculator as calc

def test_empty_string():
    assert calc.add('') == 0

def test_single_number_string():
    assert calc.add('6') == 6
    assert calc.add('0') == 0

def test_two_numbers_string():
    assert calc.add('1,4') == 5
    assert calc.add('21,21') == 42

def test_multiple_numbers_string():
    assert calc.add('1,2,3') == 6
    assert calc.add('100,200,300,50,10,40') == 700

def test_new_line_between_numbers_string():
    assert calc.add('1\n2,3') == 6
    assert calc.add('10\n20\n20\n10,20\n20') == 100