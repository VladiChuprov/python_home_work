#Задача 1. Напишите программу, которая принимает на вход вещественное 
#или целое число и показывает сумму его цифр. Через строку нельзя решать.
#*Пример:*
# 6782 -> 23
# 0,56 -> 11

def sum_numbers(num):
    sum=0
    while num**2 != int(num)**2 :
        num = num * 10
    while num > 0:
        lot = num % 10
        sum = sum + lot 
        num = num // 10    
    return sum 

try:
    x = float(input('Введите число  '))
    print (f"Сумма цифр числа {str(x)} = {int(sum_numbers(x))}")
except:
    print ("Введите число")
