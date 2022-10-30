array = [[] for _ in range(10)]


def create_hash_table(array):
    for i in range(len(array)):
        print(i+1, end=" ")
        for j in array[i]:
            print(j, end=" ")
        print()


def get_hash(arg):
    return arg % len(array)


def insert(array, arg, val):
    hash = get_hash(arg)
    array[hash].append(val)


if __name__ == '__main__':
    insert(array, 7, 'стол')
    insert(array, 9, 'машина')
    insert(array, 3, 'дом')
    insert(array, 1, 'кровать')
    insert(array, 6, 'солнце')
    insert(array, 5, 'дверь')
    insert(array, 21, 'КОЛЛИЗИЯ')
    create_hash_table(array)
