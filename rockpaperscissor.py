import random
user_choice=int(input("enter your choice"))
if user_choice>=3 or user_choice<0:
    print("user entered a invalid number and you loose")
else:

    computer_choice=random.randint(0,2)
    print(f"computer choose {computer_choice}")
    if user_choice==computer_choice:
        print("draw")
    elif user_choice ==0 and computer_choice ==2:
        print("you win")
    elif user_choice ==2 and computer_choice==0:
        print("computer wins")
    elif user_choice>computer_choice:
        print("you win")
    elif computer_choice<user_choice:
        print("you lose")

