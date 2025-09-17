import argparse
import csv
import math
import os
import random
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Tuple


Point = Tuple[float, float]
Route = List[int]


def load_points(
    csv_path: Optional[str] = None,
    *,
    num_points: int = 30,
    seed: int = 42,
    min_coord: float = 0.0,
    max_coord: float = 100.0,
) -> List[Point]:
    """Load sensor coordinates from a CSV file or generate random points.

    Expected CSV format: header optional; two numeric columns named x,y or first two columns parsed as floats.
    """
    rng = random.Random(seed)
    points: List[Point] = []

    if csv_path and os.path.exists(csv_path):
        with open(csv_path, "r", newline="") as f:
            reader = csv.reader(f)
            # Try to detect header
            first_row = next(reader, None)
            if first_row is None:
                return points
            def try_parse(row: Sequence[str]) -> Optional[Point]:
                try:
                    x = float(row[0]) if row[0] != "x" else None
                    y = float(row[1]) if row[1] != "y" else None
                    if x is None or y is None:
                        return None
                    return (x, y)
                except Exception:
                    return None

            first_point = try_parse(first_row)
            if first_point is not None:
                points.append(first_point)
            for row in reader:
                if not row:
                    continue
                p = try_parse(row)
                if p is not None:
                    points.append(p)
    else:
        # Generate random points
        for _ in range(num_points):
            x = rng.uniform(min_coord, max_coord)
            y = rng.uniform(min_coord, max_coord)
            points.append((x, y))

    return points


def euclidean_distance(a: Point, b: Point) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.hypot(dx, dy)


def compute_distance_matrix(points: Sequence[Point]) -> List[List[float]]:
    n = len(points)
    dist: List[List[float]] = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(points[i], points[j])
            dist[i][j] = d
            dist[j][i] = d
    return dist


def route_length(route: Sequence[int], dist: Sequence[Sequence[float]], *, return_to_start: bool = True) -> float:
    total = 0.0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]
    if return_to_start and route:
        total += dist[route[-1]][route[0]]
    return total


def random_route(n: int, rng: random.Random) -> Route:
    r = list(range(n))
    rng.shuffle(r)
    return r


def greedy_nearest_neighbor(dist: Sequence[Sequence[float]], start: int = 0) -> Route:
    n = len(dist)
    unvisited = set(range(n))
    route: Route = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda j: dist[current][j])
        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return route


def two_opt_swap(route: Route, i: int, k: int) -> Route:
    # Returns a new route where the segment [i:k] is reversed
    return route[:i] + list(reversed(route[i : k + 1])) + route[k + 1 :]


def simulated_annealing(
    initial_route: Route,
    dist: Sequence[Sequence[float]],
    *,
    initial_temp: float = 100.0,
    cooling_rate: float = 0.995,
    iterations: int = 50000,
    seed: int = 42,
) -> Route:
    rng = random.Random(seed)
    current = list(initial_route)
    best = list(current)
    current_cost = route_length(current, dist)
    best_cost = current_cost
    temp = initial_temp

    n = len(current)
    if n < 4:
        return current

    for _ in range(iterations):
        # Propose a 2-opt neighbor
        i = rng.randrange(1, n - 2)
        k = rng.randrange(i + 1, n - 1)
        candidate = two_opt_swap(current, i, k)

        # Compute delta efficiently by recomputing local change (simple full recompute for clarity)
        candidate_cost = route_length(candidate, dist)
        delta = candidate_cost - current_cost

        if delta < 0 or rng.random() < math.exp(-delta / max(1e-12, temp)):
            current = candidate
            current_cost = candidate_cost
            if candidate_cost < best_cost:
                best = candidate
                best_cost = candidate_cost
        temp *= cooling_rate
        if temp < 1e-6:
            temp = 1e-6
    return best


def plot_routes(
    points: Sequence[Point],
    routes: Sequence[Sequence[int]],
    labels: Sequence[str],
    colors: Optional[Sequence[str]] = None,
    *,
    title: str = "AUV Sensor Visit Routes",
    save_path: Optional[str] = None,
    show: bool = False,
) -> None:

    if colors is None:
        colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    plt.figure(figsize=(8, 6), dpi=120)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.scatter(xs, ys, c="black", s=25, zorder=3, label="Sensors")

    for idx, route in enumerate(routes):
        color = colors[idx % len(colors)]
        path = route + [route[0]] if route else []
        path_x = [points[i][0] for i in path]
        path_y = [points[i][1] for i in path]
        plt.plot(path_x, path_y, "-o", color=color, alpha=0.8, linewidth=1.5, markersize=3, label=labels[idx])

    plt.title(title)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.legend()
    plt.grid(True, linestyle=":", linewidth=0.5)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Optimize AUV routes (TSP) over sensor coordinates.")
    parser.add_argument("--csv", type=str, default=None, help="Path to CSV with columns x,y (optional header)")
    parser.add_argument("--n", type=int, default=30, help="Number of random points if CSV not provided")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--sa-iters", type=int, default=20000, help="Simulated annealing iterations")
    parser.add_argument("--sa-temp", type=float, default=100.0, help="Initial temperature for SA")
    parser.add_argument("--cooling", type=float, default=0.995, help="Cooling rate for SA (0-1)")
    parser.add_argument("--show", action="store_true", help="Display plot window")
    parser.add_argument("--out", type=str, default="task3_routes.png", help="Output plot file path")

    args = parser.parse_args()

    points = load_points(args.csv, num_points=args.n, seed=args.seed)
    if len(points) < 3:
        raise SystemExit("Need at least 3 points to form a route.")

    dist = compute_distance_matrix(points)
    rng = random.Random(args.seed)

    # Routes
    rand_route = random_route(len(points), rng)
    greedy_route = greedy_nearest_neighbor(dist, start=0)
    sa_route = simulated_annealing(
        greedy_route,
        dist,
        initial_temp=args.sa_temp,
        cooling_rate=args.cooling,
        iterations=args.sa_iters,
        seed=args.seed,
    )

    # Distances
    rand_len = route_length(rand_route, dist)
    greedy_len = route_length(greedy_route, dist)
    sa_len = route_length(sa_route, dist)

    print("Route distances (lower is better):")
    print(f"  Random: {rand_len:.2f}")
    print(f"  Greedy: {greedy_len:.2f}")
    print(f"  SA-optimized: {sa_len:.2f}")

    # Plot
    plot_routes(
        points,
        routes=[rand_route, greedy_route, sa_route],
        labels=[f"Random ({rand_len:.0f})", f"Greedy ({greedy_len:.0f})", f"SA ({sa_len:.0f})"],
        title="AUV Swarm Route Optimization (Random vs Greedy vs SA)",
        save_path=args.out,
        show=bool(args.show),
    )
    print(f"Saved plot to: {args.out}")


if __name__ == "__main__":
    main()


