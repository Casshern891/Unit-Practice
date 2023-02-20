import random

def times():
  a = random.randint(3, 9)
  b = random.randint(1, 9)
  ans = a * b
  question = "What is {} times {}?".format(a, b)
  print(question)
  guess = input("Answer: ")
  if guess != str(ans):
    print("Sorry! the right answer was {}.".format(ans))

def start():
    print("Welcome to times table practice.")
    print("Here are 10 questions:")
    for i in range(10):
        times()
    print("Well done!")

start()
