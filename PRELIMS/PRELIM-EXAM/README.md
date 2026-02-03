Sorting Algorithm Stress Test GUI
Overview

The Sorting Algorithm Stress Test GUI is a Python-based benchmarking application that evaluates the performance of three classic sorting algorithms using structured CSV datasets. The CSV file contains the columns ID, FirstName, and LastName.

This project demonstrates the real-world performance difference between O(n²) algorithms (Bubble Sort and Insertion Sort) and the O(n log n) Merge Sort, reinforcing key concepts in algorithm analysis. The application provides a clean graphical interface for testing scalability and measuring execution time.

Features

Column Selection: Sort by ID, FirstName, or LastName

Sorting Algorithm Selection: Bubble Sort, Insertion Sort, Merge Sort

Progress Bar: Displays live sorting progress with percentage

Cancel Sorting: Allows users to instantly stop long-running sorts

Performance Metrics: Measures load time, sort time, and total execution time

Output Display: Shows the first 10 rows of sorted results in a scrollable text box

GUI-Based: Built using Tkinter (no external libraries required)

Requirements

Python 3.x

Standard Python libraries only:

tkinter

csv

time

threading

No additional packages are required

Usage

Open the project in VS Code

Ensure sorting_gui.py and the CSV file are in the same project directory.

Select Python Interpreter

Press Ctrl + Shift + P

Type Python: Select Interpreter

Choose Python 3.x

Run the GUI

Press F5 or right-click sorting_gui.py → Run Python File in Terminal

Select CSV File

Click Select CSV File

Choose the CSV file to benchmark

Select Column

Choose ID, FirstName, or LastName

Select Algorithm

Choose Bubble Sort, Insertion Sort, or Merge Sort

Set Row Limit (N)

Enter the number of rows to sort (e.g., 1,000; 10,000; 100,000)

Run Sort

Click Run Sort

Observe the progress bar and percentage indicator

Cancel Sort (Optional)

Click Cancel to immediately stop execution

The output box will display CANCELLED!

View Results

The first 10 sorted values are displayed

Performance metrics appear below the status label

Notes

All sorting algorithms are implemented from scratch

No built-in sorting functions such as .sort() or sorted() are used

Bubble Sort and Insertion Sort may take a very long time for large datasets

The progress bar and cancel function help manage long executions
