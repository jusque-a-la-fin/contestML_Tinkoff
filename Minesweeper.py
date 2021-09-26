# для случайного расположения бомб
import random
# для очищения консоли
import os


# Печать игрового поля
def print_playing_field(string_field_values, size):
    print()
    print("\t\t\t\tСАПЁР\n")

    el = "   "
    for i in range(size):
        el = el + "     " + str(i + 1)
    print(el)

    for row in range(size):
        el = "     "
        if row == 0:
            for column in range(size):
                el = el + "______"
            print(el)

        el = "     "
        for column in range(size):
            el = el + "|     "
        print(el + "|")

        el = "  " + str(row + 1) + "  "
        for column in range(size):
            el = el + "|  " + str(string_field_values[row][column]) + "  "
        print(el + "|")

        el = "     "
        for col in range(size):
            el = el + "|_____"
        print(el + '|')

    print()


# Функция, устанавливающая бомбы
def lay_bombs(int_field_values, number_of_bombs, size):
    # счетчик установленных бомб
    counter = 0
    while counter < number_of_bombs:

        # генерация случайной позиции ячейки
        value = random.randint(0, size * size - 1)

        # получение столбца и строки из позиции
        row = value // size
        column = value % size

        # Установить бомбу в эту ячейку, если последняя свободна
        if int_field_values[row][column] != -1:
            counter = counter + 1
            int_field_values[row][column] = -1


# Функция, устанавливающая в ячейку без бомбы число,
# которое показывает, сколько бомб находится вокруг
# данной ячейки
def place_number_of_bombs(values, size):
    # Цикл по ячейкам поля
    for row in range(size):
        for column in range(size):

            # Пропускаем заминированную ячейку
            if values[row][column] == -1:
                continue

            # Проверяем верхнюю ячейку на наличие бомбы
            if row > 0 and values[row - 1][column] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем нижнюю ячейку на наличие бомбы
            if row < size - 1 and values[row + 1][column] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем левую ячейку на наличие бомбы
            if column > 0 and values[row][column - 1] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем правую ячейку на наличие бомбы
            if column < size - 1 and values[row][column + 1] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем верхнюю левую ячейку на наличие бомбы
            if row > 0 and column > 0 and values[row - 1][column - 1] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем верхнюю правую ячейку на наличие бомбы
            if row > 0 and column < size - 1 and values[row - 1][column + 1] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем нижнюю левую ячейку на наличие бомбы
            if row < size - 1 and column > 0 and values[row + 1][column - 1] == -1:
                values[row][column] = values[row][column] + 1

            # Проверяем нижнюю правую ячейку на наличие бомбы
            if row < size - 1 and column < size - 1 and values[row + 1][column + 1] == -1:
                values[row][column] = values[row][column] + 1


# Рекурсивная функция, ищущая все нулевые ячейки,
# соседние с нулевой ячейкой, которую выбрал игрок
def find_zero_valued_cells(row, column, string_field_values, int_field_values, visited, size):
    # Если ячейка не посещена
    if [row, column] not in visited:

        # Отметить ячейку посещенной
        visited.append([row, column])

        # Если ячейка содержит ноль
        if int_field_values[row][column] == 0:

            # Запоминаем её
            string_field_values[row][column] = int_field_values[row][column]

            # рекурсивные вызовы по соседним ячейкам
            if row > 0:
                find_zero_valued_cells(row - 1, column, string_field_values, int_field_values, visited, size)
            if row < size - 1:
                find_zero_valued_cells(row + 1, column, string_field_values, int_field_values, visited, size)
            if column > 0:
                find_zero_valued_cells(row, column - 1, string_field_values, int_field_values, visited, size)
            if column < size - 1:
                find_zero_valued_cells(row, column + 1, string_field_values, int_field_values, visited, size)
            if row > 0 and column > 0:
                find_zero_valued_cells(row - 1, column - 1, string_field_values, int_field_values, visited, size)
            if row > 0 and column < size - 1:
                find_zero_valued_cells(row - 1, column + 1, string_field_values, int_field_values, visited, size)
            if row < size - 1 and column > 0:
                find_zero_valued_cells(row + 1, column - 1, string_field_values, int_field_values, visited, size)
            if row < size - 1 and column < size - 1:
                find_zero_valued_cells(row + 1, column + 1, string_field_values, int_field_values, visited, size)

        # Если ячейка не содержит ноль
        if int_field_values[row][column] != 0:
            string_field_values[row][column] = int_field_values[row][column]


