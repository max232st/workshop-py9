# Контроллер программы - вся логика тут

import sys
import pygame as pg

import settings
import model
import botAI
import view

def user_click(): # Определяем, куда тыкнул мышкой пользователь (в какую клетку поля)
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get column of mouse click (1-3)
    if (x < settings.screen_width / 3):
        col = 1
    elif (x < settings.screen_width / 3 * 2):
        col = 2
    elif (x < settings.screen_width):
        col = 3
    else:
        col = 0
    # get row of mouse click (1-3)
    if (y < settings.screen_height / 3):
        row = 0
    elif (y < settings.screen_height / 3 * 2):
        row = 1
    elif (y < settings.screen_height):
        row = 2
    else:
        row = -1
    if (col == 0) and (row == -1): # непопал
        return 0
    else: return row * 3 + col

def check_click(inp): # определям, свободна ли клетка, в которую ткнули
    return True if inp in model.field else False

def run(): # основной цикл
    pg.init()

    screen = pg.display.set_mode((settings.screen_width, settings.screen_height + 100), 0, 32) # размер окна
    pg.display.set_caption('Tic Tac Toe GAME')
    CLOCK = pg.time.Clock()

    while True: # Цикл на игры
        view.game_initiating_window(screen)
        game_result = 'None'
        model.init()

        # Вопросник с настройкми игры
        x_turn = True if view.my_question(screen,'Кто ходит первым?','Х','0') == 1 else False
        bot_play_X = True if view.my_question(screen,'За кого играет БОТ?','Х','0') == 1 else False
        bot_algorithm = 2 if view.my_question(screen,'Как круто играет БОТ?','Слабо','Сильно') == 1 else 3

        view.draw_status(screen, 'Ходят X') if x_turn else view.draw_status(screen, 'Ходят 0')
        pg.display.update()
        ok_click = True
        my_input = '0'
        while game_result == 'None':
            if (x_turn ^ bot_play_X): # определяем, что надо ждать клика от человека, или пропускаем цикл,
                                      # когда ходит бот
                ok_click = False
                while True:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                        elif event.type == pg.MOUSEBUTTONDOWN:
                            my_input = str(user_click())
                            ok_click = check_click(my_input)
                            break
                    if ok_click: break

            if x_turn:
                view.draw_status(screen, 'Ходят X')
                if bot_play_X:
                    model.field = model.field.replace(botAI.get_bot_turn(model.field, 'X', bot_algorithm), 'X')  # бот сходил за X
                else:
                    model.field = model.field.replace(my_input, 'X')  # чел сходил за X
            else:
                view.draw_status(screen, 'Ходят 0')
                if not bot_play_X:
                    model.field = model.field.replace(botAI.get_bot_turn(model.field, 'O', bot_algorithm), 'O')  # бот сходил за O
                else:
                    model.field = model.field.replace(my_input, 'O')  # чел сходил за O

            view.PrintField(screen,model.field)  # отрисовка X и O на игровом поле

            x_turn = not x_turn
            view.draw_status(screen, 'Ходят X') if x_turn else view.draw_status(screen, 'Ходят 0')

            game_result = botAI.MyCheckGame(model.field)  # проверяем, чего там с результатом игры
            pg.display.update()
            CLOCK.tick(settings.fps)

        view.game_over(screen,game_result)

        if view.my_question(screen,'Будем еще играть?','Да','Нет') == 2: break
