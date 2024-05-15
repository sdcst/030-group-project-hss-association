

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
    easy = [1,2,3,4,5,6,7,8,9,10]
    medium = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    hard = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    l = input("pick a level: hard ,medium or easy")
    if l == "easy":
        n = input("pick a number between 1 - 10")
        
        for n in range(1,10):
            round1 = random.choice(easy)
            while n  == round1:
                print("you got it!")
                break
            if n != round1:
                print("not quite")
                break

    elif l == "medium":
        nn = input("pick a number between 1-50")
       
        for nn in range(1,50):
            round2 = random.choice(medium)
            while nn == round2:
                 print("you got it!")
                 break
            if nn != round2:
                print("not quite")
                break

                
    elif l == "hard":
        nnn = input("pick a number between 1-100")
        
        for nnn in range(1,100):
            round3 = random.choice(hard)
            while nnn == round3:
                print("you got it!")
                break
            if nnn !=round3:
                print("not quite")
                break
numberguessing()     
    
