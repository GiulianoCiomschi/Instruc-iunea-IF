x=int(input(" Ionel este pe locul:"))
if(x <= 100):
    if (x%4==0):
        print ("Ionel va primi tricoul negru")
    if (x%4==1):
        print("Ionel va primi tricoul alb")
    if (x%4==2):
        print("Ionel va primi tricoul roșu")
    if (x%4==3):
        print("Ionel va primi tricoul albastru")
else:
    print("Ionel nu este in primii 100")