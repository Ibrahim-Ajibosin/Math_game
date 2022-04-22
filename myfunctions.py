

####### Getting user point ##########
def get_user_point(userName):
 user_list = []
 score_list = []
 with open("user_Scores.txt", "r") as f: 
    for line in f:
       content = line.split()
       user_list.append(content[0])
       score_list.append(content[1])
    for name,user_score in zip(user_list,score_list):
     if userName == name:
        return user_score
    else:
        return "-1"   

######## Updating user points #############
def updateUserPoints(newUser,user_Name,score):
    if newUser == True:
        with open("user_Scores.txt", "a") as my_file:
           my_file.write(user_Name + " " + str(score) + "\n")
           print('1 ran')
    else:
         details = []
         with open("user_Score.tmp", "w") as my_file:
            with open("user_Scores.txt", "r") as s:      
                for line in s:
                    #content = line.split()
                    if user_Name == line[0]:
                        line[1] = score
                    details.append(line)
                for item in details:
                 my_file.write(str(item) + " ")        
            print(details)
            print('2 ran') 
                       

################### Generating the question ###################
def generate_question():
    import random
    operandList  = [0,4,7,9,6]
    operatorList = [" ", "tea", "cup", "man"]
    operatorDict = {1 : "+", 2: "-", 3: "**", 4: "*"}

    ############ Updating the operandList with random numbers between the range 1-9 ############
    for i in range(0,len(operandList)):
     operandList[i] = random.randint(1, 9)
    print("operand list : " + str(operandList))

    ###### Updating the operatorList by using randint() on the operatorDict to generate random operators ######
    for z in range(0,len(operatorList)):
     operatorList[z] = operatorDict[random.randint(1,4)]
    count = operatorList.count("**")

    ######## keeping the first occurence of "**" and replacing the subsequent ones with an empty string ########
    wanted_index = [a for a,b in enumerate(operatorList) if b == "**"]
    if len(wanted_index) > 1 :
     for j in range(1, len(wanted_index)):
        operatorList[wanted_index[j]] = "+"
    print(count)
    print (operatorList)

    ############## Generating the mathematical expression ##############
    from itertools import zip_longest
    question_string = ""
    for operand, operator in zip_longest(operandList,operatorList,fillvalue=""):
     question_string += str(operand) + operator
    result = eval(question_string)
    print(result)

    ################# Interacting with the user by showing the user the question #################
    user_question = question_string.replace("**", "^")
    print(user_question)

    try :
    ######### Prompt the user for an answer to the question #########
        user_input = int(input("Type your answer"))
        if user_input == result :
            print("Good work ")
            return 1
        else:
            print("Try again")
            return 0
    except:
        print("Enter an interger")