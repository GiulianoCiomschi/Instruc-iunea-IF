n1=int(input("Dati numarul gaini:"))
n2=int(input("Dati numarul boabe:"))
if n2%n1==0:
    print("Fiecare gaina a primit",n2//n1,"boabe, curcanul a primit 0 boabe",sep=" ")
elif n1%n2!=0:
    if n2%n1>n2//n1:
        print("Curcanul a primit cu",n2%n1,"boabe mai mult",sep=" ")
    if n2%n1<n2//n1:
        print("Fiecare gaina a primit cu",n2//n1,"boabe mai mult", sep=" ")
else:
    print("Numar egal de boabe")