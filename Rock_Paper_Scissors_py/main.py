import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#declare game_images
game_images = [rock, paper, scissors]

#declare the name user_choice to store the user's input
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors. "))

#
print(game_images[user_choice])

#
computer_choice = random.randint(0, 2)
#
print("Computer chose: ")
#
print(game_images[computer_choice])

#if statement
if user_choice >= 3 or user_choice < 0:
  print("This is an invalid number, you lose!")
#
elif user_choice == 0 and computer_choice == 2:
   print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

