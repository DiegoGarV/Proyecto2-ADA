import time
import matplotlib.pyplot as plt


# Definimos la clase del árbol de Fenwick (Binary Indexed Tree)
class FenwickTree:
    def __init__(self, size):
        # Inicializamos el árbol con ceros, de tamaño (size + 1) porque usamos índices 1-based
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        # Incrementamos el índice porque el árbol usa índices 1-based
        index += 1
        while index < len(self.tree):
            # Sumamos el valor a la posición correspondiente
            self.tree[index] += value
            # Nos movemos al siguiente índice afectado
            index += index & -index

    def query(self, index):
        # Convertimos a índice 1-based
        index += 1
        result = 0
        # Sumamos todos los valores acumulados hasta ese índice
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


# Función principal que cuenta inversiones usando programación dinámica
def inversionCountDP(arr):
    if not arr:
        return 0

    # Discretizamos los valores del arreglo, para convertirlos en índices pequeños
    sorted_unique = sorted(set(arr))
    value_to_index = {val: idx for idx, val in enumerate(sorted_unique)}

    # Inicializamos el árbol de Fenwick con la cantidad de valores únicos
    tree = FenwickTree(len(sorted_unique))
    inversions = 0

    # Recorremos el arreglo de derecha a izquierda (bottom-up)
    for num in reversed(arr):
        idx = value_to_index[num]
        # Consultamos cuántos valores menores ya hemos visto (inversiones)
        inversions += tree.query(idx - 1)
        # Registramos el valor actual como "visto"
        tree.update(idx, 1)

    return inversions


# Lee los arreglos desde un archivo de texto línea por línea
def read_arrays_from_file(filename):
    arrays = []
    with open(filename, "r") as file:
        for line in file:
            # Convierte cada línea en una lista de enteros
            array = list(map(int, line.strip().split()))
            arrays.append(array)
    return arrays


# Mide el tiempo de ejecución del algoritmo para cada arreglo
def measure_execution_times(arrays):
    times = []
    for arr in arrays:
        start_time = time.perf_counter()
        # Ejecutamos el algoritmo sobre una copia del arreglo
        inversionCountDP(arr.copy())
        elapsed_time = (time.perf_counter() - start_time) * 1e6
        print(
            f"Inversiones de {arr}: {inversionCountDP(arr.copy())} - Tiempo: {elapsed_time:.2f} µs"
        )
        times.append(elapsed_time)
    return times


def plot_results(arrays, times):
    plt.figure(figsize=(12, 6))
    x_labels = [f"Array {i+1}" for i in range(len(arrays))]

    plt.plot(
        range(len(arrays)),
        times,
        marker="o",
        linestyle="-",
        color="g",
        label="Tiempo de ejecución (DP)",
    )

    plt.xticks(range(len(arrays)), x_labels, rotation=45, ha="right")
    plt.xlabel("Arreglos de prueba")
    plt.ylabel("Tiempo de ejecución (µs)")
    plt.title("Tiempo de ejecución por arreglo - Programación Dinámica")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    filename = "pruebas.txt"
    arrays = read_arrays_from_file(filename)
    times = measure_execution_times(arrays)
    plot_results(arrays, times)
