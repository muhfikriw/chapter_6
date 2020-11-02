a = int(input("sisi 1 = "))
b = int(input("sisi 2 = "))
c = int(input("sisi 3 = "))

def isPhytagoras(a,b,c):
    if((a*a) + (b*b) == (c*c)):
        print("a=",a,",b=",b,",c=",c,"  => ini pythagoras")
    else:
        print("a=",a,", b=",b,", c=",c,"=> ini bukan pythagoras")

isPhytagoras(a,b,c)