import numpy as np
x=np.zeros ((3,))
weights=np.zeros((3,))
desired=np.zeros((3,))
actual=np.zeros((3,))
for i in range(0,3):
        x[i]=float(input("Intial inputs:"))
for i in range(0,3):
        weights[i]=float(input("Intial weights:"))
for i in range(0,3):
    desired[i]=float(input("Intial desired:"))
a=float(input("Enter learning rate:"))
actual=x*weights
print("Actual initial",actual)
print("Actual desired",desired)
while True:
        if np.array_equal(desired,actual):
            break
        else:
            for i in range(0,3):
                weights[i]=weights[i]+a*(desired[i]-actual[i])
            actual=x*weights
print("*" * 30)
print("Final output using delta rule")
print("Corrected weights",weights)
print("actual",actual)
print("desired",desired)
