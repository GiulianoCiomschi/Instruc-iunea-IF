x=int(input(" Locul lui Radu:"))
if(x<=125):
    if(x//25==0):
        print("Radu va fi in clasa a V-a'A'")
    if(x//25==1):
        print("Radu va fi in clasa a V-a'B'")
    if(x//25==2):
        print("Radu va fi in clasa a V-a'C'") 
    if(x//25==3):
        print("Radu va fi in clasa a V-a'D'")      
    if(x//25==4):
        print("Radu va fi in clasa a V-a'E'")
else:
    print("Radu nu intra in primii 125 de elevi ")    