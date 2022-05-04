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

states =  genbin(4)
states = numpy.array(states)

changeStates = numpy.copy(states)
changeStates.shape

W = [
    [0, 1, -2, 2],
    [-1, 0, 0, 1],
    [0, 3, 0, -1],
    [2, -1, 2, 0]
]

W = numpy.array(W)
W.shape

bA = [1, 0, 1, 0]
bA = numpy.array(bA)
bA = bA[numpy.newaxis, :]
bA.shape

print('states\n',states)
newUpdateFun = numpy.add(numpy.dot(changeStates, W), bA)
print('\nnewUpdateFun\n', newUpdateFun)

u = 5
c = 0.001

nodeON = numpy.where (newUpdateFun==0, 1-(1-c), numpy.where(newUpdateFun>0, 0.5 + numpy.multiply(0.5, numpy.tanh(numpy.multiply(u, newUpdateFun))), changeStates))
print('\nnodeON\n', nodeON)

nodeOFF = numpy.where(newUpdateFun==0, 1-c, numpy.where(newUpdateFun<0, 0.5 - numpy.multiply(0.5, numpy.tanh(numpy.multiply(u, newUpdateFun))), changeStates))
print('\nnodeOFF\n', nodeOFF)

print('\nMargin Error')
err = numpy.subtract(nodeON, nodeOFF)
print(err)
#Test Case
equation = numpy.multiply(0.5, numpy.tanh(numpy.multiply(u, newUpdateFun)))
changeStates = numpy.where (newUpdateFun==0, 1-(1-c), numpy.where(newUpdateFun>0, 0.5 + equation, changeStates))
print(changeStates)

