import numpy as np
import random
random.seed()
def guess_number(start, end, max_count, hidden_number): 
    #start, end - диапазон чисел от 1 до 100
    #max_count - максимальное количество попыток (20)
    #print("Загадайте число от {start} до {end} я попытаюсь угадать его за {max_count} попыток или меньше.")
    low = start
    high = end
    #low - минимальное значение числа
    #high - максимальное значение числа
    
    for count in range(1, max_count + 1):
        #middle - середина диапазона от low до high
        middle = int((high-low)/2)
        guess = random.randint(low, high)
        #guess - угадываемые числа
        print(f'Попытка {count}: Я думаю ваше число {guess}.')
        
        if guess == hidden_number: 
            # hidden_number - загаданное число, которое надо отгадать
            print("Ура! Я угадал число!")
            return
                 
        elif hidden_number < middle:
            print("Мое число слишком маленькое.")
            high = middle
            
        else:
            print("Мое число слишком большое.")
            low = middle
            
    print("К сожалению, я не смог угадать число за заданное количество попыток.")
hidden_number = random.randint(1, 100)
guess_number(1, 100, 20, hidden_number)                        
           
            




#import numpy as np
#import random
#random.seed()
#print(random.random)
#count = 0
#number = np.random.randint(1, 101)
#print("Загадано число от 1 до 100")
#min = 0
#max = 100
#while True:
    #predict = int(input())
    #count += 1
    #if number == predict:
        #break
    #elif number > predict:
        #min = predict
        #print(f"Угадываемое число больше {predict}")
        #print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max + min) / 2)}')
    #elif number < predict:
        #max = predict
        #print(f"Угадываемое число меньше {predict}")
        #print(f'Алгоритм бинарного поиска рекомендует вам число:{round((max+min)/2)}')


#print(f"Вы угадали число {number} за {count} попыток.")

