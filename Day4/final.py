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


image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print(f"You choose: {image[user_choice]}")
print(f"Computer choose: {image[computer_choice]}")
if(user_choice<0) or (user_choice>2):
    print("You enter unvalid choice")
elif(user_choice==0 and computer_choice==2):
    print("You win!")
elif(computer_choice==0 and user_choice==2):
    print("You lose!")
elif(computer_choice<user_choice):
    print("You win!")
elif(computer_choice>user_choice):
    print("You lose!")
elif(user_choice==computer_choice):
    print("A draw!")