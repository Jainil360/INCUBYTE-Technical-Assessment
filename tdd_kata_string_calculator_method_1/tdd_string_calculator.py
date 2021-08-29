callCount = 0
def add(numbers):
    global callCount 
    callCount += 1
    if numbers == '':return 0
    else:
        numbers = handle_custom_delimiter(numbers)
        numbers = numbers.replace('\n',',')
        numbers = map(int, numbers.split(','))
        numbers = list(filter(lambda x: x < 1000, numbers))
        negativeNumbers = list(filter(lambda x: x < 0, numbers))
        if negativeNumbers: raise Exception('negatives not allowed ' + str(negativeNumbers))
    return sum(numbers)

def handle_custom_delimiter(numbers):
    if numbers.startswith('//'):
        delimiterDetail,numberString = numbers.split('\n',1)
        customDelimiter = delimiterDetail[2:]
        delimitersList = [char for char in customDelimiter]
        if (len(set(delimitersList)) == 1 ):
            numbers = numberString.replace(customDelimiter,',')
        else:
            for delimiter in delimitersList:
                    numberString = numberString.replace(delimiter,',') 
            numbers = numberString
    return numbers

def GetCalledCount():
    global callCount
    return callCount
