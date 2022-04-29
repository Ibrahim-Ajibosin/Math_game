from os import remove, rename

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
           my_file.write(user_Name + " " + str(score) + "\n")
           print('1 ran')
    else:
         with open("userScore.tmp", "w") as s:
            with open("user_Scores.txt", "r") as my_file:      
                for line in my_file:
                    content = line.split()
                    if user_Name == content[0] :
                        content[1] = score
                    line = content[0] + " " + str(content[1]) + '\n'
                    print(line)
                    s.write(str(line))        
         remove('user_Scores.txt')
         rename('userScore.tmp', 'user_Scores.txt')
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