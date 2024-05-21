

def arearectangle():
    l = input("enter the length ")
    w = input("enter the width ")
    l = float(l)
    w= float(w)
    a = l*w
    print(f"the area of the rectangle given is {a} ")

   

def areatriangle():
    b = input("enter the base")
    h = input("enter the height")
    b = float(b)
    h = float(h)
    a = 0.5*b*h
    print(f"the area of the triangle is {a} ")

def volumecylinder():
    import math 
    r = input("enter radius")
    h = input("enter in the height")
    r = float(r)
    h = float(h)
    v = math.pi*r**0.5*h
    print(f"the volume of a cylinder is {v}")

  

def budget():
    h = input("what is your hourly income?")
    m = input("what is your monthly income?")
    r = input("how much is your monthly rent?")
    h = float(h)
    m = float(m)
    r = float(r)
    total = m - r
    total = float(total)
    print(f"the have {total} dollars to spend on groceries, phone, living needs,savings, etc per month ")

def numberguessing():
    import random   

    l = input("pick a level: hard ,medium or easy")
    if l == "easy":
        max_number = 10
        attempts = 5
    elif l == "medium":
        max_number = 50
        attempts = 7
    elif l == "hard":
        max_number = 100
        attempts = 10
    else:
        print("invalid level")
        return

    secret_number = random.randint(1, max_number)
    print(f"welcome to the {l} round of the number guessing game")
    print(f"I am thinking of a number between 1 and {max_number} you have{attempts} attempts")

    for attempt in range (1, attempts + 1):
        guess = int(input("enter your guess:"))
        if guess < secret_number:
            print("oops! too low, try again")
        elif guess > secret_number:
            print("oops! too high , try again")
        else:
            print(f"Yay! you guessed the correct number, {secret_number} was the answer")
            return

    print(f"sorry you run out of attempts the correct answer was {secret_number}")

    print("welcome to the number guessing game")
    while True:
        print("Choose your difficulty level:easy,medium,hard")
        l = input("enter your level of choice:").lower()
        if l in ["easy", " medium", "hard"]:
            numberguessing()
        play_again = input("do you want to play again? yes/no?")
        
        if play_again != "yes":
            print("thanks for playing!")
            break
        else:
            print("invalid choice. Please choose easy, medium,hard.")
numberguessing()