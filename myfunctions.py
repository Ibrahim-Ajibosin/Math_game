

####### Getting user point ##########

def get_user_point(userName):
 user_list = []
 score_list = []
 with open("user_Scores.txt", "r") as f: 
    for line in f:
       content = line.split()
       user_list.append(content[0])
       score_list.append(content[1])
    for x,y in zip(user_list,score_list):
     if userName == x:
        return y
    else:
        return "-1"   


######## Updating user points #############

def updateUserPoints(newUser,user_Name,score):
    if newUser == True:
        with open("user_Scores.txt", "a") as my_file:
           my_file.write("\n" + user_Name + " " + str(score) + "\n")
           print('1 ran')
    else:
         details = []
         with open("user_Scores.tmp", "w") as my_file:
            with open("user_Scores.txt", "r") as s:      
                for line in s:
                    content = line.split()
                    if user_Name == content[0]:
                        content[1] = score
                    details.append(content)
            my_file.write(str(details) + "\n")        
            print(details)
            print('2 ran') 
                       