# Функция, очищающая консоль
def clear_console():
    os.system("clear")


# Функция, выводящая главное меню
def display_main_menu():
    print("\t\t\tМеню:")
    print("1. Новая игра")
    print("2. Сохраненные игры")
    print("3. Выход")
    print("Выберите, что хотите сделать")
    print("Нажмите соответсвующую цифру, например 1 или 2 или 3: ", end='')


# Функция, определяющая, нужно ли завершить игру
def check_finish(string_field_values, size, number_of_bombs):
    # счетчик непустых ячеек
    count = 0

    # Цикл по всем ячейкам
    for row in range(size):
        for column in range(size):

            # если ячейка содержит флаг или непустая
            if string_field_values[row][column] != ' ' and string_field_values[row][column] != 'F':
                count = count + 1

    # если открыты все ячейки без бомб
    if count == size * size - number_of_bombs:
        return True
    else:
        return False


# Функция, устанавливающая значки бомб в игровом поле
def show_bombs(string_field_values, int_field_values, n):
    for row in range(n):
        for column in range(n):
            if int_field_values[row][column] == -1:
                string_field_values[row][column] = '*'


# Функция, обрабатывающая ввод пользователя для игры
def play(saved_size, saved_string_field_values, saved_number_of_bombs, new_game=True):
    print("\n\t\t\tИнструкция:")
    print("1. Введите координаты ячейки: Например, \"1 2 Open\"")
    print("2. Чтобы поставить флаг в ячейку, наберите её координаты: Например, \"1 2 Flag\"")

    # Если новая игра запускается
    if new_game == True:

        print("\nВыберите размер поля. Введите только одно натуральное число, например 5: ", end='')

        # Ввод размера игрового поля
        size = int(input())

        # Проверки на корректность размера
        if size == 0:
            print("Извините, размер поля не может быть равен 0")
        if size < 0:
            print("Извините, размер поля не может быть отрицательным")

        # Ввод количества бомб
        print("Выберите количество бомб. Введите только одно число, например 5: ", end='')
        number_of_bombs = int(input())

        # Проверки на корректность количества бомб
        if number_of_bombs > size ** 2:
            print("Ошибка! Количество бомб больше количества ячеек")
        elif number_of_bombs < 0:
            print("Ошибка! Количество бомб не может быть отрицательным числом")

    # если запускается сохраненная игра
    else:
        size = saved_size
        number_of_bombs = saved_number_of_bombs

    # Значения ячеек в целочисленном формате
    int_field_values = [[0 for y in range(size)] for x in range(size)]

    # Значения ячеек в строковом формате
    if new_game == True:
        string_field_values = [[' ' for y in range(size)] for x in range(size)]
    else:
        string_field_values = saved_string_field_values

    # Ячейки, которые содержат флаг
    flags = []

    # Устанваливаем бомбы
    lay_bombs(int_field_values, number_of_bombs, size)

    # устанавливаем значения ячеек, которые не содержат бомбы
    place_number_of_bombs(int_field_values, size)

    # Переменная, приводящая к выходу из цикла
    finish = False

    # переменная, детектирующая первую итерацию цикла
    # позволяет предлагать после каждого хода
    # покинуть/сохранить игру или нет
    firstIteration = False

    # Цикл, управляющий игрой
    while not finish:

        if firstIteration == False:
            print_playing_field(string_field_values, size)
        else:
            print_playing_field(string_field_values, size)

            # Если выходим из игры
            print("Желаете покинуть партию?")
            print("Нажмите 1, если да. Нажмите любую другую клавишу, если нет")
            choice = input()
            if choice == '1':
                print("Желаете сохранить эту игру ?")
                print("Нажмите 1, если да. Нажмите любую другую клавишу, если нет")
                choice = input()
                if choice == '1':
                    print('Введите название сохраняемой игры, например: "игра1" ')
                    name = input()
                    return string_field_values, size, number_of_bombs, name
                else:
                    return -1

        firstIteration = True

        # Пользовательский ввод
        input_from_user = input("Введите координаты ячейки, например \"1 2 Open\" или \"1 2 Flag\" ").split()

        # Проверка ввода, открывающего ячейку
        if len(input_from_user) == 3 and input_from_user[2] == "Open":

            # Блокировка неправильного ввода
            try:
                values_from_user = list(map(int, input_from_user[:2]))
            except ValueError:
                clear_console()
                print("Неправильный ввод!")
                display_main_menu()
                continue

        # Проверка ввода, устанавливающего в ячейке флаг
        elif len(input_from_user) == 3:
            if input_from_user[2] != 'Flag':
                clear_console()
                print("Неправильный ввод!")
                display_main_menu()
                continue

            # Блокировка неправильного ввода
            try:
                values_from_user = list(map(int, input_from_user[:2]))
            except ValueError:
                # Очищаем консоль
                clear_console()
                print("Неправильный ввод!")
                display_main_menu()
                continue

            # Проверка на корректность вводимых чисел
            if values_from_user[0] > size or values_from_user[0] < 1 or \
                    values_from_user[1] > size or values_from_user[1] < 1:
                # Очищаем консоль
                clear_console()
                print("Неправильный ввод!")
                display_main_menu()
                continue

            # Получаем индексы столбцов и строк
            row = values_from_user[0] - 1
            column = values_from_user[1] - 1

            # Если ячейка уже содрежит флаг
            if [row, column] in flags:
                # Очищаем консоль
                clear_console()
                print("\nФлаг уже установлен")
                continue

            # Если ячейка уже открыта и пользователь пытается её открыть ещё раз
            if string_field_values[row][column] != ' ':
                # Очищаем консоль
                clear_console()
                print("Число в ячейке уже известно")
                continue

            # Оповещение об установке флага
            if len(flags) < number_of_bombs:
                # Очищаем консоль
                clear_console()
                print("\nФлаг установлен")

                # Добавляем новый флаг
                flags.append([row, column])

                # Устанавливаем значок флага на игровом поле
                string_field_values[row][column] = 'F'
                continue

            # В противном случае флаг поставить нельзя
            else:
                # Очищаем консоль
                clear_console()
                print("Флаг поставить нельзя")
                continue

        else:
            clear_console()
            print("\nНеправильный ввод!")
            display_main_menu()
            continue

        # Проверка на корректность вводимых чисел
        if values_from_user[0] > size or values_from_user[0] < 1 or \
                values_from_user[1] > size or values_from_user[1] < 1:
            clear_console()
            print("\nНеправильный ввод!")
            display_main_menu()
            continue

        # Получаем индексы столбцов и строк
        row = values_from_user[0] - 1
        column = values_from_user[1] - 1

        # Удалить флаг из ячейки, если она уже содержит флаг
        if [row, column] in flags:
            flags.remove([row, column])

        # Если наступили на бомбу, игра заканчивается
        if int_field_values[row][column] == -1:
            string_field_values[row][column] = '*'
            show_bombs(string_field_values, int_field_values, size)
            print_playing_field(string_field_values, size)
            print("Поражение!!")
            print("Желаете сохранить эту партию ?")
            print("Нажмите 1, если да. Нажмите любую другую клавишу, если нет")
            choice = input()
            if choice == '1':
                print('Введите название сохраняемой партии, например: "игра1" ')
                name = input()
                saved_string_field_values = string_field_values
                saved_size = size
                return saved_string_field_values, size, number_of_bombs, name
            else:
                return -1

            finish = True
            continue

        # Если открыли ячейку, которая соседствует с нулевыми ячейками
        elif int_field_values[row][column] == 0:
            vis = []
            string_field_values[row][column] = '0'
            find_zero_valued_cells(row, column, string_field_values, int_field_values, vis, size)

        # Если открыли ячейку, которая соседствует с ячейками, которые содержат хотя бы 1 бомбу
        else:
            string_field_values[row][column] = int_field_values[row][column]

        # Проверяем, завершилась ли игра
        if (check_finish(string_field_values, size, number_of_bombs)):
            show_bombs(string_field_values, int_field_values, size)
            print_playing_field(string_field_values, size)
            print("Победа!!")
            print("Желаете сохранить эту партию ?")
            print("Нажмите 1, если да. Нажмите любую другую клавишу, если нет")
            choice = input()
            if choice == '1':
                print('Введите название сохраняемой партии, например: "игра1" ')
                name = input()
                saved_string_field_values = string_field_values
                saved_size = size
                return saved_string_field_values, size, number_of_bombs, name
            else:
                return -1

            finish = True
            continue
        clear_console()


