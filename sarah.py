
def arearectangle():
    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
            elif REPLAY == "EXIT":
                return None
            else:
                print("Invalid Input...")
        return True

    l = input("enter the length ")
    w = input("enter the width ")
    l = float(l)
    w= float(w)
    a = l*w
    print(f"the area of the rectangle given is {a} ")

    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        arearectangle()
    else:
        print("\n")
        instructions()
   

def areatriangle():
    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
            elif REPLAY == "EXIT":
                return None
            else:
                print("Invalid Input...")
        return True

    b = input("enter the base")
    h = input("enter the height")
    b = float(b)
    h = float(h)
    a = 0.5*b*h
    print(f"the area of the triangle is {a} ")

    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        areatriangle()
    else:
        print("\n")
        instructions()

def volumecylinder():
    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
            elif REPLAY == "EXIT":
                return None
            else:
                print("Invalid Input...")
        return True

    import math 
    r = input("enter radius")
    h = input("enter in the height")
    r = float(r)
    h = float(h)
    v = math.pi*r**0.5*h
    print(f"the volume of a cylinder is {v}")

    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        volumecylinder()
    else:
        print("\n")
        instructions()


def budget():

    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
            elif REPLAY == "EXIT":
                return None
            else:
                print("Invalid Input...")
        return True

    h = input("what is your hourly income?")
    m = input("what is your monthly income?")
    r = input("how much is your monthly rent?")
    h = float(h)
    m = float(m)
    r = float(r)
    total = m - r
    total = float(total)
    print(f"the have {total} dollars to spend on groceries, phone, living needs,savings, etc per month ")
    
    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        budget()
    else:
        print("\n")
        instructions()

def numberguessing():
    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
            elif REPLAY == "EXIT":
                return None
            else:
                print("Invalid Input...")
        return True 

    import random   

    print("Welcome to number guessing!\nYou will get 5 attempts for easy, 7 attempts for medium and 10 attempts for hard.")

    LL = False
    while LL != True:
        l = input("pick a level: hard ,medium or easy: ")
        try:
            if l == "easy" or l == "medium" or l == "hard":
                LL = True
        except:
            print("Invalid input.. try again...")

    if l == "easy":
        max_number = 10
        attempts = 5
        LL == True
    elif l == "medium":
        max_number = 50
        attempts = 7
        LL == True
    elif l == "hard":
        max_number = 100
        attempts = 10
        LL == True
        


    secret_number = random.randint(1, max_number)
    print(f"I am thinking of a number between 1 and {max_number} you have{attempts} attempts")

    for attempts in range (1, attempts + 1):
        guess = int(input("enter your guess: "))
        if guess < secret_number:
            print("oops! too low, try again")
        elif guess > secret_number:
            print("oops! too high , try again")
        else:
            print(f"Yay! you guessed the correct number, {secret_number} was the answer")
            replayAnswer = replay()
            if replayAnswer == True:
                print("\n")
                numberguessing()
            else:
                print("\n")
                instructions()

    print(f"sorry you run out of attempts the correct answer was {secret_number}")
    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        numberguessing()
    else:
        print("\n")
        instructions()

        
        