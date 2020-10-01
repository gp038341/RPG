import random
import time

#text animation
def printText(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.045)
    print()

#Battle system
def Battle():
    print()
    playerHealth = 100
    enemyHealth = 75
    print("Player health:", playerHealth)
    print("Enemy health:", enemyHealth)
    print()
    battling = True
    while battling:
        print("What would you like to do?")
        attackChoice = input("attack, run, item >> ")
        damage = random.randint(5, 20)
        enemyDamage = random.randint(1, 10)
        if attackChoice == "attack":
            enemyHealth = enemyHealth - damage
            print("You dealt", damage)
            print("Enemy Health:", enemyHealth)
            playerHealth = playerHealth - enemyDamage
            print("Enemy dealt:", enemyDamage)
            print("Player Health:", playerHealth)
        if enemyHealth <= 0:
            battling = False
        if playerHealth <= 0:
            print("You Lose!")
            battling = False
        if attackChoice == "run":
            gotAway = random.randint(1, 50)
            if gotAway == 1:
                print("Couldn't get away!")
            else:
                print("Got away safely")
                battling = False
        if attackChoice == "item":
            print("Opening inventory")
            print(inventory)
            item_choice = input("Which item do you want to use? >> ")
            if item_choice == "potion":
                playerHealth += 20
                print("Player Health:", playerHealth)
    

print("RPG")

# User chooses name
printText("Hey there! You must be new around here.")
name = input("What is your name? >> ")
print("Nice to meet you", name)

#Story Dialogue
printText("My name is Bob")
time.sleep(1)
printText("Welcome to the item mine! You can look around and find items like swords and gold.")
printText("Go ahead and look around for some items. To move, enter n, s, e, w.")
printText("Press l to look around.")
time.sleep(.300)
printText("You can only can carry 3 items in your inventory so be careful of what you choose.")
print()
print()

items = ["a staff, ", "gold, ", "a sword, ", "a potion, ", "nothing, ", "nothing, ", "nothing, ", "nothing, ", "nothing, ", "nothing, "]

inventory = []
gold = 0

#Loops 3 times
x = 0
while x < 3:

    #
    foundItem = random.choice(items)
    movement = input("Choose a direcetion >> ")
    
    if movement == "l":
        print("You found", foundItem)
        addInventory = input("add this to your inventory?   y / n >> ")
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

#Story
print()
print()
printText("Bob:  Now that you have your 3 items, let's see what you got.")
printText(inventory)
time.sleep(2)
printText("Wow these are all great items!")
printText("Thanks for getting them for me!")
list.clear(inventory)
time.sleep(1)
printText("Bob ran off with all of your items.")
print("Your current inventory:", inventory)

time.sleep(.500)
printText("Hey you there!")
time.sleep(2)
printText("Did Bob just steal all of your items?!?")
printText("I know a way you can get them back. Bob lives at the end of Forest Grove ")
printText("There are many enemies along the way. Here you'll need this.")
printText("Recieved iron sword.")
inventory.append("iron_sword")
print("Your inventory is:", inventory)
time.sleep(1)
printText("Names Billy by the way. Come talk to me if you ever need to heal yourself from battle")
printText("Speaking of battle, how bout we have a practice one right now!")

Battle()
printText("Great battle!")
printText("If you ever want to become a better swordsman, I can teach you and give you better swords for a price of course")
printText("You'll want to head up north next. That will lead you to Bob")
printText("Don't forget, press i to open your inventory")
player_inventory = input("What would you like to do?")
printText("i for inventory or n to go north")
if player_inventory == "i":
    print(inventory)
equipping_item = input("Would you like to equip an item? y / n >> ")
if equipping_item == "y":
    print("Equiping item")
    damage = random.randint(7, 22)




