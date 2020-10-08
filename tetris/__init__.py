from copy import deepcopy
from random import choice, randint

FIELD_EMPTY_SYMBOL = '.'
FIGURE_CURRENT_SYMBOL = '#'
FIGURE_OTHER_SYMBOL = '#'
FIGURES = ['I', 'T', 'O', 'S', 'Z', 'L', 'J']

WIDTH = 10
HEIGHT = 20

event = {
    'new_figure': True,
    'end': False,
    'dead-line': 0,
}

parameter_figure = {

    'current_shape_figure': '',
    'current_shape_rotation': 1,
    'current_num_color': ''
}

colors_dict = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'pur': 35,
    'skyblue': 36,
}
colors_list = ['red', 'blue', 'green', 'yellow', 'pur', 'skyblue']


def _create_field(width=8, height=13):
    """Создать поле в соответсвии с развмерами"""

    field = [[FIELD_EMPTY_SYMBOL for _ in range(width)] for _ in range(height)]
    return field


def _create_figure(figure_body):
    """Создание фигуры в зависимомти от ее тела"""
    figures = {
        'I': [[0, 0], [1, 0], [2, 0]],
        'T': [[0, 0], [0, 1], [0, 2], [1, 1], [2, 1]],
        'O': [[0, 0], [0, 1], [1, 0], [1, 1]],
        'S': [[0, 1], [0, 2], [1, 0], [1, 1]],
        'Z': [[0, 0], [0, 1], [1, 1], [1, 2]],
        'L': [[0, 0], [1, 0], [2, 0], [2, 1]],
        'J': [[0, 1], [1, 1], [2, 0], [2, 1]],
    }

    figure = figures[figure_body]

    random_shift = randint(0, WIDTH - 3)

    for i in range(len(figure)):
        figure[i][1] += random_shift

    return figure


def _move_right(current_figure, other_figure):
    """Смещение фигуры в право"""
    displaced_figure = []

    for i in current_figure:

        if i[1] >= WIDTH - 1:
            return current_figure

        point = [i[0], i[1] + 1]
        if point in other_figure:
            return current_figure

        displaced_figure.append(point)

    return displaced_figure


def _move_left(current_figure, other_figure):
    """Смещение фигуры в лево"""
    displaced_figure = []

    for i in current_figure:

        if i[1] <= 0:
            return current_figure

        point = [i[0], i[1] - 1]
        if point in other_figure:
            return current_figure

        displaced_figure.append(point)

    return displaced_figure


def _move_bottom(current_figure, other_figure):
    """Смещение фигуры в низ"""

    displaced_figure = []

    for i in current_figure:

        if i[0] == HEIGHT - 1:
            event['new_figure'] = True
            return current_figure

        point = [i[0] + 1, i[1]]

        if point in other_figure:
            event['new_figure'] = True
            return current_figure

        displaced_figure.append(point)

    return displaced_figure


def _figure_falling(current_figure, other_figure):
    displaced_figure = []

    for i in current_figure:

        if i[0] == HEIGHT - 1:
            event['new_figure'] = True
            return current_figure

        point = [i[0] + 1, i[1]]

        if point in other_figure:
            event['new_figure'] = True
            return current_figure

        displaced_figure.append(point)

    return displaced_figure


