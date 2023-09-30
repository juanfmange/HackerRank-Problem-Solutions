arr = [1,1,0,-1,-1]
p = 0
n = 0
z = 0
for i in arr:
    
    if i == 0:
        print("zero")
        z = z + 1
    elif i >= 1:
        print("positivo")
        p =  p + 1
    elif i < 0:
        print("negativo")
        n = n + 1
    print(i)
print(p,n,z)
    
print(p / len(arr))
print("{:.6f}".format(p / len(arr)))

def plus_minus(arr):
    for i in arr:
        if i == 0:
            z =+ 1
        elif i >= 1:
            p =+ 1
        elif i < 0:
            n =+ 1
    positive = "{:.6f}".format(p / len(arr))
    negative = "{:.6f}".format(n / len(arr))
    zero = "{:.6f}".format(z / len(arr))
    return positive, negative, zero

plus = plus_minus(arr)
print(plus)