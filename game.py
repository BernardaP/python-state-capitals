import random

from capitals import states

capitals = states

# access each dictionary
# print(capitals[0])

#randomize the dictionaries 
random.shuffle(capitals)

# create dictionaries for answers
correct_answer = {}
wrong_answer = {}
score = []

# initial message
title = "STATE CAPITALS"
center_title = title.center(35)
print("========================================")
print(center_title)
print("========================================")
print("\nHello, ready to learn the state capitals? \nLet's start!")

# main function running the game
def state_game():
    score = 0
    for state in capitals:
        promp = input(f"\n- What is the capital of {state['name']}?: \n  ")
        results = promp
        if state['name'] not in correct_answer:
            correct_answer[state['name']] = 0
            wrong_answer[state['name']] = 0  
        if results.lower() == state['capital'].lower():
            correct_answer[state['name']] += 1 
            score += 1
            total_answers = correct_answer[state['name']] + wrong_answer[state['name']]
            print(f"\n  That is correct!")
            print(f"  You have answered correctly {correct_answer[state['name']]} out of {total_answers}")
            print(f"  Score: {score}")
        else:
            wrong_answer[state['name']] += 1
            total_answers = correct_answer[state['name']] + wrong_answer[state['name']]
            print(f"\n  That is not the capital of {state['name']}, sorry!")  
            print(f"  Right answer: {state['capital']}")
            print(f"  You have answered correctly {correct_answer[state['name']]} out of {total_answers}")

# functions for answers and total score
def r_answer():
    print(f"\nCorrect answers per state:")
    for key in correct_answer:
        print(f" {key} = {correct_answer[key]}")
    
def w_answer():
    print(f"\nIncorrect answers per state:")
    for key in wrong_answer:
        print(f" {key} = {wrong_answer[key]}")

def total_score():        
    points = correct_answer.values()
    score = sum(points)
    print(f"\nTotal Points: {score}")     

# loop to run the game and give user option to exit it
message = "\nDo you want to play again? (yes/no)"  

while message != "no":
    state_game()
    message = input("\nDo you want to play again? (yes/no) \n" )
    if message != "no":
        print(f"\nLet's keep playing!")   
    else:
       print(f"\n----------------------------")
       print(f'Here is your score: ')
       print(f"----------------------------")
       total_score()
       r_answer()
       w_answer()
       print(f"----------------------------")
       print(f'\nThanks for playing! \nSee you next time!\n') 
        

        

