from itertools import permutations
from math import factorial  # To calculate (n - 1)!

def calculate_cost(graph, path):
    cost = 0
    n = len(graph)
    for i in range(n):
        cost += graph[path[i] - 1][path[(i + 1) % n] - 1]
    return cost

def tsp_all_paths(graph, start_city):
    n = len(graph)
    cities = list(range(1, n + 1))
    cities.remove(start_city)
    
    total_paths = factorial(n - 1)  # (n - 1)!
    print(f"Total number of paths: {total_paths}\n")

    all_permutations = permutations(cities)
    
    paths_and_costs = []
    min_cost = float('inf')

    # Loop through all permutations and calculate the cost for each path
    for perm in all_permutations:
        path = [start_city] + list(perm) + [start_city]
        cost = calculate_cost(graph, path)
        paths_and_costs.append((path, cost))
        if cost < min_cost:
            min_cost = cost

    # Display all paths with their costs
    print("All possible paths with their costs:")
    path_number = 1
    for path, cost in paths_and_costs:
        path_str = " -> ".join(map(str, path))
        if cost == min_cost:
            print(f" **Path {path_number}: {path_str}, Cost: {cost}")
        else:
            print(f"Path {path_number}: {path_str}, Cost: {cost}")
        path_number += 1

    # Display shortest path(s) with stars
    print("\nShortest path(s):")
    path_number = 1
    for path, cost in paths_and_costs:
        if cost == min_cost:
            shortest_path_str = " -> ".join(map(str, path))
            print(f"Path {path_number}: {shortest_path_str}, Cost: {cost}")
        path_number += 1

def get_graph():
    while True:
        n = input("Enter the number of cities: ")
        if n.isdigit() and int(n) > 1:
            n = int(n)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    graph = []
    print("Enter the distance matrix (each row separated by a newline):")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1} (for city {i + 1}): ").split()))
                if len(row) != n:
                    raise ValueError
                if any(x < 0 for x in row):
                    raise ValueError
                graph.append(row)
                break
            except ValueError:
                print(f"Invalid input for row {i + 1}. Please enter {n} non-negative integers.")

    return graph

if __name__ == "__main__":
    graph = get_graph()
    while True:
        try:
            start_city = int(input(f"Enter the starting city (1 to {len(graph)}): "))
            if start_city < 1 or start_city > len(graph):
                raise ValueError
            break
        except ValueError:
            print(f"Invalid input. Please enter an integer between 1 and {len(graph)}.")
    tsp_all_paths(graph, start_city)
