from collections import deque

def valid(lm, lc, rm, rc):
    if lm >= 0 and rm >= 0 and lc >= 0 and rc >= 0:
        if (lm == 0 or lm >= lc) and (rm == 0 or rm >= rc):
            return True
    return False

def mc(m, c, b):
    start_state = (m, c, 0, 0, 1)  
    goal_state = (0, 0, m, c, 0)  
   
    queue = deque([(start_state, [])])
    visited = set([start_state])
   
    possible_moves = [(i, j) for i in range(b + 1) for j in range(b + 1) if 1 <= i + j <= b]
   
    while queue:
        (lm, lc, rm, rc, boat_pos), path = queue.popleft()

        if (lm, lc, rm, rc, boat_pos) == goal_state:
            return path + [(lm, lc, rm, rc, boat_pos)]


        for mm, cm in possible_moves:
            if boat_pos == 1:  
                new = (lm - mm, lc - cm, rm + mm, rc + cm, 0)
            else:  
                new = (lm + mm, lc + cm, rm - mm, rc - cm, 1)
           
            if valid(new[0], new[1], new[2], new[3]) and new not in visited:
                visited.add(new)
                queue.append((new, path + [(lm, lc, rm, rc, boat_pos)]))
   
    return None  # No solution found

# Input validation
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")

# Main part of the program
lm = get_positive_integer("Enter the number of missionaries: ")
lc = get_positive_integer("Enter the number of cannibals: ")
b = get_positive_integer("Enter the boat capacity: ")

# Find the solution
p = mc(lm, lc, b)

if p is not None:
    # Initial state
    print([lm, lc, 1], [0, 0, 0])
   
    for i in range(1, len(p)):
        lmp, lcp, rmp, rcp, boat_pos = p[i-1]
        lmc, lcc, rmc, rcc, boat_pos = p[i]

        if boat_pos == 1:
            # Moving from right to left
            print(f"step{i}:  From Right to left {abs(rmc - rmp)} Missionaries and {abs(rcc - rcp)} Cannibals moved")
            print(f"[{lmc}M, {lcc}C, 1B] --- [{rmc}M, {rcc}C, 0B]")
        else:
            # Moving from left to right
            print(f"step{i}:  From left to right {abs(lmc - lmp)} Missonaries and {abs(lcc - lcp)} Cannibals moved")
            print(f"[{lmc}M, {lcc}C, 0B] --- [{rmc}M, {rcc}C, 1B]")
else:
    print("Not possible")
