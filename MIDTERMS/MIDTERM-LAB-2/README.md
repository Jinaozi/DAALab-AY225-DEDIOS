# PathPanda – Multi-Criteria Route Optimization

**Brief Report and Documentation**

## Introduction

**Program Type:** Web Application (GUI)

PathPanda is a browser-based tool that analyzes transportation networks and determines optimal routes based on **distance, travel time, and fuel consumption**. The system allows users to upload a dataset of routes and automatically compute the **best starting node and shortest paths** using graph algorithms.

The goal of this project is to demonstrate how graph algorithms can be applied to solve real-world routing problems. By analyzing different metrics, the system helps identify the most efficient routes between locations while also visualizing the network structure.

---

# System Features

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

# Technologies Used

* **HTML**
* **CSS**
* **JavaScript**
* **XLSX.js** (for reading Excel files)
* **Dijkstra’s Algorithm** for shortest path computation

---

# Approach

The PathPanda system models the transportation network as a **graph structure**. In this graph:

* **Nodes** represent locations or cities.
* **Edges** represent connections between locations.
* Each edge contains three weights:

  * Distance
  * Travel time
  * Fuel consumption.

When a dataset is uploaded, the system reads the data and converts it into a graph representation. Each node is evaluated as a potential starting point. The program then computes the shortest paths from that node to all other nodes using different optimization metrics.

After performing these calculations, the program determines the total cost from each starting node and compares the results. The node with the lowest combined cost across all metrics is selected as the **best overall starting node**.

---

# Algorithm Used

The primary algorithm used in PathPanda is **Dijkstra’s Algorithm**.

Dijkstra’s algorithm is widely used in graph theory to determine the shortest path between nodes in a weighted graph. It works by selecting the node with the lowest temporary distance and updating the cost of its neighboring nodes until all nodes have been visited.

In PathPanda, the algorithm is executed three separate times using different weights:

* **Distance Optimization** – determines the shortest route in kilometers.
* **Time Optimization** – determines the fastest route in minutes.
* **Fuel Optimization** – determines the most fuel-efficient route.

Each node is evaluated as a possible starting point, and the system selects the **best overall node based on the lowest combined score**.

---

# Dataset Format

The input file must contain the following columns:

| From   | To     | Distance (km) | Time (mins) | Fuel (L) |
| ------ | ------ | ------------- | ----------- | -------- |
| IMUS   | BACOOR | 10            | 15          | 1.2      |
| BACOOR | DASMA  | 12            | 25          | 1.5      |
| DASMA  | KAWIT  | 12            | 25          | 1.5      |

---

# Output

The application generates:

* 🏆 **Best Overall Starting Node**
* 📊 **Node Rankings**
* 📏 **Shortest Distance Routes**
* ⚡ **Fastest Routes**
* ⛽ **Lowest Fuel Consumption Routes**
* 🗺️ **Interactive Graph Visualization**

---

# Challenges Encountered

One of the main challenges during development was handling **multiple optimization metrics simultaneously**. Since the system needed to compute routes based on distance, time, and fuel consumption, the algorithm had to be executed multiple times while managing different weight values.

Another challenge was designing a **clear visualization of the network graph**. As the number of nodes and edges increases, the graph can become difficult to interpret. To address this, the nodes were arranged in a circular layout and route highlighting was implemented to help users easily follow the optimal paths.

Additionally, reading **Excel and CSV files** required careful parsing to ensure the dataset was correctly interpreted and converted into the graph structure used by the algorithm.

---

# Conclusion

PathPanda demonstrates how graph algorithms such as **Dijkstra’s Algorithm** can be applied to real-world route optimization problems. By evaluating routes based on multiple metrics and presenting the results through an interactive interface, the system provides a practical and user-friendly solution for analyzing transportation networks.

The project highlights the importance of algorithms in solving complex pathfinding problems while also emphasizing the role of visualization in improving user understanding of network data.
