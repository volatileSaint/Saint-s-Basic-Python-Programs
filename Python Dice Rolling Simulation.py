import random
import time

def dieroll():
    times_rolled = 0
    die_amount = input("\nHow many dice would you like to throw? ")
    roll_amount = input("\nHow many rolls would you like to throw? ")
    while times_rolled < int(roll_amount):
        print ("\nRolling the dice...")
        time.sleep(2.5)
        #This sleep function is for dramatic effect.
        roll = random.randrange(int(die_amount), int(die_amount)*6)
        print ("\nYou rolled a {}!".format(roll))
        times_rolled += 1
    rollagain()

def rollagain():
    print("\nWould you like to roll again?\n")
    print ("1.) Yes")
    print ("2.) No")
    roll_again = input()
    if roll_again == "1":
        dieroll()
    elif roll_again == "2":
        exit()
    else:
        print ("\nI cannot understand that, unfortunately.")
        time.sleep(2)
        #This sleep function is meant to give them time to read.
        rollagain()

    
dieroll()

    

  
            


