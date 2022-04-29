
################## Math Game #########################
######################################################

from myfunctions import generate_question, get_user_point, updateUserPoints


name = input("Enter your username")

if not name.isalpha():
    print("Your last name cant be a digit")
else:
    user_point = int(get_user_point(name))

    if user_point == -1 :
        newUser = True
    else :
        newUser = False

    if newUser == True :
        user_point = 0
        
    userChoice = 0
    while userChoice != "-1":
        user_point += generate_question()
        user_input = input("Enter -1 to end the game or 0 to continue ")
        userChoice = user_input

    ####### Update the userScores.txt file ##########
    updateUserPoints(newUser,name,str(user_point))
