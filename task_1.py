def size_array():
    size = int(input('Введите размер массива: '))
    return size


def fill(size):
    array_ = []
    while len(array_) <= size:
        user_input = [input('Добавьте значение в массив: ')]
        if len(array_) == size:
            print('Массив заполнен. Увеличьте массив или замените значение в занятой ячейке.')
            break
        if user_input != ['stop'] and len(array_) != size:
            array_ += user_input
            print(array_)
            continue
        if user_input == ['stop']:
            print('Выход из функции добавления')
            break
    return array_


def get(array_):
    user_input = int(input('Какой элемент вывести: '))
    if user_input > len(array_) - 1:
        raise IndexError
    count = 1
    for i in array_:
        if count == user_input:
            print(i)
        count += 1


def del_without_del(new_array):
    extra_array = []
    user_input_ = int(input('По какому индексу удалить элемент: '))
    for i in range(len(new_array)):
        if i != user_input_ and user_input_ < len(new_array):
            extra_array = extra_array + [new_array[i]]
        if i == user_input_ and user_input_ < len(new_array):
            continue
        if i != user_input_ and user_input_ >= len(new_array):
            raise IndexError
    new_array = extra_array
    return new_array


def show(new_array):
    print(new_array)


def insert(new_array):
    extra_array = []
    user_input = input('Какой элемент вставить: ')
    user_input_ = int(input('На место какого индекса вставить элемент: '))
    for i in range(len(new_array)):
        if i != user_input_ and user_input_ < len(new_array):
            extra_array = extra_array + [new_array[i]]
        else:
            extra_array = extra_array + [user_input]
            extra_array = extra_array + [new_array[i]]
    new_array_ = extra_array
    return new_array_


if __name__ == '__main__':
    size = size_array()
    array_ = fill(size)
    get(array_)
    new_array = del_without_del(array_)
    show(new_array)
    new_array_ = insert(new_array)
    show(new_array_)
