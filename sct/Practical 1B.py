import math
inputs=int(input("Enter the no. of input layer neurons="))
print("Enter the input neurons values:")
inputsn=[]
for i in range (0,inputs):
        elements=float(input())
        inputsn.append(elements)
print(inputsn)
print("Enter the weight for input layer neurons:")
weight=[]
for i in range (0,inputs):
        weele=float(input())
        weight.append(weele)
print(weight)
print("Calculating the net input the output nueron")
Yinn=[]
for i in range (0,inputs):
        Yinn.append(inputsn[i]*weight[i])
        Yin=(round(sum(Yinn),3))
print(Yin)
print("The output from the neuron in case of a binary Sigmoidal Acyivation Function")
Y=1/(1+math.exp(-Yin))
print(Y)
print("The output from the neuron in case of a Bipolar Sigmoidal Activation Function")
Y=2/(1+math.exp(-Yin))
print(Y)

