def sum(*data):
    a = 0
    for i in data:
        a += i
    print(a)


def rata(*data):
    a = 0
    b = 0
    for i in data:
        a += i
        b += 1
    rata2 = a/b
    print(rata2)


def mak(*data):
    a = data[0]
    for i in data:
        if (i > a):
            a = i
    print(a)


def min(*data):
    a = data[0]
    for i in data:
        if (i < a):
            a = i
    print(a)
