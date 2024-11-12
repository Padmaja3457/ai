from collections import deque

def checkinput(prom):
    """Prompts the user for a positive integer and validates the input."""
    while True:
        try:
            j = int(input(prom))
            if j < 0:
                print("Volume cannot be negative. Enter a positive integer.")
            elif j == 0:
                print("Volume cannot be 0. Enter a valid input.")
            else:
                return j
        except ValueError:
            print("Invalid input format.")

# Action mapping for each rule
action_list = {
    1: "Fill jug 1",
    2: "Empty jug 1",
    3: "Fill jug 2",
    4: "Empty jug 2",
    5: "Pour water from jug 2 into jug 1",
    6: "Pour water from jug 1 into jug 2",
    7: "Pour water from jug 2 into jug 1 until jug 1 is full",
    8: "Pour water from jug 1 into jug 2 until jug 2 is full"
}

def get_possible_moves(j1_current, j2_current, j1_capacity, j2_capacity):
    possible_moves = []

    # Rule 1: Fill 5 Lt. jug (Jug 1)
    if j1_current < j1_capacity:
        possible_moves.append((j1_capacity, j2_current, 1))

    # Rule 2: Empty 5 Lt. jug (Jug 1)
    if j1_current > 0:
        possible_moves.append((0, j2_current, 2))

    # Rule 3: Fill 3 Lt. jug (Jug 2)
    if j2_current < j2_capacity:
        possible_moves.append((j1_current, j2_capacity, 3))

    # Rule 4: Empty 3 Lt. jug (Jug 2)
    if j2_current > 0:
        possible_moves.append((j1_current, 0, 4))

    # Rule 5: Pour from Jug 2 into Jug 1 until Jug 1 is full
    if j1_current + j2_current <= j1_capacity and j2_current > 0:
        possible_moves.append((j1_current + j2_current, 0, 5))

    # Rule 6: Pour from Jug 1 into Jug 2 until Jug 2 is full
    if j1_current + j2_current <= j2_capacity and j1_current > 0:
        possible_moves.append((0, j1_current + j2_current, 6))

    # Rule 7: Pour from Jug 2 into Jug 1 until Jug 1 is full
    if j1_current + j2_current >= j1_capacity and j2_current > 0:
        possible_moves.append((j1_capacity, j2_current - (j1_capacity - j1_current), 7))

    # Rule 8: Pour from Jug 1 into Jug 2 until Jug 2 is full
    if j1_current + j2_current >= j2_capacity and j1_current > 0:
        possible_moves.append((j1_current - (j2_capacity - j2_current), j2_capacity, 8))

    return possible_moves

def water_jug(j1_capacity, j2_capacity, target):
    """Solves the water jug problem using breadth-first search."""
    queue = deque()
    visited_set = set()
    start = (0, 0)
    queue.append((start, []))
    visited_set.add(start)

    while queue:
        (j1_current, j2_current), path = queue.popleft()
        path = path + [(j1_current, j2_current)]

        if j1_current == target or j2_current == target:
            print("Solution path:")
            for i in range(len(path) - 1):
                current = path[i]
                next_state = path[i + 1]
                
                # Get the action corresponding to the move
                for move in get_possible_moves(current[0], current[1], j1_capacity, j2_capacity):
                    if move[0] == next_state[0] and move[1] == next_state[1]:
                        print(f"{action_list[move[2]]}: {next_state}")

            print(f"Final path: {path}")
            if j1_current == target:
                print(f"Solution found: Jug 1 contains the target volume of {target} liters.")
            elif j2_current == target:
                print(f"Solution found: Jug 2 contains the target volume of {target} liters.")

            return

        for move in get_possible_moves(j1_current, j2_current, j1_capacity, j2_capacity):
            if (move[0], move[1]) not in visited_set:
                visited_set.add((move[0], move[1]))
                queue.append(((move[0], move[1]), path))

    print("No solution found.")

def check(j1, j2, t):
    """Checks if the target volume can be measured using the given jugs."""
    if t > j1 and t > j2:
        print("Not Possible: Both jugs are smaller than the target.")
        return True
    return False

# Input capacities and target volume
j1 = checkinput("Enter Capacity of Jug 1: ")
j2 = checkinput("Enter Capacity of Jug 2: ")
t = checkinput("Enter Target Volume: ")

if check(j1, j2, t):
    print("Solution is not possible.")
else:
    water_jug(j1, j2, t)
