'''we all have placed snake, water gun game in our childhood . if you haven't , google the rules of this game and
write a python program capable of playing this game with the user.'''
import random
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you == 'g':
            return False
        elif you == 'w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = 'g'



you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(comp, you)
print(f"Computer choose {comp}")
print(f"You choose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Win!")
