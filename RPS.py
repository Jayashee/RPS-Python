import random
def rps ():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock ()
    elif computer_choice == 2:
        computer_choice_paper ()
    else:
        computer_choice_scissors ()
def try_again():
    choice = raw_input(" Would you like to play again? y/n ")
    if choice == "y" or choice == "yes" or choice == "Y":
        rps()
    elif choice == "n" or choice == "no" or choice == "N":
        print "Thanks for playing"
        quit()
    else:
        print ("Try Again")
        try_again()

def computer_choice_rock ():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print "Tie. You choose rock and the computer choose rock."
        try_again()
    elif user_choice == "2":
        print "You Win. You choose paper and the computer choose rock."
        try_again()
    elif user_choice == "3":
        print "You loose. You choose scissors and the computer choose rock."
        try_again()
    else:
        print ("Try again")

#computer_choice_rock()

def computer_choice_paper ():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print "You loose. You choose rock and the computer choose paper."
        try_again()
    if user_choice == "2":
        print "Tie. You choose paper and the computer choose paper."
        try_again()
    if user_choice == "3":
        print "You Win. You choose scissors and the computer choose paper."
        try_again()
    else:
        print ("Try again")

#computer_choice_paper()

def computer_choice_scissors ():
    user_choice = raw_input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print "You Win. You choose rock and the computer choose scissor."
        try_again()
    if user_choice == "2":
        print "You loose. You choose paper and the computer choose scissor."
        try_again()
    if user_choice == "3":
        print "Tie. You choose scissors and the computer choose scissors."
        try_again()
    else:
        print ("Try again")

computer_choice_scissors()
computer_choice_rock()
computer_choice_paper()

rps()
