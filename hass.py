

def circle_area():

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


def right_triangle_hypotenuse_finder():
        
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
                
def unit_conversion():

        num = 0
        unit1 = ''
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
        
        while unit1 == "":
                
                try:
                        print("What unit of measurement did you enter?")
                        print("pick one of the following:")
                        print("(cm/mm/m/km)")
                        unit1 = input(': ')
                        unit1 == 'cm' or unit1 == 'mm' or unit1 == 'm' or unit1 == 'km'
                        continue

                except:
                                print(unit1,"is not a vaild input")
                                print("Please try again!")
                                print("-----------------")
        
        while unit2 == "":
                
                try:
                        print("What unit of measurement do you want to convert to?")
                        print("pick one of the following:")
                        print("(cm/mm/m/km)")
                        unit2 = input(': ')
                
                        if unit1 == unit2:
                                print('what.')
                        if unit1 == 'cm' and unit2 =='mm':
                                unit3 = num * 10
                                print('your new unit is',num+unit2)
                                



                except:
                        if unit2 != 'cm' or unit2 != 'mm' or unit2 != 'm' or unit2 != 'km':

                                print(unit2,"is not a vaild input")
                                print("Please try again!")
                                print("-----------------")

        

                

                
                




def distance():

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


        


