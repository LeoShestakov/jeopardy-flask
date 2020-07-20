import random

def calc_points(game_info, answer):
    value = game_info['value']
    if value != "":
        if answer.lower() == game_info['answer'].lower():
            return value
        else:
            return value * -1
    
# def game(score):
#     round= display_clue(random_index())
#     print(f"Your category is {round[0]} for {round[2]} points.")
#     print(f"{round[1]}")
#     answer= input("Type your answer here: ").lower()
#     if similar_text(answer, round[3]) > 55:
#         score+=round[2]
#     else:
#         score-=round[2]
#     print(f"The answer is {round[3]}.")
#     print(f"Your score: {score}")
#     response= input("Ready for the next question? (Y/N)")
#     if response == "Y":
#         game(score)
#     else:
#         print(f"Final score: {score}")
#         print("See you next time!")