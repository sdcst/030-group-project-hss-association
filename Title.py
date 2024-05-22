

import FirstScreen

FirstScreen.TitleScreen()

i = 0
a = False

while a != True:
        try:
                i = int(input("Input your number here: "))
                if i == 1:
                        print('function for menu here')   
                        a == True      
                if i == 2:
                        print("function for authors here")  
                        a == True      
                if i == 3:
                        a == True 
                        quit()



        except:
                print("Not a valid input.")
                print("Try again")


