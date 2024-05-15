def instructions():
    # Will display instructions
    # input p[loarameters: none needed
    # output parameters: None
    # Author:
    # Modified:
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
        card2 = random.choice(cards)
        cards.remove(card2)
        sum = card1+card2
        print(f"Your two first cards are {card1} and {card2}. The sum of your cards is {sum}.")

BlackJack()