def _figure_flip(current_figure, other_figure):
    # Копия текущей фигуры, которую будут переварачивать
    rotated_figure = deepcopy(current_figure)

    if parameter_figure['current_shape_figure'] == 'I':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] += 1

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] -= 1

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] += 1

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][0] += 1
            rotated_figure[2][1] += 1

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] += 1

            rotated_figure[2][0] += 1
            rotated_figure[2][1] -= 1

    if parameter_figure['current_shape_figure'] == 'O':
        pass

    if parameter_figure['current_shape_figure'] == 'T':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][1] += 2

            rotated_figure[1][0] += 1
            rotated_figure[1][1] += 1

            rotated_figure[2][0] += 2

            rotated_figure[4][0] -= 1
            rotated_figure[4][1] -= 1

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 2

            rotated_figure[1][0] += 1
            rotated_figure[1][1] -= 1

            rotated_figure[2][1] -= 2

            rotated_figure[4][0] -= 1
            rotated_figure[4][1] += 1

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][1] -= 2

            rotated_figure[1][0] -= 1
            rotated_figure[1][1] -= 1

            rotated_figure[2][0] -= 2

            rotated_figure[4][0] += 1
            rotated_figure[4][1] += 1

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 2

            rotated_figure[1][0] -= 1
            rotated_figure[1][1] += 1

            rotated_figure[2][1] += 2

            rotated_figure[4][0] += 1
            rotated_figure[4][1] -= 1

    if parameter_figure['current_shape_figure'] == 'S':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] += 1

            rotated_figure[1][0] += 2

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] += 1

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] -= 1

            rotated_figure[1][1] -= 2

            rotated_figure[2][0] += 1
            rotated_figure[2][1] += 1

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] -= 1

            rotated_figure[1][0] -= 2

            rotated_figure[2][0] += 1
            rotated_figure[2][1] -= 1

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] += 1

            rotated_figure[1][1] += 2

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] -= 1

    if parameter_figure['current_shape_figure'] == 'Z':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][1] += 2

            rotated_figure[1][0] += 1
            rotated_figure[1][1] += 1

            rotated_figure[3][0] += 1
            rotated_figure[3][1] -= 1

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 2

            rotated_figure[1][0] += 1
            rotated_figure[1][1] -= 1

            rotated_figure[3][0] -= 1
            rotated_figure[3][1] -= 1

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][1] -= 2

            rotated_figure[1][0] -= 1
            rotated_figure[1][1] -= 1

            rotated_figure[3][0] -= 1
            rotated_figure[3][1] += 1

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 2

            rotated_figure[1][0] -= 1
            rotated_figure[1][1] += 1

            rotated_figure[3][0] += 1
            rotated_figure[3][1] += 1

    if parameter_figure['current_shape_figure'] == 'L':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] += 1

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] -= 1

            rotated_figure[3][1] -= 2

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][0] -= 1
            rotated_figure[2][1] += 1

            rotated_figure[3][0] -= 2

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][0] += 1
            rotated_figure[2][1] += 1

            rotated_figure[3][1] += 2

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] += 1

            rotated_figure[2][0] += 1
            rotated_figure[2][1] -= 1

            rotated_figure[3][0] += 2

    if parameter_figure['current_shape_figure'] == 'J':

        if parameter_figure['current_shape_rotation'] == 1:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] += 1

            rotated_figure[2][0] -= 2

            rotated_figure[3][0] -= 1
            rotated_figure[3][1] -= 1

        if parameter_figure['current_shape_rotation'] == 2:
            rotated_figure[0][0] += 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][1] += 2

            rotated_figure[3][0] -= 1
            rotated_figure[3][1] += 1

        if parameter_figure['current_shape_rotation'] == 3:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] -= 1

            rotated_figure[2][0] += 2

            rotated_figure[3][0] += 1
            rotated_figure[3][1] += 1

        if parameter_figure['current_shape_rotation'] == 4:
            rotated_figure[0][0] -= 1
            rotated_figure[0][1] += 1

            rotated_figure[2][1] -= 2

            rotated_figure[3][0] += 1
            rotated_figure[3][1] -= 1

    for i in rotated_figure:

        if i[1] < 0 or i[1] >= WIDTH:
            return current_figure

        if i[0] >= HEIGHT - 1:
            return current_figure

        if i in other_figure:
            return current_figure

    parameter_figure['current_shape_rotation'] %= 4
    parameter_figure['current_shape_rotation'] += 1

    return rotated_figure


