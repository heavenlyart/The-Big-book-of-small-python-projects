import random

def condition_cheker(input:str):
    global GuessNo
    try:
        if len(input)==3:
            GuessNo = str(GuessNo)
            broadcast = 0
            if input == GuessNo:
                print("you have got the number!")
                return "stop"
            else:
                for number in range(3):
                    if input[number] == GuessNo[number]:
                        print("fermi")
                        break
                    else: broadcast = 1
                if broadcast == 1:
                    for chr in input:
                        if chr in GuessNo:
                            print("pico")
                            break
                        
        else: 
            print("it wasn't 3 numbers blud!. Exiting by default.")
            return "stop"
    except:
        print("A problem occured infor Rusty")
            

   

print("I am thinking of a 3-digit number. Try to guess what it is.")
print('''Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.''')


def game_start():
    global GuessNo
    print()
    print('''  I have thought up a number.
 You have 10 guesses to get it.''')
    GuessNo = random.randint(100,999)
    for turn in range(1, 11):
        print("Guess #",turn)
        entry = input("please enter your number: ")
        stop = condition_cheker(entry)
        if stop == "stop":
            break
    
    again = input("would you like to play again? (yes/no)")
    if again == "yes":
        game_start()
    elif again == "no":
        print("Thanku for playing the game!")
    else:
        print("Wrong input exiting by default")

game_start()
        
    



    