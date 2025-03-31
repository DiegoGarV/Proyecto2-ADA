import time
import matplotlib.pyplot as plt


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        index += 1  # Convertir a índice 1-based
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1  # Convertir a índice 1-based
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


def inversionCountDP(arr):
    if not arr:
        return 0

    # Discretización: convertir los valores a índices únicos
    sorted_unique = sorted(set(arr))
    value_to_index = {val: idx for idx, val in enumerate(sorted_unique)}

    tree = FenwickTree(len(sorted_unique))
    inversions = 0

    for num in reversed(arr):
        idx = value_to_index[num]
        inversions += tree.query(idx - 1)
        tree.update(idx, 1)

    return inversions


def read_arrays_from_file(filename):
    arrays = []
    with open(filename, "r") as file:
        for line in file:
            array = list(map(int, line.strip().split()))
            arrays.append(array)
    return arrays


def measure_execution_times(arrays):
    times = []
    for arr in arrays:
        start_time = time.perf_counter()
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
