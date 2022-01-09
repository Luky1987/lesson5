#imports

import graphics as gr
import tkinter as tk
import time


def main():
    x, y = 600, 450
    width, height = 600, 450

    global window
    window = gr.GraphWin('My House', 1000, 600)

    open_window_for_house(x, y, width, height)



def open_window_for_house(x, y, width, height):
    """
    Функция заполняющая пространство вокруг дома,
    для визуальных эффектов
    """
    #Окно для размещения домика



    #Покраска травы и неба
    color_street = gr.Rectangle(gr.Point(1000,600), gr.Point(0, 350))
    color_street.setFill('Green')
    color_street.draw(window)
    color_oxygen = gr.Rectangle(gr.Point(0,0), gr.Point(1000, 350))
    color_oxygen.setFill('Blue')
    color_oxygen.draw(window)

    #Добавление светила
    color_sun = gr.Circle(gr.Point(900,80),50)
    color_sun.setFill('Yellow')
    color_sun.draw(window)

    draw_house(x, y, width, height)
    time.sleep(3)


def draw_house_foundation(x, y, width, height):
    """
    Функция рисующая основание домика, основание выполнено серым цветом
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    load_house_fondation = gr.Rectangle(gr.Point(x - width/2, y - height/2),
                           gr.Point(x + width/2, y + height/2))
    load_house_fondation.setFill('Grey')
    load_house_fondation.draw(window)



def draw_house_walls(x, y, width, height):
    """
    Функция рисующая стены домика
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """

    load_house_wall = gr.Rectangle(gr.Point(x - width/2, y - height/2),
                                   gr.Point(x + width/2, y + height/2))
    load_house_wall.setFill('Brown')
    load_house_wall.draw(window)



def draw_house_roof(x, y, width, height):
    """
    Функция рисующая крышу домика
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    load_house_roof = gr.Polygon(gr.Point(x, height),
            gr.Point(x - width / 2, y),gr.Point(x + width / 2, y))
    load_house_roof.setFill('Orange')
    load_house_roof.draw(window)


def ufo():
    """
    Функция добавляет НЛО на небо
    :return: None
    """
    ship_alien = gr.Oval(gr.Point(100,100),gr.Point(250,125))
    ship_alien.setFill('Red')
    ship_alien.setOutline('Green')
    ship_alien.setWidth(5)
    ship_alien.draw(window)
    #ship_alien.move(900,100)


def draw_house(x,y,width,height):
    """
    Функция рисующая домик шириной width, высотой height, с опорной точкой в центре
    нижней точки фундамента x, y.
    :param x: координата x середины домика
    :param y: координата y низа домика
    :param width: полная ширина домика (фундамента или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    Ничего не возвращаем
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y*0.725, walls_width, walls_height)
    draw_house_roof(x, y*1.025 - foundation_height - walls_height, width, roof_height*0.8)
    ufo()


main()



