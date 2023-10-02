def calcular_mediana(arreglo):
    arreglo_ordenado = sorted(arreglo)
    n = len(arreglo_ordenado)
    
    if n % 2 == 1:
        # Si la longitud del arreglo es impar, la mediana es el elemento en el medio.
        mediana = arreglo_ordenado[n // 2]
    else:
        # Si la longitud del arreglo es par, la mediana es el promedio de los dos elementos del medio.
        mediana = (arreglo_ordenado[(n // 2) - 1] + arreglo_ordenado[n // 2]) / 2
    
    return mediana

arreglo = [1,2,3,4,5,6,7]
print(calcular_mediana(arreglo))