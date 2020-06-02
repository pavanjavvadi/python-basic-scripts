import sys
user1 = input("Enter your Name:")
user2 = input("Enter your Name:")
us1option = input(f"{user1}--What do you want to choose rock, paper or scissors:")
us2option = input(f"{user2}--What do you want to choose rock, paper or scissors:")
def compare(u1,u2):
    if u1 == u2:
        return("it's a tie.")
    elif u1 =="rock":
        if u2 =="scissors":
            return(user1,"wins")
        else:
            return(user2,"wins")
    elif u1 == "paper":
        if u2 == "rock":
            return(user1,"wins")
        else:
            return(user2,"wins")
    elif u1 == "scissors":
        if u2 == "paper":
            return(user1,"wins")
        else:
            return(user2,"wins")
    else:
        return("Invalid input!you have not entered rock,paperor scissors,try again.")
        sys.exit()
print(compare(us1option,us2option))        