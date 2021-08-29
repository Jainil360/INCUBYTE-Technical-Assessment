def add(numbers):
    if numbers == '':return 0
    else:
        numbers = map(int, numbers.split(','))
    return sum(numbers)