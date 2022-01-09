def main():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house_foundation(x, y, width, height):
    """
    Функция рисующая основание домика
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    print('Типа рисую основание...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    """
    Функция рисующая стены домика
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """
    Функция рисующая крышу домика
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    print('Типа рисую крышу...', x, y, width, height)
    pass


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
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


main()



