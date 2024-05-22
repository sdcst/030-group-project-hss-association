

import FirstScreen

FirstScreen.TitleScreen()

def authors():
        print("Fuctions by Hassam")
        print("- Finding the Area of a Circle")
        print("- Finding Hypotenuse")
        print("- Finding the Speed")
        print("- Unit Convertion")
        print("------------------------------")

i = 0
a = False

while a != True:
        try:
                i = int(input("Input your number here: "))
                if i == 1:
                        #  
                        a == True      
                if i == 2:
                        authors()  
                        a == True      
                if i == 3:
                        a == True 
                        quit()



        except:
                print("Not a valid input.")
                print("Try again")


