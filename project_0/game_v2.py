import numpy as np
import random
random.seed()
print(random.random)
count = 0
number = np.random.randint(1, 101)
print("Загадано число от 1 до 100")
min = 0
max = 100
while True:
    predict = int(input())47
    count += 1
    if number == predict:
        break
    elif number > predict:
        min = predict
        print(f"Угадываемое число больше {predict}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
    elif number < predict:
        max = predict
        print(f"Угадываемое число меньше {predict}")
        print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max+min)/2)}')


print(f"Вы угадали число {number} за {count} попыток.")

