#задача 1. Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.

num = int (input("Введите число  "))
i=2
num_divider =[]
while i <= num:
    if num % i ==0 :
        num_divider.append(i)
        num //= i 
    else :
        i+=1 
print (f"Список простых множителей числа  : {num_divider} ")

