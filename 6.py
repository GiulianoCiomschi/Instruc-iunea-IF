n1=int(input("Dati prima nota:"))
n2=int(input("Dati a doua nota:"))
n3=int(input("Dati a treia nota:"))
if n3>8:
    print(n1,n2,n3,sep=" ")
if n3<8:
    if n1>n2:
        print(n1)
    if n2>n1:
        print(n2)    