def add(numbers):
    if numbers == '':return 0
    else:
        numbers = numbers.replace('\n',',')
        numbers = map(int, numbers.split(','))
    return sum(numbers)