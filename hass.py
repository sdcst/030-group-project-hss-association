

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
    


