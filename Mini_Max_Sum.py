"""arr = [1,2,3,4,5]
def mini_max_sum(arr):
    max_len = arr[len(arr) -4 :]
    min_len = arr[:len(arr) -1]
    print(sum(min_len), sum(max_len))
    #print(min_len, max_len)

print(mini_max_sum(arr))"""

"""
- Tomar del arreglo cada valor
- restar 



"""

def eliminar_elementos(list):
    result = []
    suma = []
    for i in range(len(list)):
        new = list[:i] + list[i+1:]
        result.append(new)
        for lista in result:
            res = sum(lista)
            suma.append(res)
    maximus = max(suma)
    minimus = min(suma)
    print(minimus, maximus)
    




list = [1,2,3,4,5]
print(eliminar_elementos(list))
    
