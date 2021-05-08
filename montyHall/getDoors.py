import random

def getGates( ):
   gates = [0,0,0]
   moneyIndex = random.randint(0,2)
   gates[moneyIndex] = 1;
   return gates;

def reveal(gates, selected):
    if (gates[selected] == 0):
        for i in range(0,3):
            if (i != selected and gates[i]==0):
                return i
    else:
        index = random.randint(0,1)
        for i in range(0,3):
            if (gates[i]==0):
                if (i == index):
                    return i;
                index+= 1
                
def chooseGate():
    return random.randint(0,2)

def product(gates, selected, revealed, switch):
    if (switch):
        for i in range(0,3):
            if (i != selected and i != revealed):
                return gates[i]
    else:
        return gates[selected]

times = 100000
predictSwitch = 0
for i in range(0,times):
    gates = getGates();
    firstUserSelection = chooseGate();
    gateRevealedByHost = reveal(gates, firstUserSelection)
    predictSwitch += product(gates, firstUserSelection, gateRevealedByHost, True)
    
predictNotSwitch = 0
for i in range(0,times):
    gates = getGates();
    firstUserSelection = chooseGate();
    gateRevealedByHost = reveal(gates, firstUserSelection)
    predictNotSwitch += product(gates, firstUserSelection, gateRevealedByHost, False)
    
    
# print("Switch: {0}, Not Switch: {1}".format(predictSwitch, predictNotSwitch))
print("Switch Count: {0}, Switch Probability: {1}".format(predictSwitch, predictSwitch/times))
print("Not Switch Count: {0}, Not Switch Probability: {1}".format(predictNotSwitch, predictNotSwitch/times))