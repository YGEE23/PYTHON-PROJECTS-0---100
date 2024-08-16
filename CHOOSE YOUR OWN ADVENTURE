name = input("Type your name: ")
print ("welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can either go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk aroumd it or swim accross. type walk to walk aroumd and swim to swim accross: ")

    if answer == "swim":
        print("You swim accross and were eaten by an aligator")
    
    elif answer =="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You loose.")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobly, do you want to cross or head back (cross/back)? ")

    if answer == "back":
        print("You go back and loose.")
    elif answer == "cross":
        answer = input ("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("you talk to the stranger and they give you gold. You WIN! ")
        elif answer == "no":
            print("You ignore the stranger and they are offended. you LOOSE")

        else:
            print("NOt a bac option but you lose.")


else:
    print("Not a valid option. You loose.")

print("Thank you for trying", name)