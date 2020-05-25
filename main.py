"""Basic interface for my programs """
print("Launching Program")

import datetime as dt
import stocks
import apcalculator
import random
import generalfunction
import news
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
        if word.lower() in new:
            return 5
        if word.lower() in settings:
            return 6
        if word.lower() in helps:
            return 0
        if word.lower() in exit:
            return 999

# ui response
goodbyeday = ["have a nice day Boss!","Good day Boss!", "I look forward to serve you again Boss!", "See you soon Boss!"]
goodbyenight =["Good night Boss!", "Take care Boss!"]
# user inputs list
stock = ["stock","stocks","investing"]
time = ["time"]
fgo = ["ap", "fgo", "fate"]
exit =["bye","good night","see you later","later","close","exit","Goodbye"]
note= ["notes","note"]
settings = ["setting","settings","voice","voice recognition"]
new = ['Whats new', 'news', "today's news"]
helps = ['help']

DT = dt.datetime.now()
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

modechoice = "n" #disable voice recognition by default

promot = input("How can I help you today? ")

while chkpromot(promot) != 999:
    print(promot)
    if chkpromot(promot)==2:
        DT = dt.datetime.now()
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
        originalpathnote = os.getcwd()
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
                print(file1.read().splitlines())
                file1.close()
            elif action == 2:
                file1 = open(filename, "a+")
                messages = input("What's the messages? ")
                file1.write(messages+"\n")
                file1.close()
        os.chdir(originalpathnote)

    elif chkpromot(promot)==5:
        choice = generalfunction.getnumber("Would you like to get news from new york times (press 1), cnbc (press 2), financial times(press 3), cbc(press4)? ")
        print("")
        print("_"*30)
        if choice == 1:
            news.main("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
        if choice == 2:
            news.main("https://www.cnbc.com/id/100003114/device/rss/rss.html")
        if choice == 3:
            news.main("https://www.ft.com/?format=rss")
        if choice == 4:
            news.main("https://www.cbc.ca/cmlink/rss-topstories")

    elif chkpromot(promot)==6:
        print("Would you like to use voice recognition? y/n")
        modechoice = input("")

    elif chkpromot(promot)==0:
        print("type stock to find stocks \ntype time to check time \ntype note to check note\ntype news to check news\ntype setting to check voice recognition settings\ntype exit to leave")

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





