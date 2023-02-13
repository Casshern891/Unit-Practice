import random

def add_practice():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    ans = a + b
    question = "What is {} plus {}?".format(a, b)
    print(question)
    guess = input("Answer :")
    if guess != str(ans):
        print("Sorry! That was incorrect.")

def start_program():
    print("Welcome to addtion practice.")
    print("Here are 10 questions")
    for i in range(10):
        add_practice()
    print("Well done!")

start_program()