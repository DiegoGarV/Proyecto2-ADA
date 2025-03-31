"""
Este código está inspirado en la solución Merge Sort encontrada para resolver este problema.
https://www.geeksforgeeks.org/inversion-count-in-Aay-using-merge-sort/
"""

import time
import matplotlib.pyplot as plt

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

# Función para leer los aarrays de prueba
def read_arrays_from_file(filename):
    arrays = []
    with open(filename, 'r') as file:
        for line in file:
            array = list(map(int, line.strip().split()))
            arrays.append(array)
    return arrays

# Función para calcular los tiempos de ejecución de cada arreglo
def measure_execution_times(arrays):
    times = []
    n=1
    for arr in arrays:
        start_time = time.perf_counter()
        inversionCount(arr.copy())  # Usamos una copia para no modificar el original
        elapsed_time = (time.perf_counter() - start_time) * 1e6
        print(f"{n}.) Inversiones de {arr}: {inversionCount(arr.copy())} - Tiempo: {elapsed_time:.2f} µs - Tamaño: {len(arr)}")
        times.append(elapsed_time)
        n+=1
    return times

# Función para graficar los resultados
def plot_results(arrays, times):
    plt.figure(figsize=(12, 6))
    x_labels = [f"Array {i+1}" for i in range(len(arrays))]

    plt.plot(range(len(arrays)), times, marker='o', linestyle='-', color='b', label='Tiempo de ejecución')

    plt.xticks(range(len(arrays)), x_labels, rotation=45, ha='right')  # Rotamos para mejor visibilidad
    plt.xlabel('Arreglos de prueba')
    plt.ylabel('Tiempo de ejecución (µs)')
    plt.title('Tiempo de ejecución por arreglo')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    filename = "pruebas.txt"
    arrays = read_arrays_from_file(filename)
    times = measure_execution_times(arrays)
    plot_results(arrays, times)