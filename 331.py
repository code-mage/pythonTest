#Problem 2
import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)
current_time = datetime_object.strftime("%H:%M:%S")
print("Current Time =", current_time)
future_date_and_time = datetime_object + datetime.timedelta(hours = 4, minutes=30)
print("future time = ", future_date_and_time.strftime("%H:%M:%S"))

#problem 3

date = input("Enter date in YYYY-MM-DD format")
year, month, day = map(int, date. split('-'))
date = datetime. date(year, month, day)
today = datetime.date.today()
diff = date - today
print(diff)
diff1 = int(diff.days)
if diff1 == 0:
    print("today")
elif diff1 >= -1 and diff1 <=0:
    print("yesterday")
elif diff1 <= 1 and diff1 >=0:
    print("tomorrow")
elif diff1 <= -2 or diff1 >=2:
    print("neither")
    
#XOR gate
print("enter first value")
aInput= int(input())
print("enter second value")
bInput= int(input())

if aInput == 1 and bInput == 1:
    XORGate = "False"
    XORGateNum = 0
elif aInput == 1 and bInput == 0:
    XORGate = "True"
    XORGateNum = 1
elif aInput == 0 and bInput == 1:
    XORGate = "True"
    XORGateNum = 1
elif aInput == 0 and bInput == 0:
    XORGate = "False"
    XORGateNum = 0

print('XOR Gate output is', XORGate, 'or', XORGateNum)
