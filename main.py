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
  print(f"Your Choice is :\n{rock}\n Computer Choice is :\n{rock}")
  print("you draw")
elif user_input ==1 and computer_choice==2:
  print(f"Your Choice is : \n{rock}\n Computer Choice is :\n {paper}")
  print("You Lose")
elif user_input ==1 and computer_choice==3:
  print(f"Your Choice is : \n{rock}\n Computer Choice is :\n {scissors}")
  print("You win")
elif user_input ==2 and computer_choice==1:
  print(f"Your Choice is : \n{paper}\n Computer Choice is :\n {rock}")
  print("You win")
elif user_input ==2 and computer_choice==2:
  print(f"Your Choice is : \n{paper}\n Computer Choice is :\n {paper}")
  print("You draw")
elif user_input ==2 and computer_choice==3:
  print(f"Your Choice is : \n{paper}\n Computer Choice is :\n {scissors}")
  print("You lose")
elif user_input ==3 and computer_choice==1:
  print(f"Your Choice is : \n{scissors}\n Computer Choice is :\n {rock}")
  print("You lose")
elif user_input ==3 and computer_choice==2:
  print(f"Your Choice is : \n{scissors}\n Computer Choice is :\n {paper}")
  print("You Win")
elif user_input ==3 and computer_choice==3:
  print(f"Your Choice is : \n{scissors}\n Computer Choice is :\n {scissors}")
  print("Its a draw game")

print("Game over !!")
print("Designed and created by : the diaspora boy")