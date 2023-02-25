import random
import os
import higherlower

logo = higherlower.logo
vs = higherlower.vs
data = higherlower.data

score = 0

answer = ""
guess = ""

def genData():
    global answer
    global guess
    global score

    firstData = data[random.randint(0, len(data) - 1)]
    secondData = data[random.randint(0, len(data) - 1)]

    while (firstData["name"] == secondData["name"]):
        secondData = data[random.randint(0, len(data) - 1)]
        
    firstDataFollowers = firstData["follower_count"]
    secondDataFollowers = secondData["follower_count"]

    print(logo)

    print(f"Compare A: {firstData['name']}, a {firstData['description']}, from {firstData['country']}.")

    print(vs)

    print(f"Against B: {secondData['name']}, a {secondData['description']}, from {secondData['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (guess != "A" and guess != "B"):
        os.system("clear")
        print("Invalid input. Please try again.")
        genData()
        return

    if (firstDataFollowers > secondDataFollowers):
        answer = "A"
    else:
        answer = "B"

    if (guess != answer):
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score += 1
        os.system("clear")
        print(f"You're right! Current score: {score}")
        genData()

genData()




