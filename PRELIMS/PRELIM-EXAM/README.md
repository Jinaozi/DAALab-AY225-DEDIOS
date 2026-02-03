# Sorting Algorithm Stress Test

## Overview

The **Sorta Happemed** is a Python-based benchmarking application that evaluates the performance of three classic sorting algorithms using structured CSV datasets. The CSV file contains the columns **ID**, **FirstName**, and **LastName**.

This project demonstrates the real-world performance difference between **O(n²)** algorithms (Bubble Sort and Insertion Sort) and the **O(n log n)** Merge Sort, reinforcing key concepts in algorithm analysis. The application provides a clean graphical interface for testing scalability and measuring execution time.

---

## Features

* **Column Selection:** Sort by `ID`, `FirstName`, or `LastName`
* **Sorting Algorithm Selection:** Bubble Sort, Insertion Sort, Merge Sort
* **Cancel Sorting:** Allows users to instantly stop long-running sorts
* **Performance Metrics:** Measures load time, sort time, and total execution time
* **Output Display:** Shows the first 10 rows of sorted results in a scrollable text box
* **GUI-Based:** Built using Tkinter (no external libraries required)

---

## Usage

1. **Open the project in VS Code**

   * Ensure `sorting_gui.py` and the CSV file are in the same project directory.

2. **Select Python Interpreter**

   * Press `Ctrl + Shift + P`
   * Type **Python: Select Interpreter**
   * Choose Python 3.x

3. **Run the GUI**

   * Press `F5` or right-click `sorting_gui.py` → **Run Python File in Terminal**

4. **Select CSV File**

   * Click **Select CSV File**
   * Choose the CSV file to benchmark

5. **Select Column**

   * Choose `ID`, `FirstName`, or `LastName`

6. **Select Algorithm**

   * Choose Bubble Sort, Insertion Sort, or Merge Sort

7. **Set Row Limit (N)**

   * Enter the number of rows to sort (e.g., 1,000; 10,000; 100,000)

8. **Run Sort**

   * Click **Run Sort**
   * Observe the progress bar and percentage indicator

9. **Cancel Sort (Optional)**

   * Click **Cancel** to immediately stop execution
   * The output box will display **CANCELLED!**

10. **View Results**

    * The first 10 sorted values are displayed
    * Performance metrics appear below the status label

---

## Notes

* All sorting algorithms are implemented **from scratch**
* No built-in sorting functions such as `.sort()` or `sorted()` are used
* Bubble Sort and Insertion Sort may take a very long time for large datasets

---

## Conclusion

The benchmarking results clearly confirm theoretical time complexities:

* **Bubble Sort** and **Insertion Sort** scale poorly due to their **O(n²)** complexity.
* **Merge Sort** remains efficient even at large input sizes, validating its **O(n log n)** complexity.
* This experiment demonstrates why modern applications rely on divide-and-conquer algorithms for large datasets.
