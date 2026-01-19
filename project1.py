# # SNAKE, WATER, GUN GAME    sudharna he wrong he
# import random

# computer = random.choice([-1,0,1])
# youstr = input("enter your choice: ")
# youdict ={"s":1, "w":-1, "g": 0}
# reversedict = {1: "snake", -1: "water", 0: "gun"}

# you = youdict[youstr]

# # by now we have 2 numbers (variables), you and computer
# print(f"you chose{reversedict[you]}\ncomputer chose {reversedict[computer]}")

# if(computer == you):
#     print("its a drow")

# else:
#     if(computer==-1 and you ==1):
#         print("you win")

#     elif(compile==-1 and you ==0):
#         print("you lose")

#     elif(computer==1 and you==-1):
#         print("you lose")
        
#     elif(computer==1 and you==0):
#         print("you win")
        
#     elif(computer==0 and you==-1):
#         print("you win")
        
#     elif(computer==0 and you==1):
#         print("you lose")

#     else:
#         print("something went wrong")
        
    

    # SNAKE, WATER, GUN GAME
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s = snake, w = water, g = gun): ").lower()

youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

# input check
if youstr not in youdict:
    print("Invalid choice! Please choose s, w or g")
    exit()

you = youdict[youstr]

print(f"You choose {reversedict[you]}")
print(f"Computer choose {reversedict[computer]}")

if computer == you:
    print("It's a draw")

elif computer == -1 and you == 1:
    print("You win")

elif computer == -1 and you == 0:
    print("You loseg")

elif computer == 1 and you == -1:
    print("You lose")

elif computer == 1 and you == 0:
    print("You win")

elif computer == 0 and you == -1:
    print("You win")

elif computer == 0 and you == 1:
    print("You lose")

else:
    print("Something went wrong")
