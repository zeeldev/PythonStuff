"""
Create a Box Office app...

"""
#--------- setup ---------------------
# list 
# [(movie title, gross in Millions $)]
box_list = [('It',60.00)
    ,('Home Again', 5.3)
    ,('American Assassin', 14.8)
    ,('Mother!',7.5)
    ,('Home Alone', 65.3)
]

idxl = 10 #left justify
idxr = 10
idxc = 40
#--------- end of setup ---------------

#function to return the 2nd element Gross Earnings
def takeGrossEarnings(e):
    return e[1]

#call the function and sort reversed (descending based on gross earnings)
box_list.sort(key=takeGrossEarnings, reverse=True)

# debug
#print(box_list)

# print the output
print("RANK".ljust(idxl), "TITLE".ljust(idxc), "GROSS".rjust(idxr))
for i in range(len(box_list)):
    print(str(i + 1).ljust(idxl), str(box_list[i][0]).ljust(idxc), str(box_list[i][1]).rjust(idxr))
    """
    output...
    RANK       TITLE                                         GROSS
    1          It                                             60.0
    2          American Assassin                              14.8
    3          Mother!                                         7.5
    4          Home Again                                      5.3 
    """
