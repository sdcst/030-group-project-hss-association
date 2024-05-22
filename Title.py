

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





i = 0
a = False

def start_menu():
        while a != True:
                try:
                        i = int(input("Input your number here: "))
                        if i == 1:
                                #fuctions here  
                                a == True

                        if i == 2:
                                authors()  
                                a == True 

    
                        if i == 3:
                                a == True 
                                exit()



                except:
                        print("Not a valid input.")
                        print("Try again")

start_menu()
