n1=int(input("Dati n1:"))
p1=int(input("punctaj:"))
n2=int(input("Dati n2:"))
p2=int(input("punctaj:"))
n3=int(input("Dati n3:"))
p3=int(input("punctaj:"))
if p1>p2 and p1>p3: 
    print("punctaj maxim are",n1,sep=" ")
if p2>p1 and p2>p3: 
    print("punctaj maxim are",n2,sep=" ")    
if p3>p2 and p3>p1: 
    print("punctaj maxim are",n3,sep=" ")
if(p1==p2)and(p1>p3)and(p2>p3):
    print("punctaj maxim au",n1,n2,sep=" ")    
if(p1==p3)and(p1>p2)and(p3>p2):
    print("punctaj maxim au",n1,n3,sep=" ")   
if(p3==p2)and(p3>p1)and(p2>p1):
    print("punctaj maxim au",n3,n2,sep=" ")    
if((p1==p2)and(p2==p3)and(p1==p3)):
    print("punctaj maxim au toti")       