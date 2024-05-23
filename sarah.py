
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
    
    CM = False
    while CM != True:
        l = input("enter the length in (cm): ")
        try:
            l = float(l)
            CM = True
        except:
            print("Invalid Entry... try again... ")
    
    WM = False
    while WM != True:
        w = input("enter the width in (cm): ")
        try:
            w = float(w)
            WM = True
        except:
            print("Invalid Entry... try again... ")
    

    a = l*w
    print(f"the area of the rectangle given is {a}cm squared. ")

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

    TB = False
    while TB != True:
        b = input("enter the length of the base of the triangle in (cm): ")
        try:
            b = float(b)
            TB = True
        except:
            print("Invalid Entry... try again... ")

    HT = False
    while HT != True:
        h = input("enter the height of the triangle in (cm): ")
        try:
            h = float(h)
            HT = True
        except:
            print("Invalid Entry... try again... ")
 
    a = 0.5*b*h
    print(f"the area of the triangle is {a}cm.  ")

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
    
    RC = False
    while RC != True:
        r = input("enter radius of the cylinder in (cm); yahoo")
        try:
            r = float(r)
            RC = True
        except:
            print("Invalid entry... try again...")

    HC = False
    while HC != True:
        h = input("enter in the height of the cylinder in (cm): ")
        try:
            h = float(h)
            HC = True
        except:
            print("Invalid entry... try again...") 
    
    
    v = math.pi*r**0.5*h
    print(f"the volume of a cylinder is {v}cm cubed.")

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

    HI = False
    while HI != True:
        h = input("what is your hourly income? ")
        try:
            h = float(h)
            HI = True
        except:
            print("Invalid entry... try again...")

    MI = False
    while MI != True:
        m = input("what is your monthly income? ") 
        try:
            m = float(m)
            MI = True
        except:
            print("Invalid entry... try again...")
    
    MR = False
    while MR != True:
        r = input("how much is your monthly rent? ") 
        try:
            r = float(r)
            MR = True
        except:
            print("Invalid entry... try again...")
    
    total = m - r
    total = float(total)
    print(f"the have ${total} dollars to spend on groceries, phone, living needs,savings, etc per month.")
    
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
        if l == "easy" or l == "medium" or l == "hard":
            LL = True
        else:
            print("Invalid input.. try again...")

    if l == "easy":
        max_number = 10
        attempts = 5
        
    elif l == "medium":
        max_number = 50
        attempts = 7
        
    elif l == "hard":
        max_number = 100
        attempts = 10
        
        


    secret_number = random.randint(1, max_number)
    print(f"\nI am thinking of a number between 1 and {max_number} you have {attempts} attempts")

    for attempts in range (1, attempts + 1):
        GUESS = False
        while GUESS != True:
            guess = input("enter your guess: ")
            try:
                guess = float(guess)
                GUESS = True
            except:
                print("That guess was not valid. try again...\n")
                
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

numberguessing()

        
        