# Функция, управляющая сохраненными играми
def saved_games(saved_string_field_values, saved_size, saved_number_of_bombs, saved_names):
    # если нет сохраненных игр
    if (len(saved_names) == 0):
        print("\nВы не сохранили ни одной игры\n")
        return -1

    print("\tВы сохранили следующие игры")
    for i in range(len(saved_names)):
        print("{}. {}".format(i + 1, saved_names[i]))
    print("\nВыберите, какую игру хотите продолжить")
    print("Нажмите соответсвующую цифру, например 1 или 2 или 3: ", end='')
    choice = int(input())

    # пока пользователь не введет корректные данные
    while (choice not in range(1, len(saved_names) + 1)):
        print(range(len(saved_names)))
        print("Вы нажали неверный номер!!")
        print("Попробуйте еще раз")
        choice = int(input())

    # значения ячеек сохраненной игры строкового формата
    saved_string_field_values1 = saved_string_field_values

    # размер поля сохраненной игры
    saved_size1 = saved_size

    # количество бомб сохраненной игры
    saved_number_of_bombs1 = saved_number_of_bombs

    # названия сохраненных игр
    saved_names1 = saved_names

    # цикл, управляющий сохраненными играми
    while True:
        action = play(saved_size[choice - 1], saved_string_field_values[choice - 1], saved_number_of_bombs[choice - 1],
                      False)
        # игра не сохраняется
        if action == -1:
            return -1
        # Игра сохраняется
        else:
            # показать главное меню
            display_main_menu()

            # получить выбор действия из главного меню
            step = int(input())
            if step == 1:

                # запустить игру
                action = play(saved_size, saved_string_field_values, saved_number_of_bombs)

                # если пользователь решил не сохранять игру
                if action == -1:
                    return -1

                # если пользователь решил сохранить игру
                else:
                    # получить данные сохраненной игры

                    m_v, n, s_m_n, name = action
                    saved_string_field_values1.append(m_v)
                    saved_size1.append(n)
                    saved_number_of_bombs1.append(s_m_n)
                    saved_names1.append(name)

            # если пользователь решил сохранить игру
            if step == 2:

                # получить данные сохраненной игры
                m_v, n, s_m_n, name = action
                saved_string_field_values1.append(m_v)
                saved_size1.append(n)
                saved_number_of_bombs1.append(s_m_n)
                saved_names1.append(name)

                # запустить сохраненную игру
                action1 = saved_games(saved_string_field_values1, saved_size1, saved_number_of_bombs1, saved_names1)
                # если пользователь решил не сохранять игру
                if action1 == - 1:
                    return -1

            if step == 3:
                break


