# PathPanda – Multi-Criteria Route Optimizer

**Program Type:** Web Application (GUI)

PathPanda is a browser-based tool that analyzes transportation networks and determines optimal routes based on **distance, travel time, and fuel consumption**.
It allows users to upload a dataset of routes and automatically computes the **best starting node and shortest paths** using graph algorithms.

---

## Features

* Upload route data using **Excel (.xlsx, .xls) or CSV**
* Automatic **shortest path analysis**
* Calculates optimal routes for:

  * 📏 Shortest Distance
  * ⚡ Fastest Time
  * ⛽ Lowest Fuel Consumption
* Identifies the **best overall starting node**
* Displays **node rankings**
* Interactive **network graph visualization**
* Shows **alternative routes** for each destination

---

## Technologies Used

* **HTML**
* **CSS**
* **JavaScript**
* **XLSX.js** (for reading Excel files)
* **Dijkstra’s Algorithm** for shortest path computation


---

## How to Run

1. Download or clone the repository.
2. Open `PathPanda.html` in any modern web browser.
3. Upload a dataset file (`.xlsx`, `.xls`, or `.csv`).
4. Click **Auto-Analyze All Nodes**.
5. View the generated route analysis and graph visualization.

---

## Dataset Format

The input file must contain the following columns:

| From   | To     | Distance (km) | Time (mins) | Fuel (L) |
| ------ | ------ | ------------- | ----------- | -------- |
| IMUS   | BACOOR | 10            | 15          | 1.2      |
| BACOOR | DASMA  | 12            | 25          | 1.5      |
| DASMA  | KAWIT  | 12            | 25          | 1.5      |

---

## Algorithm

The system uses **Dijkstra’s Algorithm** to compute the shortest paths between nodes based on three metrics:

* Distance
* Time
* Fuel Consumption

Each node is evaluated as a possible starting point, and the system selects the **best overall node based on the lowest combined score**.

---

## Output

The application generates:

* 🏆 **Best Overall Starting Node**
* 📊 **Node Rankings**
* 📏 **Shortest Distance Routes**
* ⚡ **Fastest Routes**
* ⛽ **Lowest Fuel Consumption Routes**
* 🗺️ **Interactive Graph Visualization**
