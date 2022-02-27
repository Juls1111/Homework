import random

a = random.randint(1, 10)
print(a)
b = int(input(" Введите число от 1 до 10: "))
while True:
    if b == a:
        print("Вы угадали!")
        break
    elif b < a:
        print("Загаданное число больше!")
        b = int(input(" Введите число от 1 до 10: "))
    else:
        print("Загаданное число меньше!")
        b = int(input(" Введите число от 1 до 10: "))
