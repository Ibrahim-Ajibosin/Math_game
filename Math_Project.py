
################## Math Game #########################
######################################################

from myfunctions import generate_question, get_user_point, updateUserPoints

try:
    name = input("Enter your username")

    score = int(get_user_point(name))

    newUser = True if score == -1 else False
        
    if newUser == True :
      score = 0

    userChoice = 0

    while userChoice != "-1" :

        userscore = generate_question()
        score = userscore
        user_input = input("Enter -1 to end the game or 0 to continue")
        userChoice = user_input

    ####### Update the userScores.txt file ##########

    updateUserPoints(newUser,name,score)

except:
    print("Try running the game again, an error has occurred")