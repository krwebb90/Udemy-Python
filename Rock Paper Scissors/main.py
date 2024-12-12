def mainprogram():
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
  
  import random
  
  #assign ascii art to list
  game_images = [rock, paper, scissors]
  
  #User Decision
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  
  #Computer Decision
  computer_choice = random.randint(0,2)
  
  #Printing User Choice
  if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  else:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
  
  #Print if situations nested in the else statement above
    if user_choice == computer_choice:
      print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif user_choice == 1 and computer_choice == 0:
      print("You win!")
    elif user_choice == 2 and computer_choice == 1:
      print("You win!")
    else:
      print("You lose.")

while True:
  import time
  time.sleep(1)
  mainprogram()