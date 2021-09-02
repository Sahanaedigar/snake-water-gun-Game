import random
def swg(comp,mine):
    if(comp==mine):
        return None
    if(comp=='s' and mine=='g'):
        return True
    elif(comp=='w' and mine=='s'):
        return True
    elif(comp=='g' and mine=='w'):
        return True
    else:
        return False
choice=('s','w','g')          # s for snake,w for water and g for gun
comp=random.randint(0,2)      # returns a number from range 0,1,2
comp=choice[comp]
mine=input('choice either s,w or g: ')
win=swg(comp,mine)
print(f"you chose {mine} and the computer chose {comp}")
if win is None:
    print("Match Drawn")
if win:
    print("you won")
else:
    print("you lose")

