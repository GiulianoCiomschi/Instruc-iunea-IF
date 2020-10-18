n1=int(input("Dati primul nr:"))
n2=int(input("Dati al doilea nr:"))
if n1%2==0 and n2%2==0:
    if(n1>n2):
        print(n1)
    if(n2>n1):
        print(n2)
if n1%2!=0 and n2%2==0:
    print(n2)
if n1%2==0 and n2%2!=0:
    print(n1)
else:
    print("nu exista numar par")