import random
import time

def printText(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.045)
    print()

def Battle():
    playerHealth = 100
    print("Player health:", playerHealth)
    print()
    print("What would you like to do?")
    attackChoice = input("attack, run, item")
    damage = random.randint(1, 20)
    if input == attack:
        print(damage)
    
    

print("RPG")

# User chooses name
printText("Hey there! You must be new around here.")
name = input("What is your name? >> ")
print("Nice to meet you", name)

#Story Dialogue
printText("My name is Bob")
printText("Welcome to the item mine! You can look around and find items like swords and gold.")
printText("Go ahead and look around for some items. To move, enter n, s, e, w.")
printText("Press l to look around.")
printText("You can only can carry 3 items in your inventory so be careful of what you choose.")
print()
print()

items = ["a staff, " , "gold, ", "a sword, ", "a potion, ", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"]

inventory = []

#Loops 3 times
x = 0
while x < 3:

    #
    foundItem = random.choice(items)
    movement = input("Choose a direcetion >> ")
    
    if movement == "l":
        print("You found", foundItem)
        addInventory = input("add this to your inventory?   y/n >> ")
        if addInventory == "y":
            printText("Adding to inventory")
            inventory.append(foundItem)
            print(inventory)
            x += 1

        if addInventory == "n":
            print("Ok")

        
    if movement == "n":
        print("Going north")
            
    if movement == "s":
        print("Going south")
        
    if movement == "e":
        print("Going east")
      
    if movement == "w":
        print("Going west")
print()
print()
printText("Bob:  Now that you have your 3 items, let's see what you got.")
printText(inventory)
printText("Wow these are all great items!")
printText("Thanks for getting them for me!")
list.clear(inventory)
printText("Bob ran off with all of your items.")
print("Your current inventory:", inventory)

printText("Hey you there!")
printText("Did Bob just steal all of your items?!?")
printText("I know a way you can get them back. Bob lives at the end of Forest Grove ")
printText("There are many creatures along the way. Here you'll need this.")
printText("Recieved iron sword.")
printText("Names Billy by the way. Come talk to me if you ever need to heal yourself from battle")
printText("Speaking of battle, how bout we have a practice one right now!")
inventory.append("iron_sword")
print("Your inventory is:", inventory)
Battle()



