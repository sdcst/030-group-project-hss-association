

i = 0

while i != 1 or 2 or 3:
        try:
                i = int(input("Input your number here: "))
                if i == 1:
                        print('function for menu here')         
                if i == 2:
                        print("function for authors here")  
                if i == 3:
                        quit
                else:
                        print("Not a valid input.")
                        print("Try again")
        except:
                print("Not a valid input.")
                print("Try again")


#notdone