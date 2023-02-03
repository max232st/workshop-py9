# модуль отрисовки и взаимодействия с человеком

import pygame as pg
import time
import sys

import settings

# картики X и O глобально
x_img = None
o_img = None

def game_initiating_window(screen):
    global x_img
    global o_img

    # подгоняем изображения под нужный размер
    x_img = pg.transform.scale(pg.image.load("img/X.png"), (80, 80))
    o_img = pg.transform.scale(pg.image.load("img/0.png"), (80, 80))

    # обновление экрана
    pg.display.update()
    screen.fill(settings.bg_color)

    # рисуем вертикальные линии сетки
    pg.draw.line(screen, settings.line_color, (settings.screen_width / 3, 0), (settings.screen_width / 3, settings.screen_height), 7)
    pg.draw.line(screen, settings.line_color, (settings.screen_width / 3 * 2, 0), (settings.screen_width / 3 * 2, settings.screen_height), 7)

    # рисуем горизонтальные линии сетки
    pg.draw.line(screen, settings.line_color, (0, settings.screen_height / 3), (settings.screen_width, settings.screen_height / 3), 7)
    pg.draw.line(screen, settings.line_color, (0, settings.screen_height / 3 * 2), (settings.screen_width, settings.screen_height / 3 * 2), 7)

def draw_status(screen,message): # отрисовка строки статуса
    font = pg.font.Font(None, 30)

    # рендер текста в буфер
    # и установка свойств текста - цвет и высота букв
    text = font.render(message, 1, (255, 255, 255))

    # помещаем отрендеренный текст в окно
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(settings.screen_width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def my_question(screen,question,text1,text2): # месседж-бокс с вопросом и вариантами ответов
    font = pg.font.Font(None, 30)

    # рендер текста вопроса в буфер
    # и установка свойств текста - цвет и высота букв
    text = font.render(question, 1, (255, 255, 255))

    # помещаем отрендеренный текст вопроса в окно
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(settings.screen_width / 2, 500 - 75))
    screen.blit(text, text_rect)

    # тескт 1-ого варианта ответа
    text = font.render(text1, 1, (255, 255, 255))
    text_rect = text.get_rect(center=(settings.screen_width / 4, 500 - 30))
    screen.blit(text, text_rect)

    # тескт 2-ого варианта ответа
    text = font.render(text2, 1, (255, 255, 255))
    text_rect = text.get_rect(center=(settings.screen_width * 3 / 4, 500 - 30))
    screen.blit(text, text_rect)

    # рисуем линии - будут "кнопочки" с вариантами ответа
    pg.draw.line(screen,(255, 255, 255), [0, 400 + 40],[600, 400 + 40], 2)
    pg.draw.line(screen,(255, 255, 255), [settings.screen_width / 2, 400 + 40],[settings.screen_width / 2, 500], 2)

    pg.display.update()

    # обработка вариантов ответа и возвращение результата
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if pos[1]>400:
                    if pos[0]<(settings.screen_width / 2):
                        return 1
                    else: return 2

def PrintField(screen,local_field): # рисуем X и O на поле
                                    # просто - лепим картинки в нужные места окна
    for i in range(0,3):
        for j in range(0, 3):
            if local_field[i * 3 + j] == 'X':
                screen.blit(x_img, ((settings.screen_height / 3) * j +27, (settings.screen_width / 3) * i +27))
            if local_field[i * 3 + j] == 'O':
                screen.blit(o_img, ((settings.screen_height / 3) * j +27, (settings.screen_width / 3) * i +27))

def game_over(screen,s): # вывод результатов игры на экран
                         # просто красиво выводим текст
    font = pg.font.Font(None, 40)
    text = font.render(s, 1, (255, 255, 0))
    text_rect = text.get_rect(center=(settings.screen_width / 2, settings.screen_height / 2 ))
    screen.blit(text, text_rect)
    pg.display.update()
