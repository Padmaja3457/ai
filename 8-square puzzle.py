import heapq

moves = [(0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left'), (-1, 0, 'up')]

def heuristic(state, goal_state):
    return sum(state[i][j] != goal_state[i][j] and state[i][j] != '_' for i in range(3) for j in range(3))

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def print_board(matrix):
    for row in matrix:
        print(' | '.join(str(num) if num != '_' else " " for num in row))
        print('-' * 9)

def astar(initial_state, goal_state):
    open_list = [(heuristic(initial_state, goal_state), 0, initial_state, [])]
    closed_set = set()

    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)
        if current_state == goal_state:
            return path

        closed_set.add(tuple(map(tuple, current_state)))
        zero_x, zero_y = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == '_')
        for move_x, move_y, move_dir in moves:
            new_x, new_y = zero_x + move_x, zero_y + move_y

            if is_valid(new_x, new_y):
                new_state = [row[:] for row in current_state]
                new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]

                if tuple(map(tuple, new_state)) not in closed_set:
                    heapq.heappush(open_list, (g + 1 + heuristic(new_state, goal_state), g + 1, new_state, path + [(new_state, move_dir, heuristic(new_state, goal_state))]))
    return None

def input_to_matrix(input_data):
    return [input_data[i:i+3] for i in range(0, len(input_data), 3)]

def get_user_input(prompt):
    while True:
        c = input(prompt).split()
        if len(set(c)) == 9 and '_' in c:
            return input_to_matrix(c)
        print("Invalid input. Enter 8 unique values and an underscore for the blank tile.")

initial_state = get_user_input("Enter the initial state with 9 space-separated elements (use '_' for blank):\n")
goal_state = get_user_input("Enter the goal state with 9 space-separated elements (use '_' for blank): \n")

print('Initial state: ')
print_board(initial_state)
print('Final state: ')
print_board(goal_state)

path = astar(initial_state, goal_state)
if path:
    for step, (state, direction, h) in enumerate(path):
        g = step + 1
        print(f'Step {g} : f(x) = {g} + {h}')
        if h == 0:
            print(f'Move the 0 to {direction}')# Stop printing steps when goal is reached
            print_board(state)
            print("Final state reached")
            break
        else:
            print(f'Move empty tile to {direction}')
            print_board(state)
else:
    print('No solution found.')
