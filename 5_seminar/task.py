print('Программа для игры с конфетами человек против человека.')

from random import randint

def makeMove(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, quantity):
    print(f"{name}, взял(а) {k}, теперь их {counter}. Осталось на столе {quantity} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
quantity = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) #  # возвращаем случайное целочисленное значение между 0 и 2 и присваиваем его булевой переменной (флаг или поднят, или опущен)
print('Жеребьевка из 0 и 2 выдала :', flag)
if flag:
    print(f"Первым ходит игрок {player1}")
else:
    print(f"Первым ходит игрок {player2}")

counter1 = 0 
counter2 = 0

while quantity > 28:
    if flag:
        k = makeMove(player1)
        counter1 += k
        quantity -= k
        flag = False
        p_print(player1, k, counter1, quantity)
    else:
        k = makeMove(player2)
        counter2 += k
        quantity -= k
        flag = True
        p_print(player2, k, counter2, quantity)

if flag:
    print(f"Поздравляю {player1}, вы выиграли!")
else:
    print(f"Поздравляю {player2}, вы выиграли!")

print('Программа для игры с конфетами человек против бота.')

from random import randint

def makeMove(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, quantity):
    print(f"{name}, взял(а) {k}, теперь их {counter}. Осталось на столе {quantity} конфет.")

player1 = input("Введите ваше имя: ")
player2 = "Bot"
quantity = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # возвращаем случайное целочисленное значение между 0 и 2 и присваиваем его булевой переменной (флаг или поднят, или опущен)
print('Жеребьевка из 0 и 2 выдала :', flag)
if flag:
    print(f"Первым ходит игрок {player1}")
else:
    print(f"Первым ходит игрок {player2}")

counter1 = 0 
counter2 = 0

while quantity > 28:
    if flag:
        k = makeMove(player1)
        counter1 += k
        quantity -= k
        flag = False
        p_print(player1, k, counter1, quantity)
    else:
        k = randint(1,29)
        counter2 += k
        quantity -= k
        flag = True
        p_print(player2, k, counter2, quantity)

if flag:
    print(f"Поздравляю {player1}, вы победили бота!")
else:
    print(f"Выиграл {player2}")