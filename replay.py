#put this at the top of your function
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


#put this at the end of your function or whenever your player stops the function
replayAnswer = replay()
if replayAnswer == True:
    print("\n")
    #put ur function name here ex; function()
else:
    print("\n")
    instructions()