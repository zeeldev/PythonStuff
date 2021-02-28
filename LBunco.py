import random;

NUMPLAYER = 2 # hard-coded for now
dPlayers = {} # Name:[round, roll, score] --> 'Jill':[1, 1, 0], 'Jack':[1, 2, 5]

# title of dice game
print("{:^65s}".format("WELCOME TO BUNCO"))
print("{:^65s}".format("------------------"))

print("\t")

# prompting the user
for x in range(NUMPLAYER):
    dPlayers[input("{:<40s}".format("Player", x , "please enter your name:"))] = [1,0,0] # init: round 1, roll 0, score 0    

print(dPlayers)

# randomize who will start
p1 = str(random.choices(list(dPlayers.keys()))[0])
print(p1 + (", you will go first. Good luck!"))

