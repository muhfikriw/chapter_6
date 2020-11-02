#starFormation1(n)
n = int(input("berapa deret? = "))
def starFormation1(n):
    for i in range(1,n+1):
        print("* "*i)
print("deret 1")
starFormation1(n)

#starFormation2(n)
def starFormation2(n):
    for i in range(n,0,-1):
        print("* "*i)
print("deret 2")
starFormation2(n)

#gabungan
def starFormation3(n):
    for i in range(1,n+1):
        print("* "*i)
    for i in range(n-1,0,-1):
        print("* "*i)
print("deret gabungan")
starFormation3(n)

