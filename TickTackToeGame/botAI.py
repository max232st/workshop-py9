# Мозги для крестиков-ноликов
from random import randint

# щаг бота - в зависимости от алгоритма
def get_bot_turn(local_field: str, my_char, algorithm):
    if algorithm == 2:
        return my_random(local_field)          # случайный
    elif algorithm == 3:
        return mega_brain(local_field, my_char)  # самый умный
    else:
        return first_free(local_field)         # самый тупой


def first_free(local_field: str):  # самый тупой - выбирает первое непустое поле
    return local_field.replace('X', '').replace('O', '')[0]

def my_random(local_field: str):  # случайно выбраем незанятое поле
    local_field = local_field.replace('X', '').replace('O', '')
    return local_field[randint(0, len(local_field)-1)]

# для mega_brain

def win_triple(triple: str, my_char):  # triple - строка из 3-х символов (цифры и Х и О)
    s = triple.replace(my_char, '')  # чистим X или O - что на вход дали
    if len(s) == 1 and s.isdigit():
        return s  # если одно место с числом осталось - то это то, что нам нужно
    return ''

# поверка, можем ли мы победить одним ходом, когда играем за my_char
def i_can_win(local_field, my_char):
    win_patterns = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                    (2, 5, 8), (0, 4, 8), (2, 4, 6))  # если в этих позициях
                                                      # стоят XXX или OOO,
                                                      # то кто-то выйграл
    triples = [local_field[win_patterns[i][0]] +
               local_field[win_patterns[i][1]] +
               local_field[win_patterns[i][2]]
               for i in range(len(win_patterns))]  # список заполненных верт, гориз и диагоналей
    k = ''
    for i in range(len(triples)):  # проверка тройки символов на то, что одного из не нехватает
                                   # для полного заполнения
        k = win_triple(triples[i], my_char)
        if k:
            break
    return k

def mega_brain(local_field: str, my_char):
    # проверяем, можем ли победить одним ходом
    ret = i_can_win(local_field, my_char)
    if ret:
        return ret  # можем!

    alien_char = ('O' if my_char == 'X' else 'X')

    # проверяем, может ли враг победить одним ходом
    ret = i_can_win(local_field, alien_char)
    if ret:
        return ret  # может! - ходим туда - ему назло!

    best_move = ['5', '1', '3', '7', '9', '2',
                 '4', '6', '8']  # лучшие ходы на поле

    # выбираем из лучших ходов, которые не заняты
    return [i for i in best_move if i in local_field.replace('X', '').replace('O', '')][0]

def MyCheckGame(local_field): # функция проверки окончания игры
    win_patterns = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # если в этих позициях
                                                                                     # стоят XXX или OOO,
                                                                                     # то кто-то выйграл
    if len(local_field.replace('X','').replace('O','')) == 0: return 'Победила дружба! Ничья!'
    if 'XXX' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'XXX Победили крестики XXX'
    if 'OOO' in list(filter(lambda x: x,[local_field[win_patterns[i][0]]+\
                                         local_field[win_patterns[i][1]]+\
                                         local_field[win_patterns[i][2]] \
                                    for i in range(len(win_patterns))])):
        return 'OOO Победили нулики OOO'
    return 'None'