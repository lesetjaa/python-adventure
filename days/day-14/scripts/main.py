# TODO - Get variables and the data we are going to use to compare
from game_data import data
from art import logo
from art import vs
import random


# TODO - Find if player is correct(True) or not(False)
def is_higher(dataA: dict, dataB: dict, player_choice: str) -> bool:
    if player_choice == "A":
        return dataA["follower_count"] > dataB["follower_count"]
    elif  player_choice == "B":
        return dataA["follower_count"] < dataB["follower_count"]

# TODO - Get Dataset
def get_random_data():
    first_data_set = random.choice(data)
    while True:
        second_data_set = random.choice(data)
        if first_data_set != second_data_set:
            break
    return [first_data_set, second_data_set]


def game():
    correct = True
    score = 0
    while correct:

        data_set = get_random_data()
        data_a = data_set[0]
        data_b = data_set[1]
        # TODO - Show Comparison

        print(logo)
        print(f"Compare A: {data_a["name"]}, {data_a["description"]}, from {data_a["country"]}.")

        print(vs)
        print(f"Against B: {data_b["name"]}, {data_b["description"]}, from {data_b["country"]}.")

        # TODO - Get the player's choice
        while True:
            choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if choice == "A" or choice == "B":
                break
            print("Enter A or B: ")
        

        correct = is_higher(data_a, data_b, choice)
        # TODO - End the Game and show the score when the user gets it wrong
        if correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}!")

game()