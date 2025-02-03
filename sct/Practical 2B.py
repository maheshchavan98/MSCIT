print("\nXOR function using McClloch-Pitts")
x1inputs = [1,1,0,0]
x2inputs = [1,0,1,0]
print("Calculating z1 = x1w11 + x2w12")
print("Considering one weight as exciatatory and other as inhibitory ")
w11 = [1,1,1,1]
w12 = [-1,-1,-1,-1]
print("x1","x2","z1")
z1 = []
for i in range(0,4):
    z1.append(x1inputs[i]*w11[i] + x2inputs[i]*w12[i])
    print(x1inputs[i]," ",x2inputs[i]," ",z1[i])
print("\nCalculating z1 = x1w21 + x2w22")
print("Considering one weight as exciatatory and other as inhibitory ")
w21 = [-1,-1,-1,-1]
w22 = [1,1,1,1]
print("x1","x2","z2")
z2 = []
for i in range(0,4):
    z2.append(x1inputs[i]*w21[i] + x2inputs[i]*w22[i])
    print(x1inputs[i]," ",x2inputs[i]," ",z2[i])
print("\nApplying Threshold = 1 for z1 and z2")
for i in range(0,4):
    if(z1[i]>=1):
        z1[i] = 1
    else:
        z1[i] = 0
    if(z2[i]>=1):
        z2[i]=1
    else:
        z2[i]=0
print("z1","z2")
for i in range(0,4):
    print(z1[i]," ",z2[i]," ")
print("x1" , "x2" , "yin")
yin = []
v1 = 1
v2 = 1
for i in range(0,4):
    yin.append(z1[i]*v1 + z2[i]*v2)
    print(x1inputs[i]," ",x2inputs[i]," ",yin[i])
y=[]
for i in range(0,4):
    if(yin[i]>=1):
        y.append(1)
    else:
        y.append(0)
print("x1","x2","y")
for i in range(0,4):
    print(x1inputs[i]," ",x2inputs[i]," ",y[i])