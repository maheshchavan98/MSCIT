num_ip = int(input("Enter the number of inputs: "))
w1 = 1
w2 = -1

print("For the", num_ip, "inputs, calculate the net input using net input formula")
x1 = []
x2 = []
for j in range(num_ip):
    element1 = int(input("X1 = "))
    element2 = int(input("X2 = "))
    x1.append(element1)
    x2.append(element2)

print("X1 =", x1)
print("X2 =", x2)

n = [element * w1 for element in x1]
m = [element * w2 for element in x2]

Yin_sum = [n[i] + m[i] for i in range(num_ip)]  # Sum of weighted inputs
Yin_diff = [n[i] - m[i] for i in range(num_ip)]  # Difference of weighted inputs

print("Yin (Sum) =", Yin_sum)
print("After assuming one weight as excitatory and the other as inhibitory, Yin (Difference) =", Yin_diff)

Y = []
for i in range(num_ip):
    if Yin_sum[i] >= 1:
        
        Y.append(1)
    else:
        
        Y.append(0)

print("Y =", Y)
