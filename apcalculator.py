"""Codes use to calculate how long it will needed to recharge ap in the game fate grand order"""
import datetime
import generalfunction
import pickle

def cal():
    current = generalfunction.getnumber("What is your current ap? ")
    target = generalfunction.getnumber("What is your target ap? ")
    while generalfunction.checklarger(current,target) != True:
        print("Current ap should be smaller than target ap!")
        current = generalfunction.getnumber("What is your current ap? ")
        target = generalfunction.getnumber("What is your target ap? ")
    difference = float(target) - float(current)
    timeneededminute = difference * 5
    now = datetime.datetime.now()
    timeofcompletion = now + datetime.timedelta(hours=0, minutes=timeneededminute, seconds=0)
    print("Your ap will be replenish to target at " + str(timeofcompletion))
    pickle.dump(timeofcompletion, open("timeofcompletion.dat","wb"))

def showhistory():
    timeofcompletion = pickle.load(open("timeofcompletion.dat","rb"))
    print("Your ap will be replenish to target at " + str(timeofcompletion))




