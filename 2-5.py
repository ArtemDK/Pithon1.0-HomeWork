# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций
# (сложение, вычитание, умножение или деление):
# вводим первое число,
# потом операцию
# и второе число
# выводится результат
#
# Программа должна завершаться только по желанию пользователя:
# можно ввести enter и программа закончится,
# или еще операцию и еще число.
# Ну и помним, что на ноль делить нельзя.

def exit_calculate() -> int:
    close_dig = int(input('Продолжить вычисления: 1 - Yes | 2 - No \n '))
    if close_dig == 2:
        quit()


while True:
    num_1 = int(input('Число 1: '))
    num_2 = int(input('Число 2: '))
    operator = int(input('''Введите номер соответсвующий знаку операции над числами:
1 - "+"
2 - "-"
3 - "*"
4 - "/" \n '''))

    match operator:
        case 1:
            print(f'{num_1} + {num_2} = {num_1 + num_2}')
            exit_calculate()
        case 2:
            print(f'{num_1} - {num_2} = {num_1 - num_2}')
            exit_calculate()
        case 3:
            print(f'{num_1} * {num_2} = {num_1 * num_2}')
            exit_calculate()
        case 4:
            if num_2 == 0:
                print('на 0 разделить не возможно')
                exit_calculate()
            else:
                print(f'{num_1} / {num_2} = {num_1 / num_2}')
                exit_calculate()
