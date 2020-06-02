import random
print("You are going to play guess game with the computer.\nHere the rules are as follows.\nYou guess and the computer guess.")
print("If your guess is equals to computer guess.")
print("you wins!!!!!!!!\nMaximun no of guesses allowed are 3.\nWe are starting the game.")
print("Are you ready to play with computer.............")
num = 3
print("Guess a integer number between 1 and 10 :")
while True:
    guess = int(input())
    computer = random.randint(1,10)
    print()
    print(f"you Guess: {guess}")
    print(f"computer guess: {computer} \n")
    if (1<int(guess)<11) and (int(guess)==int(computer)):
        print("\n\nYour guess is correct.\nYou win....... congratulations!!!!!")
        break
    elif num==1:
        print("\nNo guesse are left.\nYou lost the game")
        break
    else:
        print("\nYour guess is wrong.") 
        num = num -1
    print(f"\nyou are left with {num} chances.\nGuess again an integer number between 1 and 10")   