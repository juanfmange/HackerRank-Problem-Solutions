def aVeryBigSum(ar):
    sum = 0 # Valor incial
    for i in range(len(ar)): #bucle que recorre la longitud del arreglo
        sum+=ar[i] #tomamos la longitud del arreglo y almacenamos en la variable sum
    return sum
print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))