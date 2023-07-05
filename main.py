import art
from game_data import data
import random

Logo = art.logo
score = 0
game = True
res1 = random.choice(data)

#Displaying the Options
def display_data(account):
  acc_name = account["name"]
  acc_disp = account["description"]
  acc_country = account["country"]
  return f"{acc_name}, a {acc_disp}, from {acc_country}"

#check Answers
def check(option, fc_a, fc_b):
  if fc_a > fc_b:
    return option == "A"
  else:
    return option == "B"

#Getting the Data
#Making Game Repitation
while game:
  
  print(Logo)
  res = res1
  res1 = random.choice(data)

  while res == res1:
    res1 = random.choice(data)

  
  #Printing Optons to Choose From
  print(f"Compare A : {display_data(res)}")
  print(art.vs)
  print(f"Compare B : {display_data(res1)}")
  
  option = input("Who has more Followers A or B : ")
  
  #GEtting the Follower Count
  fc_a = res["follower_count"]
  fc_b = res1["follower_count"]
  
  correct = check(option, fc_a, fc_b)
  #Giving Answer Feedback and Counting Score
  if correct:
    score += 1
    print(f"Correct Answer. Your Current Score : {score}")
  else:
    game = False
    print(f"Wrong Answer. Your Current Score: {score}")