# Главная функция
def main():
    # выбор пункта главного меню
    step = 0

    # значения ячеек сохраненной игры строкового формата
    saved_string_field_values = []

    # размер поля сохраненной игры
    saved_size = []

    # количество бомб сохраненной игры
    saved_number_of_bombs = []

    # названия сохраненных игр
    saved_names = []

    # цикл, управляющий главным меню
    while True:

        # показать главное меню
        display_main_menu()

        # получить выбор действия из главного меню
        step = int(input())

        # начать новую игру
        if step == 1:
            # запустить игру
            action = play(saved_size, saved_string_field_values, saved_number_of_bombs)

            # если игра не сохранена
            if action == -1:
                continue

            # игру решили сохранить
            else:
                # получить данные сохраненной игры
                m_v, n, s_m_n, name = action
                saved_string_field_values.append(m_v)
                saved_size.append(n)
                saved_number_of_bombs.append(s_m_n)
                saved_names.append(name)

        # запустить сохраненную игру
        if step == 2:
            # запустить сохраненную игру
            action1 = saved_games(saved_string_field_values, saved_size, saved_number_of_bombs, saved_names)

            # если зашли в сохраненную игру и поиграв, решили выйти
            if action1 == -1:
                continue

        # выйти из игры
        if step == 3:
            break


# Вызов главной функции
main()
