"""
Este código está inspirado en la solución Merge Sort encontrada para resolver este problema.
https://www.geeksforgeeks.org/inversion-count-in-Aay-using-merge-sort/
"""

# Función para contar las inversiones al fusionar
def countAndMerge(A, l, m, r):
    
    # Tamaño de los subarreglos
    n1 = m - l + 1
    n2 = r - m

    # Subarreglos
    left = A[l:m + 1]
    right = A[m + 1:r + 1]

    res = 0
    i = 0
    j = 0
    k = l

    # Se combinan los subarreglos y se cuentan las inversiones
    while i < n1 and j < n2:

        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
            res += (n1 - i) # Si hay inversión, todas siguientes también son inversiones
        k += 1

    # Se forma el nuevo arreglo con las inversiones hechas
    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1

    return res

# Función recursiva para conteo de inversiones
def countInv(A, l, r):
    res = 0
    if l < r:
        # Divide el arreglo a la mitad
        m = (r + l) // 2

        # Inversiones de la primera mitad
        res += countInv(A, l, m)

        # Inversiones de la segunda mitad
        res += countInv(A, m + 1, r)

        # Inversiones cruzadas
        res += countAndMerge(A, l, m, r)
    return res

# Conteo de inversiones en total
def inversionCount(A):
    return countInv(A, 0, len(A) - 1)

if __name__ == "__main__":
    A = [1, 2, 4, 3]
    print(f"Cantidad de inversiones necesarias: {inversionCount(A)}")

