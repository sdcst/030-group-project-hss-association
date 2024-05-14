

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

    volumecylinder()

def budget():
    h = input("what is your hourly income?")
    m = input("what is your monthly income?")
    r = input("how much is your rent?")
    h = float(h)
    m = float(m)
    r = float(r)
    total = h + m - r
    total = float(total)
    print(f"the have {total} dollars to spend on groceries, phone, living needs,etc ")
     
    
