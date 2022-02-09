
from datastore import *
import random #used in: roll_dice(), 
sided_dice = "What sided dice are you rolling? " #used in: roll_dice()
number_of_dice = "How many dice are you rolling? " #used in: 

### Let the game begin ###

def main():
  #Define and call in console
  number = get_dice_input(sided_dice)
  roll = roll_dice(number)
  collect(roll) #datastore.py
  


#Rolling what kind of dice?
def get_dice_input(sided_dice):
  dice_roll = input(sided_dice)

  #Confirm it's numeric
  while not dice_roll.isnumeric():
    dice_roll = input("Please enter a number and greater than 0. \n\n") 
    #To do: confirm value > 0

  return int(dice_roll)


#Roll the random dice
def roll_dice(number):
  roll = random.randrange(1, number+1)
  print("You roll " + str(roll) + " of a d" + str(number))
  return roll #<int>

main()



'''Testing'''
#roll(sided_dice)
#getInput(sided_dice)
#print("Quality Check - Value: " + str(number))
#print("Type: " + str(type(number))) #should be "int"
#print("Your roll " + str(random.randrange(1, number)))
#number = get_dice_input(sided_dice) #print(type(number)) #should be <int>
#roll_dice(number)
#answer() #function from datastore.py test
#GIT Test