import random;

NUMPLAYER = 2 # hard-coded for now
MAXROUND = 2 # hard-coded for now
dPlayers = {} # Name:[round, roll, score] --> 'Jill':[1, 1, 0], 'Jack':[1, 2, 5]


def roll_dice(player):
    l_dice_result = []
    roll = input("{:<40s}".format(str(player) + " Press R to roll"))
    if str(roll).upper() == 'R':
        dice1 = random.randint(1, 6) 
        l_dice_result.append(dice1)
        dice2 = random.randint(1, 6)
        l_dice_result.append(dice2)
        dice3 = random.randint(1, 6)
        l_dice_result.append(dice3)
        #print(l_dice_result)
        return l_dice_result;

"""
def roll_dice2(player, round):
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
"""


# title of dice game
print("{:^65s}".format("WELCOME TO BUNCO"))
print("{:^65s}".format("------------------"))

print("\t")

# prompting the user
for x in range(NUMPLAYER):
    dPlayers[input("{:<40s}".format("Player", x , "please enter your name:"))] = [0,0,0] # init: round 0, roll 0, score 0    

print(dPlayers)

gameround = 1;

# randomize who will start
p1 = str(random.choices(list(dPlayers.keys()))[0])
print(p1 + (", you will go first. Good luck!"))


# PSUEDO-CODE
# while round <= MAXROUND: 
#     then keep playing same round
#     player 1 starts
#       while player 1 has die result == round:
#           keep playing
#           (increase score of player 1's round)
#       else: 
#           end game round for player 1
#           (increase count of player 1's round)
#           start game for player 2
#           while player 2 has die result == round:
#               keep playing (player 2)
#           else:
#               end game round for player 2
#               increase round
#                   

round = 1;
for k in dPlayers.keys(): # works for 2 players for now
    if k != p1: p2 = k

while round <= MAXROUND:
    print("*** round ***", round)
    tup_result = roll_dice(p1) # call the function
    print(tup_result)
    print("\t")
    print(str(p1), "rolled a", "["+ str(tup_result[0]).strip() +"]"+"["+ str(tup_result[1]) + "]"+"[" + str(tup_result[2]) +"]")
    print("dPlayers ==>", dPlayers)
    score = tup_result.count(round)
    print("p1 score", score)
    if score > 0: # a score!
        dPlayers[p1][2] = dPlayers[p1][2] + score #update the score
        print("dPlayers ==>", dPlayers)
    else:
        #update round of P1
        dPlayers[p1][0] =  dPlayers[p1][0] + 1   
        print("end of round for p1")
        print("debug 1 ...dPlayers ==>", dPlayers)
        #
        # now start of P2
        # keep looping while p2's round <> p1's round
        while dPlayers[p2][0] != dPlayers[p1][0]:
            tup_result2 = roll_dice(p2)
            print("\t")
            print(str(p2), "rolled a", "["+ str(tup_result2[0]).strip() +"]"+"["+ str(tup_result2[1]) + "]"+"[" + str(tup_result2[2]) +"]")
            score = tup_result2.count(round)
            print("p2 score", score)
            if score > 0: # a score!
                dPlayers[p2][2] = dPlayers[p2][2] + score #update the score
                print("2nd dPlayers ==>", dPlayers)
            else:
                dPlayers[p2][0] =  dPlayers[p2][0] + 1 # update p2's round   
                # increase the round
                print("end of round", round)
                round = round + 1
# end of while loop

# tie-breaker round...
#check...
if dPlayers[p1][2] == dPlayers[p2][2]:
    print("IT's a TIE!!!!")
    # continue tie breaker round here...


        









"""
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
"""





