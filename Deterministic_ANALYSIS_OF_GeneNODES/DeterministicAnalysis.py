import numpy
import sys

#Exhaustive Statues, depends onthe number of inputs
def genbin(n):
    states = list()
    for i in range(1<<n):
        s = bin(i)[2:]
        s = '0' * (n-len(s)) + s
        state = list(map(int,list(s)))
        
        if state not in states:
            states.append(state)

    return states

states =  genbin(6)
states = numpy.array(states)

changeStates = numpy.copy(states)
print(changeStates.shape)
# You can use your own values for weights in your case
W = [
    [0, 0.25, 0, 0.25, 0, 0.25],
    [0.5, 0, 0.5, 0, 0.5, 0],
    [0, 0.5, 0, -0.1, 0, -0.1],
    [0.25, 0, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0.5, 0],
    [0, 0.5, 0, -0.1, 0, -0.1]
]

W = numpy.array(W)
# You can use your own values here
bA = [0.5, 0.75, 0.1, 0.1, 0.75, 0.1]
bA = numpy.array(bA)
bA = bA[numpy.newaxis, :]
bA.shape

previousUpdateFun = numpy.zeros((16,4))
T = 0

while True:
    print('>> T=',T,'\n',states)
    print()
    newUpdateFun = numpy.dot(changeStates, W) 
    newUpdateFun = numpy.add(newUpdateFun, bA)
    print('newUpdateFun\n', newUpdateFun)
    
    if (numpy.array_equal(previousUpdateFun, newUpdateFun)==True):
        print('Previous and Current update function is equal')
        print("")
        break
        
    changeStates[newUpdateFun>0] = 1
    changeStates[newUpdateFun<0] = 0
    states = changeStates

    previousUpdateFun = newUpdateFun.copy()
    T = T+1
    print()
   
