n1=int(input("Dati primul nr:"))
n2=int(input("Dati al doilea nr:"))
n3=int(input("Dati al treilea nr:"))
if n1>=0 and n2>=0 and n3>=0:
    if(n2>n3):
        print(n2)
    if(n3>n2):
        print(n3)
else:
    print(n1+n2)