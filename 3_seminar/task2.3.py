# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]


list_num = list(map(int, input("Задайте последовательность чисел: ").split()))
i = 0
print(list_num)
while i < len(list_num)/2:
    result = list_num[i] * list_num[len(list_num)-1-i]
    i += 1
    print(result, end=' ')