
import FirstScreen

FirstScreen.TitleScreen()

def authors():


        print("Fuctions by Hassam")
        print("- Finding the Area of a Circle")
        print("- Finding Hypotenuse")
        print("- Finding the Speed")
        print("- Unit Convertion")
        print("------------------------------")
        print("Fuctions by Sarah")
        print("- Finding the Area of a Rectangle")
        print("- Finding the Area of a Triangle")
        print("- Finding the Volume of a Cylinder")
        print("- Budgeting")
        print("------------------------------")
        print("Fuctions by Sophie")
        print("- Finding the Volume of a Cube")
        print("- Determining Grocery Taxes ")
        print("- Determining Compound Interest")
        print("- Game of BlackJack")

def circle_area():
        
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

        d = 0
        pi = math.pi

        while d == 0:
                try:
                        d = float(input("Please input a your diameter: "))
                        r = d/2
                        r2 = math.pow(r,2)
                        a = r2 * pi
                        a = round(a,2)

                        r = str(r)
                
                        print("---Getting the Radius---")
                        print(d,'÷ 2 =', r)
                        print("---Getting the Area---")
                        print(r+"^2 * π")
                        print("---Answer---")
                        print(a,"is your area!")

                except:
                        if d == 0:
                                print("Not a valid input")
                                print("Try again")

        replayAnswer = replay()
        if replayAnswer == True:
                print("\n")
                circle_area()
        else:
                print("\n")
                instructions()

def right_triangle_hypotenuse_finder():
        
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

        a = 0
        b = 0

        while a == 0:
                try:
                        a = int(input("Please input your a side of the right triangle: "))
                except:
                        print("Invaild input")
                        print("Please try again!")
        while b == 0:        
                try:
                        b = int(input("Please input your b side of the right triangle: "))
               
                except:
                        print("Invaild input")
                        print("Please try again!")
               
        a2 = math.pow(a,2)
        b2 = math.pow(b,2)

        c2 = a2 + b2
        cs = math.sqrt(c2)
        c = round(cs,2)
        
        a = str(a)
        b = str(b)
        c2 = str(c2)

        print("---a^2 + b^2 = c^2---")
        print(a+"^2 +",b+"^2 =",c2)
        print("---Square rooting c^2---")
        print('√'+c2,'=', cs)
        print("---Answer---")
        print('your right triangle hypotenuse is',c)

        replayAnswer = replay()
        if replayAnswer == True:
                print("\n")
                right_triangle_hypotenuse_finder()
        else:
                print("\n")
                instructions()

def unit_conversion():
        
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
        
        num = 0
        unit1 = ''
        U1 = False
        unit2 = ''
        a = 0

        while num == 0:
                
                try:
                        num = int(input("Please input your number: "))
                        print("-----------------")
                except:
                        print("Invaild input")
                        print("Please try again!")
                        print("-----------------")
        
        while U1 != True:
                
                try:
                        print("What unit of measurement did you enter?")
                        print("pick one of the following:")
                        print("(cm/mm/m/in)")
                        U11 = False
                        while U11 != True:
                                unit1 = input(': ')
                                if unit1 == 'cm' or unit1 == 'mm' or unit1 == 'm' or unit1 == 'in':
                                        U11 = True
                                        U1 = True
                        continue

                except:
                                print(unit1,"is not a vaild input")
                                print("Please try again!")
                                print("-----------------")
        U2 = False
        while U2 != True:
                
                try:
                        print("What unit of measurement do you want to convert to?")
                        print("pick one of the following:")
                        print("(cm/mm/m/in)")
                        U22 = False
                        while U22 != True:
                                unit2 = input(': ')
                                if unit2 == 'cm' or unit2 == 'mm' or unit2 == 'm' or unit2 == 'in':
                                        U22 = True
                                        U2 = True
                except:
                        print(unit2,"is not a vaild input")
                        print("Please try again!")
                        print("-----------------")
                
        if unit1 == unit2:
                print('what.')

        #-------cm---------------------------------------------------               
        
        if unit1 == 'cm' and unit2 =='mm':
                unit3 = num * 10
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'cm' and unit2 == 'm':
                unit3 = num / 100
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'cm' and unit2 == 'in':
                unit3 = num / 2.54
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        #-------mm---------------------------------------------------

        if unit1 == 'mm' and unit2 =='cm':
                unit3 = num / 10
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'mm' and unit2 =='m':
                unit3 = num / 1000
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'mm' and unit2 == 'in':
                unit3 = num / 25.4
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        #-------m---------------------------------------------------                

        if unit1 == 'm' and unit2 =='cm':
                unit3 = num * 100
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'm' and unit2 =='mm':
                unit3 = num * 1000
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'm' and unit2 == 'in':
                unit3 = num * 39.37
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        #-------in---------------------------------------------------

        if unit1 == 'in' and unit2 =='cm':
                unit3 = num * 2.54
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'in' and unit2 =='mm':
                unit3 = num * 25.4
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)

        if unit1 == 'in' and unit2 == 'm':
                unit3 = num / 39.37
                num = str(num)
                num1 = str(unit3)
                print(num+unit1,'is',num1+unit2)
        
                replayAnswer = replay()
        if replayAnswer == True:
                print("\n")
                circle_area()
        else:
                print("\n")
                unit_conversion()
                
