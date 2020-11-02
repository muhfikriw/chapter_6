from operation import *

a = 2
b = 4
c = 6
print("a." ,a, "+", b, "x", c , "-" , b , "=", a + kali(b,c) - b )
a = 4
b = 7
c = 6
d = 9
print("b.(",a,"+",b,")x(",c,"-",d,") =", jumlah(a,b) * kurang(c,d))
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print("c.(",a,"+",b,")/(",c,"+",d,")/(",e,"+",f,") = " , jumlah(a,b) / jumlah(c,d) / jumlah(e,f))