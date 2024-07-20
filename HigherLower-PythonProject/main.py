 #Function to compare the follower count of two random dictionaries
    #and return True if the first dictionary has more followers than the second one
    #and False if the second dictionary has more followers than the first one
    #and also increase the score by 1 if the first dictionary has more followers than the second
    #and decrease the score by 1 if the second dictionary has more followers than the first one
    #and return the score
    #and also print the score
    #and also print the winner
    #and also print the loser
    #and also print the game over message
    #and also print the final score


import random
from art import logo
from art import vs
from gamedata import data
#import os

#Creating the HigherLower-game

global Current_Score
Current_Score = 0

#Function to compare the follower count of two random dictionaries
def compare_dicts():
    print(logo)
    score = Current_Score
    guessing = True
    while guessing:
        dict1 = random.choice(data)
        dict2 = random.choice(data)

        print(f"A: {dict1['name']}, {dict1['description']}")
        print(vs)
        print(f"B: {dict2['name']}, {dict2['description']}")
        global following
        following = input("Who has more following: Type 'A' or 'B': ")

        if (following == 'A' and dict1["follower_count"] > dict2["follower_count"]) or (following == 'B' and dict2["follower_count"] > dict1["follower_count"]):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            guessing = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
        
compare_dicts()





    
    









    
    
    



