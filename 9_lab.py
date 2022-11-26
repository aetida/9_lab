import random
import logging

logging.basicConfig(level = logging.INFO, filename = "sample.log", format = "%(asctime)s - %(levelname)s - %(message)s")


while True: #цикл обработки ввода границ диапазона
    try:
        num = int(input("введите натуральное число больше единицы: "))
        if num <= 1:
            logging.error(f'Ошибка. Некорректный ввод')
            print('неверный ввод\nповторите попытку')
        else:
            logging.info(f'пользователь ввел границу диапазона: {num}')
            break
    except ValueError:
        logging.error(f'Ошибка. Некорректный ввод')
        print("неверный ввод\nповторите попытку")

while True: #цикл обработки ввода количества попыток
    try:
        try_num = int(input("введите количество попыток "))
        if try_num <= 0:
            logging.error(f'Ошибка. Некорректный ввод')
            print('неверный ввод\nповторите попытку')
        else:
            logging.info(f'пользователь ввел количество попыток: {try_num}')
            break
    except ValueError:
        logging.error(f'Ошибка. Некорректный ввод')
        print("неверный ввод")

#генерация числа в диапазоне от 1 до num
randnum = random.randint(1, num)
logging.info(f'сгененрировано число: {randnum}')

while try_num>0: #цикл отгдаывания числа
    try:
        guess_num = int(input("введите загаданное число "))
        assert num >= 0
        if guess_num == randnum:
            logging.info(f'пользователь угадал число')
            print("вы угадали")
            break
        else:
            try_num -= 1
            if guess_num < randnum:
                logging.info(f'пользователь ввел число меньше загаданного')
                print("загаданное число больше")
            else:
                logging.info(f'пользователь ввел число больше загаданного')
                print("загаданное число меньше")
            if try_num == 0:
                logging.info(f'пользователь не отгадал число')
                print("попытки закончились\nзагаданное число: ", randnum)
    except ValueError:
        logging.error(f'Ошибка. Некорректный ввод')
        print("некорректный ввод\nповторите попытку")
    except AssertionError:
        logging.error(f'Ошибка. Некорректный ввод')
        print('некорректный ввод\nповторите попытку')
    
logging.info(f'работа программы завершена')