def _figure_control(current_figure, other_figure):
    """Управление фигурой"""
    control = input('move: ')

    if control[:1] in ['d', 'D', 'в', 'В']:
        current_figure = _move_right(current_figure, other_figure)

    if control[:1] in ['a', 'A', 'ф', 'Ф']:
        current_figure = _move_left(current_figure, other_figure)

    if control[:1] in ['s', 'S', 'в', 'В']:
        current_figure = _move_bottom(current_figure, other_figure)

    if control[:1] in ['w', 'W', 'ц', 'Ц']:
        current_figure = _figure_flip(current_figure, other_figure)

    return current_figure


def _render(field, current_figure, other_figure, color_other_figures):
    for index_i, value_i in enumerate(field):

        for index_j, value_j in enumerate(value_i):

            point = [index_i, index_j]

            if point in current_figure:
                print(f"\033[{parameter_figure['current_num_color']}m" + FIGURE_CURRENT_SYMBOL + '\033[37m', end='')


            elif point in other_figure:

                color = color_other_figures[other_figure.index(point)]

                print(f"\033[{color}m" + FIGURE_OTHER_SYMBOL + '\033[37m', end='')

            else:
                print(FIELD_EMPTY_SYMBOL, end='')
        print()


def check_horizontal_line(other_figure):
    # Хранить индексы i. В котором количество [i, j] == WIDTH-1
    delete_indexes = []

    for i in range(HEIGHT):
        count_j = 0
        for j in range(WIDTH):
            # Создать точку поля для проверки
            point = [i, j]

            # Если эта точка есть в списке точек остальных фигур, то количество += 1
            if point in other_figure:
                count_j += 1
        # Если количество j равняется ширине WIDTH. То индекс i добавим в список на удаление
        if count_j == WIDTH:
            delete_indexes.append(i)

    # Вернем этот список
    return delete_indexes


def delete_horizontal_by_index_i(indexes, other_figure, color_other_figures):
    for index in indexes:

        # Создаем точки, которые нужно удалить
        points = [[index, j] for j in range(WIDTH)]

        # Список в котором будут хранится индексы на удаление
        index_to_delete = []

        for i in range(len(other_figure)):

            # Если точка фигуры есть в точках на удаление, то добавить индекс точки фигуры в список индексов на удаление
            if other_figure[i] in points:
                index_to_delete.append(i)

        count_delete = 0
        # Удалить точку и ее цвет
        for i in sorted(index_to_delete, reverse=True):
            count_delete += 1
            del other_figure[i]
            del color_other_figures[i]


def other_figure_falling(other_figure, indexes):
    indexes = sorted(indexes)
    for index in indexes:
        event['dead-line'] += 1
        for i in range(len(other_figure)):
            # Если точки фигуры выше индекса, где была удалена строка. То опустить их на 1 точку вниз
            if other_figure[i][0] < index:
                other_figure[i][0] += 1


def run():
    field = _create_field(WIDTH, HEIGHT)
    other_figure = []
    current_figure = []
    color_other_figures = []
    indexes_delete_lines = []
    while not event['end']:
        print('Убито нилий:', event['dead-line'])

        if event['new_figure']:
            if current_figure:

                for point in current_figure:
                    other_figure.append(point)
                    color_other_figures.append(parameter_figure['current_num_color'])

            # Рандомная фигура из списка
            random_figure = choice(FIGURES)

            random_color = choice(colors_list)

            # Координаты рандомной фигуры
            current_figure = _create_figure(random_figure)

            # Тело текущей фигуры
            parameter_figure['current_shape_figure'] = random_figure
            parameter_figure['current_num_color'] = colors_dict[random_color]

            parameter_figure['current_shape_rotation'] = 1

            event['new_figure'] = False
        other_figure_falling(other_figure, indexes_delete_lines)
        _render(field, current_figure, other_figure, color_other_figures)
        current_figure = _figure_control(current_figure, other_figure)
        current_figure = _figure_falling(current_figure, other_figure)
        indexes_delete_lines = check_horizontal_line(other_figure)
        delete_horizontal_by_index_i(indexes_delete_lines, other_figure, color_other_figures)


run()
