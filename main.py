import random

## List of characters
alpha = ['a','b','c','d','e','f','g','h','i','j']

## Number of players and player names
players = 0
player1 = ""
player2 = ""
player3 = ""
player4 = ""

## Taking players name as input
while True:
    print("Player name or to end x: ", end="")

    if(players == 0):
        player1 = input()
        if(player1 == "x"):
            exit()
        if(player1 == ""):
            print("There must be at least one player!")
        else:
            players += 1
    elif(players == 1):
        player2 = input()
        if(player2 == "x"):
            exit()
        if(player2 == ""):
            break;
        elif(player2 == player1):
            print(""+player2+" is already is player list")
        else:
            players += 1
    elif(players == 2):
        player3 = input()
        if(player3 == "x"):
            exit()
        if(player3 == ""):
            break;
        elif(player3 == player1 or player3 == player2):
            print(""+player3+" is already is player list")
        else:
            players += 1
    elif(players == 3):
        player4 = input()
        if(player4 == "x"):
            exit()
        if(player4 == ""):
            break;
        elif(player4 == player3 or player4 == player2 or player4 == player1):
            print(""+player4+" is already is player list")
        else:
            players += 1
            break;

## Variable to store number of digits in the number
noOfDigits = 0

## Taking input for number of digits in number
while(noOfDigits <= 0 or noOfDigits > 4):
    print("Enter number of digits for each number in addition (1-4): ",end="")
    noOfDigits = int(input())


## Variables to store starting point and end point for random number generation
noFrom = 0
noTo = 0

## Setting values for start and end point
if(noOfDigits == 1):
    noFrom = 0
    noTo = 9
elif(noOfDigits == 2):
    noFrom = 10
    noTo = 99
elif(noOfDigits == 3):
    noFrom = 100
    noTo = 999
elif(noOfDigits == 4):
    noFrom = 1000
    noTo = 9999

## Generating to random numbers and calculating their sum
num1 = random.randint(noFrom, noTo)
num2 = random.randint(noFrom, noTo)
sumNum = num1+num2

## Shows both number and their sum for testing
print("One: ",num1,", Two: ",num2,", Sum: ",sumNum)

## Shuffles alphabet array randomlly
random.shuffle(alpha)

## Convert both randomly generated numbers and their sum into strings for easier manupulation 
strNum1 = str(num1)
strNum2 = str(num2)
strSum = str(sumNum)

## Variable to store temporary values of numbers converted in alphabets
strNum1New = ""
strNum2New = ""
strNum3New = ""
ansLen = len(strSum)

## Converts randomly generated numbers to characters
for i in range(0,2):
    for j in range(0,noOfDigits):
        if(i == 0):
            strNum1New += alpha[int(strNum1[j])]
        elif(i == 1):
            strNum2New += alpha[int(strNum2[j])]
            
for h in range(0, ansLen):
    strNum3New += alpha[int(strSum[h])]


## Variable declaration for storing scores, turn, letters and winner etc data required in the game
itr = noOfDigits*2 + ansLen
itrc = 0
letter = ""
digit = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0
turn1 = True
turn2 = False
turn3 = False
turn4 = False
tempNum1 = ""
tempNum2 = ""
tempNum3 = ""
replay = "x"
winner = player1
winnerScore = score1

