"""Basic interface for my programs """
print("Launching Program")

import datetime
import updatespreadsheet
import apcalculator
import random
import generalfunction


def chkpromot(sentence):
    #if the user's input is a greeting, the return a randomly chosen greeting response
    for word in sentence.split():
        if word.lower() in stock:
            return 1
        if word.lower() in time:
            return 2
        if word.lower() in fgo:
            return 3
        if word.lower() in exit:
            return 999




goodbyeday = ["have a nice day Boss!","Good day Boss!", "I look forward to serve you again Boss!", "See you soon Boss!"]
goodbyenight =["Good night Boss!", "Take care Boss!"]
stock = ["stock","stocks","investing"]
time = ["time"]
fgo = ["ap", "fgo", "fate"]
exit =["bye","good night","see you later","later","close","exit","Goodbye"]

DT = datetime.datetime.now()
currenttime = "It is " + DT.strftime("%H:%M:%S") + " now"

yourname = ("Anew")

if DT.strftime("%H") < "12":
    print("Good morning boss, " + yourname +" at your service")
    print(currenttime)

elif DT.strftime("%H") < "18":
    print("Good evening boss, " + yourname +" at your service")
    print(currenttime)

else:
    print("Good night boss, " + yourname +" at your service")
    print(currenttime)

print("Would you like to use voice recognition? y/n")
modechoice = input("")
if modechoice.lower() == "y":
    promot = generalfunction.sR()
else:
    promot = input("How can I help you today? ")

while chkpromot(promot) != 999:
    print(promot)
    if chkpromot(promot)==2:
        DT = datetime.datetime.now()
        currenttime = "It is " + DT.strftime("%H:%M:%S") + " now"
        print(currenttime)
    elif chkpromot(promot)==1:
        updatespreadsheet.main()
    elif chkpromot(promot)==3:
        print("If you like to calculate ap press 1\nIf you like to view your history press 2\n")
        choice = generalfunction.getnumber("")
        while choice != 1 and choice != 2:
            print("Please input a valid option!")
            choice = generalfunction.getnumber("")
        if choice == 1:
            apcalculator.cal()
        elif choice ==2:
            apcalculator.showhistory()
    else:
        print("Please say something")

    if modechoice.lower() == "y":
        promot = generalfunction.sR()
    else:
        promot = input("How can I help you today? ")


if promot == "exit" and DT.strftime("%H") < "12":
    print(random.choice(goodbyeday))
    input("type enter to exit")
else:
    print(random.choice(goodbyenight))
    input("press enter to exit")