def distance():

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

        from fractions import Fraction

        d = 0
        t = 0


        while d == 0:
                try:
                        d = float(input("Please input a your distance (km) that you traveled in: "))

                except:
                        if d == 0:
                                print("Not a valid input")
                                print("Try again")
        while t == 0:
                try:
                        t = float(input("Please input the time (minutes) that it took you to travel: "))

                        s = d/t
                        s = round(s,2)

                        print("---Getting the T/D---")
                        print(t,'/',d)
                        print("---Answer---")
                        print('your speed is',s,'km/min')

                except:
                        if t == 0:
                                print("Not a valid input")
                                print("Try again")

                replayAnswer = replay()
                if replayAnswer == True:
                        print("\n")
                        distance()
                else:
                        print("\n")
                        instructions()
    
def cubeVolume():
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
    LC = False
    while LC != True:
        side = input("Enter the lenght of the cube in meters: ")
        try:
            side = float(side)
            LC = True
        except:
            print("Invalid input...try again...")
    v = side**3
    print(f'The volume of that cube is {v} m.')

    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        cubeVolume()
    else:
        print("\n")
        instructions()

def grocerytaxes():
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

    NI = False
    while NI != True:
        n = input("How many items did you purchase? ")
        try:
            n = int(n)
            NI = True
        except:
            print("Invalid input... try again...")

    pricee = 0
    for i in range(n):
        PI = False
        while PI != True:
            price = input("Enter the price of your item(s): ")
            try:
                price = float(price)
                subtotal = pricee + price
                pricee = price
                PI = True
            except:
                print("Invalid input... try again...")

    subtotal = round(subtotal,2)
    pst = subtotal*0.07
    pst = round(pst,2)
    gst = subtotal*0.05
    gst = round(gst,2)
    total = subtotal+pst+gst
    print(f"Your subtotal is ${subtotal} \nThe PST taxe is ${pst} \nThe GST taxe is ${gst} \nWhich brings your total to be ${total}")
    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        grocerytaxes()
    else:
        print("\n")
        instructions()

def compoundinterest():
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
    IB = False
    while IB != True:
        P = input("What is your intial balance? ")
        try:
            P = float(P)
            IB = True
        except:
            print("Invalid input... try again...")

    print("\n")
    IR = False
    while IR != True:
        r = input("What is the interest rate, enter it in as a % (ex: 7% => 7): ")
        try:
            r = float(r)
            r = r/100
            IR = True
        except:
            print("Invalid input... try again...")

    print("\n")

    CY = False
    while CY != True:
        n = input("How many times is it compounded in per year? (ex: monthtly => 12) ")
        try:
            n = float(n)
            CY = True
        except:
            print("Invalid input... try again...")

    print("\n")

    YC = False
    while YC != True:
        t = input("How many years will it be in compound? ")
        try:
            t = float(t)
            YC = True
        except:
            print("Invalid input... try again...")

    print("\n")

    def calculateinterest(P,r,n,t):
        A = P*(1 + r/n)**(n*t)
        A = round(A,2)
        return A

    A = calculateinterest(P,r,n,t) 
    print(f"After {t} of years, your intial money will compound to ${A}.")

    replayAnswer = replay()
    if replayAnswer == True:
        print("\n")
        compoundinterest()
    else:
        print("\n")
        instructions()
        
