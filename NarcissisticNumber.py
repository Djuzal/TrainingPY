
def narcissistic( value ):
    return value == sum([int(x) ** len(str(value)) for x in str(value)]) #сравниваем число в переменой value с суммой возведённых в степень длины строки от дельных цифр числа.
