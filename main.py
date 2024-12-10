import random

x = random.randint(1, 100)
print("Добро пожаловать в игру Числовая угадайка!")
print("Загадайте любое целое число от 1 до 100")

def is_valid(n):
    if n > 100 or n < 1:
        return False
    return True

def right_answer(n):
    if n == x:
        return False
    return True

def more_or_less(n):
    if n > x:
        return False
    if n < x :
        return True

def continuation(n):
    if n.lower() == "да":
        return 0
    if n.lower() == "нет":
        return 1

count = 0

while True:
    n = int(input())

    if is_valid(n) == False:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue

    count += 1

    if more_or_less(n) == False:
        print("Загаданное число меньше!")
        continue
    elif more_or_less(n) == True:
        print("Загаданное число больше!")
        continue

    if right_answer(n) == False:
        print("Вы угадали число! Поздравляем! Ваше число попыток: ", count)
        print("Начать игру заново? ДА/НЕТ:")

    s = input()

    if s.lower() != 'да' and s.lower() != 'нет':
        while s.lower() != 'да' and s.lower() != 'нет':
            print("Я вас не понимаю. ДА/НЕТ?")
            s = input()


    if s.lower() == 'да':
        x = random.randint(1, 100)
        count = 0
        print("Загадайте любое целое число от 1 до 100")
        continue
    elif s.lower() == 'нет':
        print("Спасибо за игру! До новых встреч!")
        break










