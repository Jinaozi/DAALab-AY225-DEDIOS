import time

def bubble_sort_desc(arr):
    start_time = time.time()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr, time.time() - start_time

def load_txt_file(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file if line.strip()]

data = load_txt_file("dataset.txt")
sorted_data, time_taken = bubble_sort_desc(data)

print("Sorted:", sorted_data)
print(f"Time: {time_taken:.6f} seconds")
