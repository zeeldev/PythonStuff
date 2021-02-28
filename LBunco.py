import random;

NUMPLAYER = 2 # hard-coded for now
dPlayers = {} # Name:[round, roll, score] --> 'Jill':[1, 1, 0], 'Jack':[1, 2, 5]

def roll_dice(player, round):
    print("Round", gameround)
    print("----------------------------------------------")

    l_dice_result = []
    roll = input("{:<40s}".format(str(p1) + " Press R to roll"))
    if str(roll).upper() == 'R':
      dice1 = random.randint(1, 6) 
      l_dice_result.append(dice1)
      dice2 = random.randint(1, 6)
      l_dice_result.append(dice2)
      dice3 = random.randint(1, 6)
      l_dice_result.append(dice3)
      print("\t")
      print(str(p1), "rolled a", "["+ str(dice1).strip() +"]"+"["+ str(dice2) + "]"+"[" + str(dice3) +"]")
      #print(l_dice_result)
      #return l_dice_result;
      score = l_dice_result.count(round)
      return (player, round, score)    

# title of dice game
print("{:^65s}".format("WELCOME TO BUNCO"))
print("{:^65s}".format("------------------"))

print("\t")

# prompting the user
for x in range(NUMPLAYER):
    dPlayers[input("{:<40s}".format("Player", x , "please enter your name:"))] = [1,0,0] # init: round 1, roll 0, score 0    

print(dPlayers)

gameround = 1;

# randomize who will start
p1 = str(random.choices(list(dPlayers.keys()))[0])
print(p1 + (", you will go first. Good luck!"))

tup_result = roll_dice(p1, gameround) # call the function
print(tup_result)

if tup_result[2] > 0:
    score = tup_result[2]
    round = tup_result[1]
    print("score", score, "round", round)
    dPlayers[tup_result[0]][2] = score #update the score
    dPlayers[tup_result[0]][1] = round #update the round
    print(dPlayers[tup_result[0]])
    tup_result_2 = roll_dice(p1, gameround)
else:
    print("\nyou failed to roll a", gameround,("!"))
    print("End of ROUND", gameround, "for", (p1)+("."))






