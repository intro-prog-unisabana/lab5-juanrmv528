def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] += valor


def calc_avg(lista):
    return sum(lista) / len(lista)


def print_normalized(lista):
    print(lista)    