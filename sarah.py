

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
    l = input("pick a level: hard ,medium or easy")
    if l == "easy":
        print("pick a number between 1 - 10")
        n = 2
        n = float(n)
        for n in range(1,10):
            if n == "2":
                print("you got it!")
            else:
                print("not quite")

    elif l == "medium":
        print("pick a number between 1-50")
        nn = 10
        nn = float(nn)
        for nn in range(1,50):
            if nn == "10":
                print("you got it!")
            else:
                print("not quite")

                
    elif l == "hard":
        print("pick a number between 1-100")
        nnn = 57
        nnn = float(nnn)
        for nnn in range(1,100):
            if nnn == "57":
                print("you got it!")
            else:
                print("not quite")
     
    
