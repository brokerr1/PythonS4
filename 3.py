# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
numbers = []
for i in range(20):
    numbers.append(randint(0, 10))
print('Исходный список', numbers)

new_list = []
[new_list.append(i) for i in numbers if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")