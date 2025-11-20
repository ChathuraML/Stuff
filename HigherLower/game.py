import random
import art
from data import data


def details(profile):

    name = profile["name"]
    description = profile["description"]
    country = profile["country"]

    return f"{name}, a {description}, from {country}"

def answer_check(user_input, count_a, count_b):
    if count_a > count_b:
        return user_input == "a"
    else:
        return user_input == "b"
    
profile_b = random.choice(data)
game_status = True
score = 0
while game_status:
    
    profile_a = profile_b
    profile_b = random.choice(data)
    

    if profile_a == profile_b:
        profile_b = random.choice(data)


    print(art.logo)

    print(f"Compare A: {details(profile_a)}")
    print(art.vs)
    print(f"Compare B: {details(profile_b)}")

    follower_count_a = profile_a["follower_count"]
    follower_count_b = profile_b["follower_count"]
    answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    is_answer = answer_check(answer, follower_count_a, follower_count_b)
    if is_answer:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"You lose! Final score: {score}")
        game_status = False
        print("\n" * 20)
