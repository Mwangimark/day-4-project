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
user_input=int(input("Enter a number 1: rock, 2:paper ,3:scissors  :"))
computer_choice = random.randint(1,3)

if user_input ==1 and computer_choice==1:
  print("Your choice is\n" + rock+ "Computer choice is\n" + rock)
  print("you draw")
elif user_input ==1 and computer_choice==2:
  print("Your choice is\n" + rock+ "Computer choice is\n" + paper)
  print("You Lose")
elif user_input ==1 and computer_choice==3:
  print("Your choice is\n" + rock+ "Computer choice is\n" + scissors)
  print("You win")
elif user_input ==2 and computer_choice==1:
  print("Your choice is\n" + paper+ "Computer choice is\n" + rock)
  print("You win")
elif user_input ==2 and computer_choice==2:
  print("Your choice is\n" + paper+ "Computer choice is\n" + paper)
  print("You draw")
elif user_input ==2 and computer_choice==3:
  print("Your choice is\n" + paper+ "Computer choice is\n" + scissors)
  print("You lose")
elif user_input ==3 and computer_choice==1:
  print("Your choice is\n" + scissors+ "Computer choice is\n" + rock)
  print("You lose")
elif user_input ==3 and computer_choice==2:
  print("Your choice is\n" + scissors+ "Computer choice is\n" + paper)
  print("You Win")
elif user_input ==3 and computer_choice==3:
  print("Your choice is\n" + scissors+ "Computer choice is\n" + scissors)
  print("Its a draw game")
else:
  print("Err!!Please input a number from 1-3")

print("Game over !!")
print("Designed and created by : the diaspora boy")