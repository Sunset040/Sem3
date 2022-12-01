# Sem3

# 3.10 Начало
def doConvertHex(number):
    result = ''
    hexData=(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F')
    while (number>0):
        result = str(hexData[number % 16]) + result
        number = number // 16
    return  result

# 3.10 Вывод
number = int(input("3.10) Число 0,1,2...N: "))
print(doConvertHex(number))

# 3.10 Конец
# _________________________

# 3.11 Начало
def ifStringFloat(inputValue):
    result   = ''
    isFloat  = False
    isNumber = False

    for i in inputValue:
        if i.isdigit():
            isNumber = True
        else:
            if i == ".":
                isFloat = True
            else:
                isFloat = False
                break

    if isNumber and isFloat:
        result = 'Введенное значение является дробным числом'
    else:
        result = 'Введенное значение НЕ является дробным числом'

    return result

# 3.11 Вывод
inputValue = input("3.11) Введите число: ")
print(ifStringFloat(inputValue))

# 3.11 Конец
# _________________________

# 3.12 Начало

# буква "о" русская
def isLetterExists (inputValue, letterLower = 'о', letterUpper = 'О'):
    countLetter = 0
    isExists = False

    for i in inputValue:
        if i == letterLower or i == letterUpper:
            countLetter += 1
            isExists = True
    if isExists:
        return "Количество буквы 'о' встречается " + str(countLetter) + " раз"
    else:
        return "Буква 'о' не встречается в заданном слове"

# 3.12 Вывод

inputValue = input("3.12) Введите текст: ")
print(isLetterExists(inputValue))

# 3.12 Конец