def BlackJack():
    def replay():
        REPLAY = ""
        while REPLAY != "REPLAY" and REPLAY != "EXIT":
            REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
            if REPLAY == "REPLAY":
                pass
                #BlackJack()
            elif REPLAY == "EXIT":
                #instructions()
                return None
            else:
                print("Invalid Input...")
        return True


    import random
    cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K",]
    start = False

    while start != True:
        play = input("Welcome to BlackJack! Enter \"PLAY\" to start: ")
        if play != "PLAY":
            print("Invalid Entry, retry...")
        else: 
            start = True
    else :
        card1 = random.choice(cards)
        cards.remove(card1)
        if card1 == "J" or card1 == "Q" or card1 == "K":
            card1 = 10
        card2 = random.choice(cards)
        cards.remove(card2)
        if card2 == "J" or card2 == "Q" or card2 == "K":
            card2 = 10
        SUM = card1+card2
        print(f"Your two first cards are {card1} and {card2}. The sum of your cards is {SUM}.")

    print("\n")
    
    AIcard1 = random.choice(cards)
    cards.remove(AIcard1)
    if AIcard1 == "J" or AIcard1 == "Q" or AIcard1 == "K":
            AIcard1 = 10
    AIcard2 = random.choice(cards)
    cards.remove(AIcard2)
    if AIcard2 == "J" or AIcard2 == "Q" or AIcard2 == "K":
            AIcard2 = 10
    AIsum = AIcard1+AIcard2
    print(f"Here is one of your opponent's cards: {card2}.")
    
    print("\n")

    while SUM != 21:
        answer = input("Do you wish to \"HIT\" or \"STAY\"? ")
        if answer != "HIT" and answer != "STAY":
            print("Invalid Input, please try again...\n")
        elif answer == "HIT" or answer == "STAY":
            if answer == "HIT":
                card3 = random.choice(cards)
                cards.remove(card3)
                if card3 == "J" or card3 == "Q" or card3 == "K":
                    card3 = 10
                SUM = SUM+card3
                if SUM <= 21:
                    print(f"Your card is {card3}. The sum of your cards are now {SUM}. ")
                elif SUM > 21:
                    print(f"Uh oh, you busted, the card you got was {card3}, your sum is {SUM}, you lost.")
                    replayAnswer = replay()
                    if replayAnswer == True:
                        BlackJack()
                    else:
                        instructions()                          
            elif answer == "STAY":
                    print(f"The sum of your cards is {SUM}. Let's see what your opponent got. \n")
                    break

    while AIsum <= 16:
        AIcard3 = random.choice(cards)
        cards.remove(AIcard3)
        AIsum = AIsum + AIcard3
        if AIsum > 21:
            print(f"Oh uh! Your opponent busted, you won!")
            replayAnswer = replay()
            if replayAnswer == True:
                BlackJack()
            else:
                instructions()
    else:
        print(f"Your opponent's sum is {AIsum}.")
 
    if AIsum > SUM:
        print(f"Your opponent got closer to 21. \nYou lost.\n")
        replayAnswer = replay()
        if replayAnswer == True:
            BlackJack()
        else:
            instructions()
    elif SUM > AIsum:
        print(f"You got closer to 21. \nYou won!\n")
        replayAnswer = replay()
        if replayAnswer == True:
            BlackJack()
        else:
            instructions()
    elif SUM == AIsum:
        print("You and your opponent tied!\n")
        replayAnswer = replay()
        if replayAnswer == True:
            BlackJack()
        else:
            instructions()

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

