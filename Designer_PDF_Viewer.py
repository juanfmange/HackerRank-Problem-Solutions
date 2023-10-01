def calcular_mm(h, word):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Inicializar un diccionario vacio
    index = {}
    arr = []
    comparacion = []

    # Usar un bucle for para agregar las claves y valores al diccionario
    for letra, numero in zip(alfabeto, h):
        index[letra] = numero

    # Itero el string "w" para crear un arreglo con cada letra de la cadena     
    for i in word:
        arr.append(i)

    # Valido que la clave del arreglo arr para recuperar los caracteres de mi string esten en el diccionario y poder sacar su valor correspondiente   
    for clave in index:
        if clave in arr:
            comparacion.append(index[clave])

    mm = max(comparacion) * len(word)

    return mm

# Ejemplo de uso:
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
w = 'hola'
resultado = calcular_mm(h, w)
print(resultado)
