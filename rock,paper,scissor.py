import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
 
user_choice=int(input("what do you choose ?? TYPE 0 FOR ROCK, TYPE 1 FOR PAPER ,TYPE 2 FOR SCISSORS"))
computer_choice= random.randint(0,2)
print(f"computer choice {computer_choice}")
if user_choice==0:
    print(rock)
elif user_choice==1:
    print(paper)
else:
    print(scissors)
 
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)
    
if user_choice==0 and computer_choice==2:
    print("you win!!")
elif user_choice==2 and computer_choice==0:
    print("you lose")
elif user_choice>computer_choice:
    print("you win!!")    
elif computer_choice>user_choice:
    print ("you lose!!")
elif computer_choice==user_choice:
    print("draw!!")  
else:
    print('try again dude with valid number')      
