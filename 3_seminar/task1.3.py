#Задача 1 Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#*Пример:*

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_odd(array):
    sum  = 0 
    for i in range(1, len(array), 2):
        sum += array[i]
    return sum   

num =  list(map(int, input("Задайте последовательность чисел: ").split()))
print (f"Сумма чисел c нечетным индексом  = {sum_odd(num)}")

