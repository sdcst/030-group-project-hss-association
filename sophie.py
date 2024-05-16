def instructions():
    # Will display instructions
    # input p[loarameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print('instructions are here')
    return None

def cubeVolume():
    side = input("Enter the lenght of the cube in meters: ")
    side = float(side)
    v = side**3
    print(f'The volume of that cube is {v} m.')

def grocerytaxes():
    n = input("How many items did you purchase? ")
    n = int(n)
    pricee = 0
    for i in range(n):
        price = input("Enter the price of your item(s): ")
        price = float(price)
        subtotal = pricee + price
        pricee = price
    subtotal = round(subtotal,2)
    pst = subtotal*0.07
    pst = round(pst,2)
    gst = subtotal*0.05
    gst = round(gst,2)
    total = subtotal+pst+gst
    print(f"Your subtotal is ${subtotal} \nThe PST taxe is ${pst} \nThe GST taxe is ${gst} \nWhich brings your total to be ${total}")

def compoundinterest():
    P = input("What is your intial balance? ")
    P = float(P)
    r = input("What is the interest rate, enter it in as a % (ex: 7% => 7): ")
    r = float(r)
    r = r/100
    n = input("How many times is it compounded in per year? (ex: monthtly => 12) ")
    n = float(n)
    t = input("How many years will it be in compound? ")
    t = float(t)
    def calculateinterest(P,r,n,t):
        A = P*(1 + r/n)**(n*t)
        A = round(A,2)
        return A

    A = calculateinterest(P,r,n,t) 
    print(f"After {t} of years, your intial money will compound to ${A}.")


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
                    """REPLAY = ""
                    while REPLAY != "REPLAY" and REPLAY != "EXIT":
                        REPLAY = input("Do you wish to \"REPLAY\" or \"EXIT\"? ")
                        if REPLAY == "REPLAY":
                            BlackJack()
                            break
                        elif REPLAY == "EXIT":
                            instructions()
                            return None
                        else:
                            print("Invalid Input...")
                    """                            
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


BlackJack()