def instructions():
    print('Welcome to the instructions! \nIn here you will be able to get a preview of all 13 functions available to you to use. \nWhen done reading all of the options, you may chose a function to use. ')
    print("\n")
    print("➣1 Volume of cube: \nThis function will help you determine the volume of your cube by giving it the mesurements in meters.")
    print("\n")
    print("➣2 Grocery taxes: \n This function will help you calcute the subtotal, GST, PSt and total.")
    print("\n")
    print("➣3 Compound Interest: \nThis function will help you calculate your compound interest.")
    print("\n")
    print("➣4 BlackJack: \nThis is a game of BlackJack.\nThe rule to win is have a higher hand value than your opponent, without going over 21.\nPlayers are dealt two cards and can then choose to “hit” (receive additional cards) or “stand” (keep their current hand). \nYour opponent also receives two cards, but only one is face up.\nIf the player’s hand exceeds 21, they “bust” and lose the game. \nIf the opponent busts, player wins. If neither the player nor the opponent busts, the player with the highest hand value closest to 21, wins.")
    print("\n")
    print("➣5 Area of a rectangle: \nThis function will help you determine the area of a rectangle.")
    print("\n")
    print("➣6 Area of a triangle: \nThis function will help you determine the area of a triangle.")
    print("\n")
    print("➣7 Volume of cylinder:\nThis function will help you determine the volume of a cylinder.")
    print("\n")
    print("➣8 Budgeting:\nThis function will help you determine your monthly budget to spend.")
    print("\n")
    print("➣9 Number Guessing:\nThis is a game of number guessing. \nThere are three difficulty levels: easy, medium and hard.\nThere will be a random number for you to guess.")
    print("\n")
    print("➣10 Area of Circle:\nThis function will help you determine the area of a circle.")
    print("\n")
    print("➣11 hypotenuse finder:\nThis function will help you determing the hypotenuse of a triangle. ")
    print("\n")
    print("➣12 Speed Finder:\nThis function will help you determine the speed of your travelling subject.")
    print("\n")
    print("➣13 Unit Conversion: \nThis function will help you convert units.")
    print("\n")
    print("If you wish to exit, enter \"EXIT\".")
    
    print("The functions are numbered from 1-13. ")
    AF = False
    while AF != True:
        ANSWER = input("\nWhich funtion would you like to access? (ex: 8)")
        if ANSWER == "EXIT" or ANSWER == "1" or ANSWER == "2" or ANSWER == "3" or ANSWER == "4" or ANSWER == "5" or ANSWER == "6" or ANSWER == "7" or ANSWER == "8" or ANSWER == "9" or ANSWER == "10" or ANSWER == "11" or ANSWER == "12" or ANSWER == "13":
            AF = True
        else:
            print("Invalid Entry... try again...\n")

    if ANSWER == "1":
        print("\n")
        cubeVolume()
    elif ANSWER == "2":
        print("\n")
        grocerytaxes()
    elif ANSWER == "3":
        print("\n")
        compoundinterest()
    elif ANSWER == "4":
        print("\n")
        BlackJack()
    elif ANSWER == "5":
        print("\n")
        arearectangle()
    elif ANSWER == "6":
        print("\n")
        areatriangle()
    elif ANSWER == "7":
        print("\n")
        volumecylinder()
    elif ANSWER == "8":
        print("\n")
        budget()
    elif ANSWER == "9":
        print("\n")
        numberguessing()
    elif ANSWER == "10":
        print("\n")
        circle_area()
    elif ANSWER == "11":
        print("\n")
        right_triangle_hypotenuse_finder()
    elif ANSWER == "12":
        print("\n")
        distance()
    elif ANSWER == "13":
        print("\n")
        unit_conversion()
    elif ANSWER == "EXIT":
        FirstScreen.TitleScreen()
        start_menu()
    return None

def start_menu():
        a = False
        while a != True:
                i = input("Input your number here: ")
                if i in ['1','2','3']:
                        if i == "1":
                                instructions()
                        if i == "2":
                                authors()  
                        if i == "3":
                                a = True 
                                print("Goodbye!")

                else:
                        print("Not a valid input.")
                        print("Try again")
        exit()

start_menu()
