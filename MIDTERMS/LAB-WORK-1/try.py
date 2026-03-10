import heapq

# ── DATA ────────────────────────────────────────────────────────────────────
# [from, to, distance, time, fuel]
edges = [
    (1, 2, 10, 15, 1.2), (1, 6, 10, 15, 1.2),
    (2, 1, 10, 15, 1.2), (2, 3, 12, 25, 1.5),
    (2, 6, 10, 15, 1.2), (2, 5, 12, 25, 1.5),
    (3, 2, 12, 25, 1.5), (3, 4, 12, 25, 1.5),
    (3, 5, 12, 25, 1.5), (3, 6, 10, 25, 1.3),
    (4, 3, 12, 25, 1.5), (4, 5, 14, 25, 1.2),
    (5, 2, 12, 25, 1.5), (5, 3, 12, 25, 1.5),
    (5, 4, 14, 25, 1.2), (5, 6, 10, 25, 1.5),
    (6, 1, 10, 15, 1.2), (6, 2, 10, 15, 1.2),
    (6, 3, 10, 25, 1.3), (6, 5, 10, 25, 1.5),
]

NODES = [1, 2, 3, 4, 5, 6]
METRICS = ["Distance", "Time", "Fuel"]
UNITS   = ["km", "min", "L"]

# ── BUILD GRAPH ──────────────────────────────────────────────────────────────
def build_graph(metric_idx):
    graph = {n: [] for n in NODES}
    for from_, to, d, t, f in edges:
        cost = [d, t, f][metric_idx]
        graph[from_].append((to, cost))
    return graph

# ── DIJKSTRA ─────────────────────────────────────────────────────────────────
def dijkstra(graph, start):
    dist = {n: float('inf') for n in NODES}
    prev = {n: None for n in NODES}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_cost, u = heapq.heappop(pq)
        if curr_cost > dist[u]:
            continue
        for v, cost in graph[u]:
            new_cost = dist[u] + cost
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(pq, (new_cost, v))

    return dist, prev

def get_path(prev, start, end):
    path = []
    cur = end
    while cur is not None:
        path.insert(0, cur)
        cur = prev[cur]
    return path if path[0] == start else None

# ── ANALYZE ALL NODES ────────────────────────────────────────────────────────
def analyze_all():
    results = {}

    for start in NODES:
        results[start] = {
            'paths': {end: {} for end in NODES if end != start},
            'totals': [0.0, 0.0, 0.0]
        }

        for mi in range(3):
            graph = build_graph(mi)
            dist, prev = dijkstra(graph, start)

            for end in NODES:
                if end == start:
                    continue
                results[start]['paths'][end][mi] = {
                    'cost': dist[end],
                    'path': get_path(prev, start, end)
                }
                results[start]['totals'][mi] += dist[end]

    return results

# ── FIND BEST NODES ───────────────────────────────────────────────────────────
def find_bests(results):
    best = {'Distance': None, 'Time': None, 'Fuel': None}
    best_total = {'Distance': float('inf'), 'Time': float('inf'), 'Fuel': float('inf')}

    for node, data in results.items():
        totals = data['totals']
        if totals[0] < best_total['Distance']:
            best_total['Distance'] = totals[0]; best['Distance'] = node
        if totals[1] < best_total['Time']:
            best_total['Time'] = totals[1];     best['Time'] = node
        if totals[2] < best_total['Fuel']:
            best_total['Fuel'] = totals[2];     best['Fuel'] = node

    # Overall: normalize each metric, sum scores, pick lowest
    scores = {n: 0.0 for n in NODES}
    for mi in range(3):
        vals = [results[n]['totals'][mi] for n in NODES]
        min_v, max_v = min(vals), max(vals)
        for n in NODES:
            scores[n] += (results[n]['totals'][mi] - min_v) / (max_v - min_v if max_v != min_v else 1)

    best['Overall'] = min(scores, key=scores.get)
    return best, best_total

# ── PRINT ─────────────────────────────────────────────────────────────────────
def print_report(results, bests, best_totals):
    W = 64

    # FINAL ANSWER FIRST
    print("\n" + "═" * W)
    print("  🏆  FINAL RESULTS — BEST STARTING NODE PER METRIC")
    print("═" * W)
    print(f"  Distance = Node {bests['Distance']}   (lowest total: {best_totals['Distance']:.1f} km)")
    print(f"  Time     = Node {bests['Time']}   (lowest total: {best_totals['Time']:.1f} min)")
    print(f"  Fuel     = Node {bests['Fuel']}   (lowest total: {best_totals['Fuel']:.2f} L)")
    print(f"  Overall  = Node {bests['Overall']}   (best combined score)")
    print("═" * W + "\n")

    print("\n" + "═" * W)
    print("  ⬡  NODE PATHFINDER — SHORTEST PATH ANALYSIS")
    print("═" * W)

    # Per-node breakdown
    for start in NODES:
        data = results[start]
        print(f"\n{'─' * W}")
        print(f"  FROM NODE {start}")
        print(f"{'─' * W}")
        print(f"  {'Destination':<14} {'Route':<24} {'Dist':>7} {'Time':>7} {'Fuel':>7}")
        print(f"  {'─'*12} {'─'*22} {'─'*7} {'─'*7} {'─'*7}")

        for end in NODES:
            if end == start:
                continue
            p = data['paths'][end]
            route_str = " → ".join(str(n) for n in p[0]['path']) if p[0]['path'] else "N/A"
            d  = f"{p[0]['cost']:.1f}km"
            t  = f"{p[1]['cost']:.1f}m"
            f_ = f"{p[2]['cost']:.2f}L"
            print(f"  To Node {end:<5}      {route_str:<24} {d:>7} {t:>7} {f_:>7}")

        td, tt, tf = data['totals']
        print(f"  {'─'*12} {'─'*22} {'─'*7} {'─'*7} {'─'*7}")
        print(f"  {'TOTAL':<14} {'':<24} {td:.1f}km  {tt:.1f}m  {tf:.2f}L")

# ── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    results   = analyze_all()
    bests, best_totals = find_bests(results)
    print_report(results, bests, best_totals)
