# Надо найти индексы элементов списка, сумма которых = целевому числу.
def two_sum(numbers, target):
    for num in numbers: #Проходимся по списку
        dec = target - num #Вычитаем элемент списка из нужного числа.
        if dec in numbers: #Если результат вычитания есть в списке, то:
            return [numbers.index(num), numbers.index(dec, numbers.index(num) + 1)] #Возвращаем индекс элемента в переменной num и индекс элемента в переменной dec. для dec начинаем поиск с индекс элемента num + 1 чтобы не нарваться в случае повторения на один и тот же элемент
            """index1 = numbers.index(num)
            print(num)
            #print(index1)
            index2 = numbers.index(dec, index1 + 1)
            print(dec)
            #print(index2)"""
            
print(two_sum([2,2,3], 4))