import random

def sub():
    a = random.randint(1, 9)
    b = random.randint(1, a)
    ans = a - b
    question = "What is {} minus {}?".format(a, b)
    print(question)
    guess = input("Answer: ")
    if guess != str(ans):
        print("Sorry! That was incorrect.")

def start():
    print("Welcome! Here are 10 subtraction questions:")
    for i in range(10):
        sub()
    print("Well done!")

start()
