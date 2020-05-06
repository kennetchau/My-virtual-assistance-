"""Basic interface for my programs """
print("Launching Program")

import datetime
import stocks
import apcalculator
import random
import generalfunction
import glob,os



def chkpromot(sentence):
    #if the user's input is a greeting, the return a randomly chosen greeting response
    for word in sentence.split():
        if word.lower() in stock:
            return 1
        if word.lower() in time:
            return 2
        if word.lower() in fgo:
            return 3
        if word.lower() in note:
            return 4
        if word.lower() in exit:
            return 999


goodbyeday = ["have a nice day Boss!","Good day Boss!", "I look forward to serve you again Boss!", "See you soon Boss!"]
goodbyenight =["Good night Boss!", "Take care Boss!"]
stock = ["stock","stocks","investing"]
time = ["time"]
fgo = ["ap", "fgo", "fate"]
exit =["bye","good night","see you later","later","close","exit","Goodbye"]
note= ["notes","note"]

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
        stocks.main()
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
    elif chkpromot(promot)==4:
        print("Which notebook do you want to open?")
        currentpathnote = os.getcwd()+"/note"
        os.chdir(str(currentpathnote))
        for file in glob.glob("*.txt"):
            print(file)
        filename = input("")
        end = 0
        while end != 1:
            action = generalfunction.getnumber("What do you want to do? \nread press 1\nwrite press 2\nquit press 0\n")
            if action == 0:
                end =1
            elif action == 1:
                file1 = open(filename, "r")
                print(file1.readlines())
                file1.close()
            elif action == 2:
                file1 = open(filename, "a+")
                messages = input("What's the messages? ")
                file1.write(messages+"\n")
                file1.close()
    else:
        print("Please say/type something")

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





