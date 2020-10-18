n1=int(input("Dati bile albe mari:"))
b1=int(input("Dati bile albe mici:"))
n2=int(input("Dati bile rosii mari:"))
b2=int(input("Dati bile rosii mici:"))
n3=int(input("Dati bile verzi mari:"))
b3=int(input("Dati bile verzi mici:"))
tn=n1+n2+n3
tb=b1+b2+b3
print("Numarul total de bile este",tn+tb,sep=" ")
if tn>tb:
    print("Mai multe sunt bile mari:",tn,sep=" ")
elif tn==tb:
    print("Numarul bilelor mari si mici este egal")
else:
    print("Mai multe sunt bile mici:",tb,sep=" ")
if (n1+b1>n2+b2)and(n1+b1>n3+b3):
    print("Bile albe:", n1+b1, sep=" ")
elif (n2+b2>n3+b3)and(n2+b2>n1+b1):
    print("Bile rosii:", n2+b2, sep=" ")    
elif (n3+b3>n2+b2)and(n3+b3>n1+b1):
    print("Bile verzi:", n3+b3, sep=" ")
elif (n1+b1==n2+b2)and(n1+b1>n3+b3):
    print("Bile albe si rosii:", n1+b1, sep=" ")
elif (n1+b1==n3+b3)and(n1+b1>n2+b2):
    print("Bile albe si verzi:", n1+b1, sep=" ")
elif (n3+b3>n2+b2)and(n3+b3>n1+b1):
    print("Bile rosii si verzi:", n3+b3, sep=" ")
elif (n3+b3==n2+b2)and(n3+b3==n1+b1):
    print("Bile rosii, albe si verzi:", n1+b1, sep=" ")