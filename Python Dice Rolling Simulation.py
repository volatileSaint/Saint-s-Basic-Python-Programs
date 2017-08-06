import random
import time

def dieroll():
    #This is the amount of rolls you have already done. Each time you roll, this will change.
    times_rolled = 0
    dice_amount = input("\nHow many dice would you like to throw? ")
    roll_amount = input("\nHow many rolls would you like to throw? ")
    #This while loop lets keep rolling your dice until you have rolled the amount of rolls you have chosen.
    while times_rolled < int(roll_amount):
        print ("\nRolling the dice...")
        #This sleep function is for dramatic effect:
        time.sleep(2.5)
        #This code randomizes the what number you will get from the all of your dice.
        #When you input the number of dice of dice_amount, this code will provide you the new range for the amount of dice you choose.
        roll = random.randrange(int(dice_amount), int(dice_amount)*6)
        print ("\nYou rolled a {}!".format(roll))
        #This adds to the amount of rolls you have already done:
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
        #This sleep function is meant to give them time to read:
        time.sleep(2)
        #Repeats the function because the system cannot understand the previous user command.
        rollagain()

    
dieroll()

    

  
            


