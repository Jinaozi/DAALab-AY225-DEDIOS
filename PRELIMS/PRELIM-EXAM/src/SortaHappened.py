import csv
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

file_path = ""
cancel_sort = False
sort_thread = None
total_rows = 0

# ---------- SORTING ALGORITHMS ----------
def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        if cancel_sort:
            return
        for j in range(0, n - i - 1):
            if cancel_sort:
                return
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr, key):
    n = len(arr)
    for i in range(1, n):
        if cancel_sort:
            return
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current[key]:
            if cancel_sort:
                return
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def merge_sort(arr, key):
    if cancel_sort or len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if cancel_sort:
            return []
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---------- LOAD CSV ----------
def load_csv(file_path, n):
    data = []
    with open(file_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= n:
                break
            row["ID"] = int(row["ID"])
            data.append(row)
    return data

# ---------- GUI FUNCTIONS ----------
def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    file_label.config(text=file_path if file_path else "No file selected")

def cancel_operation():
    global cancel_sort
    cancel_sort = True
    status_label.config(text="Status: Cancelled!", fg="#d32f2f")
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "CANCELLED!\n")
    output_text.config(state=tk.DISABLED)

def run_sort_threaded():
    global sort_thread
    if sort_thread and sort_thread.is_alive():
        return
    sort_thread = threading.Thread(target=run_sort)
    sort_thread.start()

def run_sort():
    global cancel_sort, total_rows
    cancel_sort = False
    status_label.config(text="Sorting...", fg="#000000")

    if not file_path:
        messagebox.showerror("Error", "Please select a CSV file.")
        return

    try:
        total_rows = int(n_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for N.")
        return

    key = column_var.get()
    algo = algo_var.get()

    if algo in ["Bubble Sort", "Insertion Sort"] and total_rows > 10000:
        messagebox.showwarning(
            "Warning",
            "O(n²) algorithm selected. This may take a long time."
        )

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    performance_label.config(text="")

    start_load = time.time()
    data = load_csv(file_path, total_rows)
    end_load = time.time()

    if cancel_sort:
        cancel_operation()
        return

    start_sort = time.time()

    if algo == "Bubble Sort":
        bubble_sort(data, key)
    elif algo == "Insertion Sort":
        insertion_sort(data, key)
    elif algo == "Merge Sort":
        data = merge_sort(data, key)

    end_sort = time.time()

    if cancel_sort:
        cancel_operation()
        return

    status_label.config(text="Status: Done!", fg="#6E302D")

    performance_label.config(
        text=f"Load Time: {end_load - start_load:.4f}s | "
             f"Sort Time: {end_sort - start_sort:.4f}s | "
             f"Total: {(end_sort - start_load):.4f}s"
    )

    output_text.insert(tk.END, f"First 10 sorted values ({key}):\n\n")
    for row in data[:10]:
        output_text.insert(tk.END, f"{row[key]}\n")

    output_text.config(state=tk.DISABLED)

# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("Sorta Happened")
root.geometry("950x650")
root.resizable(False, False)
root.config(bg="#E1D4BE")

font_label = ("Courier New", 12, "bold")
font_button = ("Courier New", 11, "bold")
font_text = ("Courier New", 11)

main_frame = tk.Frame(root, bg="#E1D4BE")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Top frame
top_frame = tk.Frame(main_frame, bg="#E1D4BE", pady=10)
top_frame.pack(fill=tk.X)

# File selection
file_frame = tk.Frame(top_frame, bg="#E1D4BE")
file_frame.pack(fill=tk.X, pady=5)
tk.Button(
    file_frame, text="Select CSV File",
    bg="#6E302D", fg="white",
    font=font_button, command=choose_file, width=16
).pack(side=tk.LEFT, padx=10)

file_label = tk.Label(
    file_frame, text="No file selected",
    bg="#E1D4BE", fg="#665F54", font=font_label
)
file_label.pack(side=tk.LEFT, padx=10)

# Options
options_frame = tk.Frame(top_frame, bg="#E1D4BE")
options_frame.pack(fill=tk.X, pady=5)

tk.Label(options_frame, text="Column:", bg="#E1D4BE",
         fg="#665F54", font=font_label).pack(side=tk.LEFT, padx=(10,5))
column_var = tk.StringVar(value="ID")
tk.OptionMenu(options_frame, column_var, "ID", "FirstName", "LastName").pack(side=tk.LEFT)

tk.Label(options_frame, text="Algorithm:", bg="#E1D4BE",
         fg="#665F54", font=font_label).pack(side=tk.LEFT, padx=(20,5))
algo_var = tk.StringVar(value="Merge Sort")
tk.OptionMenu(options_frame, algo_var,
              "Bubble Sort", "Insertion Sort", "Merge Sort").pack(side=tk.LEFT)

tk.Label(options_frame, text="Rows (N):", bg="#E1D4BE",
         fg="#665F54", font=font_label).pack(side=tk.LEFT, padx=(20,5))
n_entry = tk.Entry(options_frame, width=8)
n_entry.pack(side=tk.LEFT)

# Buttons
buttons_frame = tk.Frame(top_frame, bg="#E1D4BE")
buttons_frame.pack(fill=tk.X, pady=5)

tk.Button(
    buttons_frame, text="Run Sort",
    bg="#5E1705", fg="white",
    font=font_button, command=run_sort_threaded, width=16
).pack(side=tk.LEFT, padx=10)

tk.Button(
    buttons_frame, text="Cancel",
    bg="#6E2510", fg="white",
    font=font_button, command=cancel_operation, width=16
).pack(side=tk.LEFT, padx=10)

# Status & Performance
status_frame = tk.Frame(main_frame, bg="#E1D4BE", pady=5)
status_frame.pack(fill=tk.X)

status_label = tk.Label(status_frame, font=font_label, bg="#E1D4BE")
status_label.pack(anchor="center")

performance_label = tk.Label(
    status_frame, text="", font=font_text,
    bg="#E1D4BE", fg="#665F54"
)
performance_label.pack(anchor="center")

# Output
output_frame = tk.Frame(main_frame, bg="#E1D4BE", pady=10, padx=10)
output_frame.pack(fill=tk.BOTH, expand=True)

output_text = tk.Text(
    output_frame, height=12, width=100,
    wrap=tk.NONE, font=font_text,
    fg="#665F54", bg="#FFFBE6"
)
output_text.pack(fill=tk.BOTH, expand=True)
output_text.config(state=tk.DISABLED)

root.mainloop()
