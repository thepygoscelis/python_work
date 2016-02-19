#Author Charlie R. Hicks

#Mission 3 cannibals and 3 missionaries must cross a river together
#They only have 1 boat which can hold two individuals at a time.
#If at any time you have more cannibals than missionaries on either side
#you loose the game.
#When you get all missionaries and cannibals to the other side you win

#Challenge build the game with only functions
def game():
    print("The goal is simple. \nIf at any point the number of missionaries is less than the number of cannibals on any side you loose. \nBoth groups must make it the right side to win. \n")
    win = play(3,3,0,0,1)
    if win == 1:
        print("You won and that makes you mighty.")
    else:
        print("Curse your sudden ,but invitable betreyal.")
def play(lm,lc,rm,rc,boat):
    print("Cannibals on the right side " + str(rc) +". \n")
    print ("Missionaries on the right side " + str(rm) + ".\n")
    print ("Cannibals on the left side " + str(lc) + ". \n")
    print("Missionaries on the left side " + str(lm) + ". \n")
    if boat == 1:
        print("Boat on  the left side. \n")
    elif boat == 2:
        print("Boat on the right side. \n")
    totalCannibals, totalMissionaries = 3,3
    if rm == 3 and rc == 3:
        return 1
    elif (rm<rc and rm > 0) or (lm<lc and lm > 0):
        return 0
    elif boat == 1:
        while totalCannibals+totalMissionaries > 2 or totalCannibals > lc or totalMissionaries > lm:
            if lc > 0:
               totalCannibals = int(input("How many Cannibals should move from the left side? (0-2) "))
            else:
               totalCannibals = 0
            if lm > 0:
               totalMissionaries = int(input("How many Missionaries should move from the left side? (0- 2) "))
            else:
               totalMissionaries = 0
        return play(lm-totalMissionaries,lc-totalCannibals,rm+totalMissionaries,rc+totalCannibals,2)
    elif boat == 2: 
        while totalCannibals+totalMissionaries > 2 or totalCannibals > rc or totalMissionaries > rm:
            if rc > 0:
               totalCannibals = int(input("How many Cannibals should move from the right side? (1 or 2) "))
            else:
               totalCannibals = 0
            if rm > 0:
               totalMissionaries = int(input ("How many Missionaries should move from the right side? (1 or 2) "))
            else:
               totalMissionaries = 0
        return play(lm+totalMissionaries,lc+totalCannibals,rm-totalMissionaries,rc-totalCannibals,1)       
        
game()
