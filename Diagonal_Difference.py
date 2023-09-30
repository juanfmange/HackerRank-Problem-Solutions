"""
Dada una matriz , calcular la diferencia (resta) absoluta entre las diagonales de esta.
"""

arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

def diagonalDifference(arr):
    sum1 = 0 #Variables para almacenar el valor de la suma de las diagonales
    sum2 = 0
    for i in range(len(arr)): #recorro la matriz
        sum1 += arr[i][i] # Sumo la diagonal principal
        sum2 += arr[i][len(arr)-i-1] # sumo la diagonal secundaria de la matriz
    return abs(sum1-sum2) #diferencia absoluta de los valores

print(diagonalDifference(arr))
