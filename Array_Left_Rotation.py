def mover_izquierda(arreglo, pasos):
    pasos = pasos % len(arreglo)  # Asegurarse de que los pasos estén dentro del rango de la longitud del arreglo
    arreglo[:] = arreglo[pasos:] + arreglo[:pasos]  # Realizar la rotación

# Ejemplo de uso
mi_arreglo = [1, 2, 3, 4, 5]
pasos_a_la_izquierda = 4

mover_izquierda(mi_arreglo, pasos_a_la_izquierda)
print(mi_arreglo)
