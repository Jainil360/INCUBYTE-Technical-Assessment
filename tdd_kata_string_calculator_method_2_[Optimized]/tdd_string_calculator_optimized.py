import re
callCount = 0
def add(numbers):
    global callCount 
    callCount += 1
    if numbers == '':
        return 0
    else:
        numbers = map(int, re.findall(r"-?\d+", numbers))
        numbers = list(filter(lambda x: x < 1000, numbers))
        negative_numbers = list(filter(lambda x: x < 0, numbers))
        if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))
        return sum(numbers)
 
def GetCalledCount():
    global callCount
    return callCount
