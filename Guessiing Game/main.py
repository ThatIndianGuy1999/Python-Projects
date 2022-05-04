from art import logo
from random import randint

easy_difficulty = 10
Medium_diffuculty = 5
Hard_difficulty = 3
choice = int(input("Choose The Difficulty : 1. Easy 2. Medium 3. Hard"))
def start(guess,answer) :
  if guess > answer :
    print("Too high try a lower  number")
  elif guess < answer :
    print("Too low try a higher number")
    return -1
  else :
    print(f"Right The Correct answer was {answer}")
def difficulty(choice) :
  if choice == 1 :
    return easy_difficulty
  elif choice == 2:
    return Medium_diffuculty
  else :
    return Hard_difficulty
turns = difficulty(choice)

def game(turns) :
  print(logo)
  print("Welcome To Number Guessing Game ")
  answer = randint(1 , 100)
  guess = 0
  while guess != answer :
    guess = int(input("Enter A Guess B/W 1 And 100 "))
    turns = turns -  1
    print(turns)
    if turns == 0 :
      break
      
    start(guess,answer)  

game(turns)
