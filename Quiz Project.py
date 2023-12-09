                 #python quiz game

questions = ("1:What is the launch date for chandrayaan-3 mission: ",
             "2:How many elements are in the periodic table: ",
             "3:Which animal lays tha largest eggs: ",
             "4:What is the most abundant gas in earth's atmosphere: ",
             "5:How many bones are in the human body: ",
             "6:Which planet in the solae system is the hottest: ",
             "7:How many parts are there in the indian army")
            
options =(("A. 17 july 2023","B. 12 july 2023","C. 14 july 2023","D. 15 july 2023"),
          ("A. 116","B. 117","C. 118","D. 119"),
          ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
          ("A. 206","B. 207","C. 208","D. 209"),
          ("A. Mercury","B. Venus","C. Earth","D. mars"),
          ("A.Three part","B.Six part","C.Eight part","D.Four part"))


answers =("C","C","D","A","A","D","A")


guesses =[]


score = 0


question_num = 0


for question in questions:
    
    print("-------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
        

    guess = input("Enter(A,B,C,D):").upper()


    guesses.append(guess)


    if guess == answers[question_num]:
        score += 1
        print("CORRCT!")
    else:
        score -= 1
        print("INCORRCT!")
        print(f"{answers[question_num]} : is the corrct answers")


    question_num += 1

    print("Your current score is",score)

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print("\n Total score is :",score)


