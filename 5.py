ac=int(input("Dati anul curent:"))
bc=int(input("Dati luna curenta:"))
cc=int(input("Dati ziua curenta:"))
an=int(input("Dati anul nasterii:"))
bn=int(input("Dati luna nasterii:"))
cn=int(input("Dati ziua nasterii:"))
if bn>bc:
    print((ac-an)-1,"ani")
elif(bn==bc):
    if( cc==cn or cc>cn):
        print(ac-an,"ani")
    if(cc!=cn or cc<cn):
        print((ac-an)-1,"ani")
else:
    print(ac-an,"ani")