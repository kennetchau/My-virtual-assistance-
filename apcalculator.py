"""Codes use to calculate how long it will needed to recharge ap in the game fate grand order"""
import datetime
import generalfunction
import pickle

def cal():
    current = generalfunction.getnumber("What is your current ap? ")
    difference_40 = 40 - float(current)
    difference_80 = 80 - float(current)
    difference_120 = 120 - float(current)
    timeneededminute_40 = difference_40 * 5
    timeneededminute_80 = difference_80 * 5
    timeneededminute_120 = difference_120 * 5
    now = datetime.datetime.now()
    timeofcompletion_40 = now + datetime.timedelta(hours=0, minutes=timeneededminute_40, seconds=0)
    timeofcompletion_80 = now + datetime.timedelta(hours=0, minutes=timeneededminute_80, seconds=0)
    timeofcompletion_120 = now + datetime.timedelta(hours=0, minutes=timeneededminute_120, seconds=0)
    print("Your ap will be replenish to 40 at " + str(timeofcompletion_40))
    print("Your ap will be replenish to 80 at " + str(timeofcompletion_80))
    print("Your ap will be replenish to 120 at " + str(timeofcompletion_120))
    timeofcompletiondat = open("timeofcompletion.dat","wb")
    pickle.dump(str(timeofcompletion_40),timeofcompletiondat)
    pickle.dump(str(timeofcompletion_80), timeofcompletiondat)
    pickle.dump(str(timeofcompletion_120), timeofcompletiondat)
    timeofcompletiondat.close()

def showhistory():
    timeofcompletion = open("timeofcompletion.dat","rb")
    value1 = pickle.load(timeofcompletion)
    value2 = pickle.load(timeofcompletion)
    value3 = pickle.load(timeofcompletion)
    print("Your ap will be replenish to 40/80/120 at " + str(value1)+", "+str(value2)+", "+str(value3))