## Main Game Begins
while True:

    ## Prints numbers converted into character 
    print(" ",strNum1New)
    print("+",strNum2New)
    print("--------")
    print(" ",strNum3New)
    print("--------")

    ## Determines which players turn is this
    if(turn1 == True):
        print("Player "+player1+" Current Score = ",score1)
        if(players > 1):
            turn2 = True
            turn1 = False
    elif(turn2 == True):
        print("Player "+player2+" Current Score = ",score2)
        if(players > 2):
            turn3 = True
            turn2 = False
        else:
            turn1 = True
            turn2 = False
    elif(turn3 == True):
        print("Player "+player3+" Current Score = ",score3)
        if(players > 3):
            turn4 = True
            turn3 = False
        else:
            turn1 = True
            turn3 = False
    elif(turn4 == True):
        print("Player "+player4+" Current Score = ",score4)
        turn1 = True
        turn4 = False

    ## Asks the user for letter and digit
    print("Enter a letter: ",end="")
    letter = input()
    print("Enter a digit: ",end="")
    digit = int(input())

    ## Checks for validity of letter and digit, then updates the string holding the numbers
    ## Then update players score and resets appropriate values at the end
    for i in range(0,noOfDigits):
        for j in range(0,10):
            if(alpha[j] == letter):
                if(alpha[digit] == letter):
                    for k in range(0,noOfDigits):
                        if(strNum1New[k] == letter):
                            tempNum1 += str(digit)
                            itrc += 1
                            if(turn1 == True):
                                if(players == 4):
                                    score4 += 1
                                elif(players == 3):
                                    score3 += 1
                                elif(players == 2):
                                    score2 += 1
                                elif(players == 1):
                                    score1 += 1
                            if(turn2 == True):
                                    score1 += 1
                            if(turn3 == True):
                                    score2 += 1
                            if(turn4 == True):
                                score3 += 1

                        else:
                            tempNum1 += strNum1New[k]
                        
                        if(strNum2New[k] == letter):
                            tempNum2 += str(digit)
                            itrc += 1
                            if(turn1 == True):
                                if(players == 4):
                                    score4 += 1
                                elif(players == 3):
                                    score3 += 1
                                elif(players == 2):
                                    score2 += 1
                                elif(players == 1):
                                    score1 += 1
                            if(turn2 == True):
                                score1 += 1
                            if(turn3 == True):
                                score2 += 1
                            if(turn4 == True):
                                score3 += 1
                        else:
                            tempNum2 += strNum2New[k]
                            
                    for k in range(0,ansLen):
                        if(strNum3New[k] == letter):
                            tempNum3 += str(digit)
                            itrc += 1
                            if(turn1 == True):
                                if(players == 4):
                                    score4 += 1
                                elif(players == 3):
                                    score3 += 1
                                elif(players == 2):
                                    score2 += 1
                                elif(players == 1):
                                    score1 += 1
                            if(turn2 == True):
                                score1 += 1
                            if(turn3 == True):
                                score2 += 1
                            if(turn4 == True):
                                score3 += 1
                        else:
                            tempNum3 += strNum3New[k]
                    strNum1New = tempNum1
                    strNum2New = tempNum2
                    strNum3New = tempNum3
                    tempNum1 = ""
                    tempNum2 = ""
                    tempNum3 = ""

    ## Checks if all numbers are converted from character to number for ending the game
    if(itrc == itr):
        print(" ",strNum1New)
        print("+",strNum2New)
        print("--------")
        print(" ",strNum3New)
        print("--------")

        ## Determins the winner
        winnerScore = score1
        if(score2 > score1 and score2 > score3 and score2 > score4):
            winner = player2
            winnerScore = score2
        if(score3 > score1 and score3 > score2 and score3 > score4):
            winner = player3
            winnerScore = score3
        if(score4 > score1 and score4 > score2 and score4 > score3):
            winner = player4
            winnerScore = score4

        ## Prints winner information and checks if user want to play again
        print("Player ",winner," wins this game. Updated score = ",winnerScore)
        print("Enter 0 to play again or to end x: ",end="")
        replay = input()

        ## If player wants to play again it generated new numbers and resets all the values
        ## If they don't it prints score of all the players and exit
        if(replay == str(0)):
            num1 = random.randint(noFrom, noTo)
            num2 = random.randint(noFrom, noTo)
            sumNum = num1+num2

            print("1 One: ",num1,", Two: ",num2,", Sum: ",sumNum)

            random.shuffle(alpha)

            strNum1 = str(num1)
            strNum2 = str(num2)
            strSum = str(sumNum)


            strNum1New = ""
            strNum2New = ""
            strNum3New = ""
            ansLen = len(strSum)

            for i in range(0,2):
                for j in range(0,noOfDigits):
                    if(i == 0):
                        strNum1New += alpha[int(strNum1[j])]
                    elif(i == 1):
                        strNum2New += alpha[int(strNum2[j])]
            
            for h in range(0, ansLen):
                strNum3New += alpha[int(strSum[h])]


            itr = noOfDigits*2 + ansLen
            itrc = 0
            letter = ""
            digit = 0
            score1 = 0
            score2 = 0
            score3 = 0
            score4 = 0
            turn1 = True
            turn2 = False
            turn3 = False
            turn4 = False
            tempNum1 = ""
            tempNum2 = ""
            tempNum3 = ""
            replay = "x"
            winner = player1
            winnerScore = score1
        else:
            print("",player1," ",score1)
            if(players > 1):
                print("",player2," ",score2)
            if(players > 2):
                print("",player3," ",score3)
            if(players > 3):
                print("",player4," ",score4)
            break

    
    

    




        

    
