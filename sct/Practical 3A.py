import numpy as np
x1 = np.array([1, 1, 1, -1, 1, -1, 1, 1, 1]) 
x2 = np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])   
b = 0  
y = np.array([1, -1])  
wtold = np.zeros(9)
wtnew = np.zeros(9)
wtnew = wtnew.astype(int)
wtold = wtold.astype(int)
eta = 1
print("First input with target=1")
for i in range(9):
    wtold[i] = wtold[i] + eta * x1[i] * y[0]  
b = b + eta * y[0] 
wtnew = wtold  
print("New weights:", wtnew)
print("Bias value:", b)
print("Second input with target=-1")
for i in range(9):
    wtold[i] = wtold[i] + eta * x2[i] * y[1]  
b = b + eta * y[1]  
wtnew = wtold 
print("New weights:", wtnew)
print("Bias value:", b)
