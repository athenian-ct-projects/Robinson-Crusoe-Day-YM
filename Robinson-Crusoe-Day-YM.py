print("Robinson Crusoe Oregon Trail-type game \nby YM '23")

print("""
Rules: There can be any number of players, but you will all be playing as a single character. 
You should work together and use logic to live on and escape the island.

Even though you should collaborate in order to keep your character alive, all players must rotate 
turns making the decision. The person who has the turn makes the final decision.

However, if the character dies as a result of your decision, you are kicked out of the game. 
The character will "respawn" and the remaining players will continue with the game, but you are not allowed to help them.
""")

#Functions
 
import time

def turncounter(j):
  while (j>=0 and j<=5):
    j = j+1
    time.sleep(20)
    print("Turn"+" " +str(j)) 
    break

def turnlimit(x):
  for x in range (1,5):
    print("Begin!")
    x = x+1
    time.sleep(20)
    print("You're getting the hang of this!")
    x = x+1
    time.sleep(20)
    print("You're halfway there!")
    x = x+1
    time.sleep(20)
    print("Almost at the finish!")
    x = x+1
    time.sleep(20)
    print("Congratulations! You have finished this game!")
    x = x+1
    break


def next1():
    sheltermat = input("Now it's time to build a shelter, the island you are on is very stormy and windy. You have two options for materials, stone or wood. \nWhich one will you build your shelter with?: ")
    stonewood(sheltermat)
 
    
def stonewood(sheltermat):
  if sheltermat == "stone" or sheltermat == "Stone":
    print("Great! It took a lot of time and energy, but you built a sturdy shelter for your time on this island.")
    escape = input("You're nearly out of supplies on the island, and you think it's time to escape. However, there are sharks circling the island. \nDo you want to leave the island?(yes/no) ")
    if escape == "yes" or escape == "Yes":
      yesno2(escape)
    elif escape == "no" or escape == "No":
      yesno2(escape)
    else: 
      print("Please choose yes or no")
      stonewood(sheltermat)
      yesno2(escape)
    
  elif sheltermat== "wood" or sheltermat == "Wood":
    print("Oh no! Your shelter was very unstable, and collapsed during a storm. The wood fell on you and killed you! Next person's turn")
    next2()
  else:
    print("error, please choose wood or stone(not case-sensitive)")
    time.sleep(2)
    next2()

def forest1():
  print("While looking in the forest for food, you run into a bear")
  forest1death = input("Do you run away?(yes/no): ")
  if forest1death == "yes" or forest1death == "Yes":
    print("Oh no! The bear caught up to you, and killed you! You've been knocked out of the game")
    time.sleep(3)
    next1()
  elif forest1death == "no" or forest1death == "No":
    print("You lived! Bears have terrible eyesight, so it didn't notice you,")
    def redblueberry():
      berrychoice = input("But you still have to get food, and you found two berry bushes, one red and one blue, which color berry will you harvest?:")
      if berrychoice == "Blue" or berrychoice == "blue":
        print("Oh no! The blue berry was poisonous, and you died! You've been knocked out of the game")
        time.sleep(3)
        next1()
      elif berrychoice == "red" or berrychoice == "Red":
        print("Red isn't always bad, the berries turned out to be a great source of energy and nutrition for you")
        next1()
      else:
        print("error, please choose red or blue")
  redblueberry()


def yesnofirst(yesno1):
  if yesno1 == "yes" or yesno1 == "Yes":
    forest1()
  elif yesno1 == "no" or yesno1== "No":
    time.sleep(3)
    next1()
  else:
    print("error, please choose yes or no")
    yesnofirst()


def yesno2(escape):
  if escape == "Yes" or escape == "yes":
    cutboat= input("While building your escape raft, you cut yourself pretty bad, are you sure you want to keep going?: ")
    if cutboat == "yes" or cutboat == "Yes":
      print("Oh no! The sharks picked up on the scent of your blood from the cut, and they killed you! Game over!")
    elif cutboat == "no" or cutboat == "No":
      print("Congrats! You played it safe and it paid off. A sailor found you on the island, and rescued you! You have completed the game!")
      print("The input for escaping is going to come up again, ignore it, you can leave now, thank you for playing!")
  elif escape == "No" or escape == "no":
    print("Congrats! Your patience paid off. A sailor found you on the island, and rescued you! You have completed the game!")

turncounter(0)
turnlimit(1)
 




