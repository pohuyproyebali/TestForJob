def first_func(int_massive: list):
    """ Уникальный целочисленный массив """
    for i in int_massive:
        if not isinstance(i, int):
            return print("Введите коректные данные")
    unic_massive = list(set(int_massive))
    return unic_massive


def second_func(my_min: int, my_max: int):
    """ Диапазон от min до max """
    return [i for i in range(my_min, my_max + 1)]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_other_point(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def program_for_sort(list_to_sort: list):
    """ Сортировка по возрастанию, а затем по убыванию """
    sorted_list = sorted(list_to_sort, key=lambda x: len(str(x)))
    return print(sorted_list, '\n', sorted_list[::-1])


program_for_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'fsd', 'fsdfsdfsd', 'sdfsdfsdfsdf'])