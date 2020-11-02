def fac(n):
    hasil = 1
    for n in range(2, n + 1):
        hasil *= n
    return hasil

#permutasi
x = int(input("nilai kombinasi 1 = "))
y = int(input("nilai kombinasi 2 = "))

def combine(x,y):
    c = x - y
    hasil = fac(x)//(fac(c)*fac(y))
    return hasil

print(combine(x,y))


a = int(input("nilai permutasi 1 = "))
b = int(input("nilai permutasi 2 = "))

def permut(a,b):
    c = a - b
    hasil = fac(a)//fac(c)
    return hasil

print(permut(a,b))