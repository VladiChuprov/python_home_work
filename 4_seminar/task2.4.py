num =  list(map(int, input("Задайте последовательность чисел: ").split()))
array = []

for i in num:
    if i not in array:
        array.append(i)
print(f"Исходная последовательнность без повторов  {array}")