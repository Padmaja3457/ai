while True:
    user_input = input("Enter the n value of n*n board (<=20): ")

    try:
        n = int(user_input)
        
        if n <= 0:
            print("Please enter a positive number.")
            continue
        elif n == 3 or n == 2:
            print("Not possible. N-queen problem is only solvable for n > 3.")
            continue
        elif n > 20:
            print("n value should be less than 20:")
            continue
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")

matrix = [[0 for i in range(n)] for j in range(n)]  
"""print("Board before plotting queens:")  
for row in matrix:  
    print(" ".join(map(str, row)))"""
while True:
    try:
        first_row = int(input("Enter a row for placing a queen to start: "))
        if first_row <= 0:
            raise ValueError()
            continue
        if first_row > n:
            raise ValueError()
            continue
        break
    except ValueError:
        print("Invalid input. Please enter valid integer")
while True:
    try:
        first_col = int(input("Enter a col for placing a queen to start: ")) 
        if first_col <= 0:
            raise ValueError()
            continue
        if first_col > n:
            raise ValueError()
            continue
        break
    except ValueError:
        print("Invalid input. Please enter valid integer")
 
matrix[first_row - 1][first_col - 1] = 1  # mark the initial position with a queen  
print("Board at step 1: ")  
for row in matrix:  
    print(" ".join(map(str, row)))  
def is_safe(matrix, row, col, n):  
        # Check vertical   
    for i in range(row):  
        if matrix[i][col] == 1:  
            return False  
                
   # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i, j = row, col
    while j < n and i < n:
        if matrix[i][j] == 1:
            return False
        i += 1
        j += 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if matrix[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    i, j = row, col
    while j >= 0 and i < n:
        if matrix[i][j] == 1:
            return False
        i += 1
        j -= 1
            
    return True  
def solve_nqueens(matrix, row, n,col_taken):  
    if row >= n:  
        return True  

        # Skip the row where the first queen is placed
    if row == first_row - 1:  
        return solve_nqueens(matrix, row + 1, n,cols_taken)  
        
    for col in range(n):  
        if col in cols_taken:  # Skip if this column is already occupied by a previous queen
            continue

        if is_safe(matrix, row, col, n):  
            matrix[row][col] = 1  # Place queen  
            cols_taken.add(col)  # Mark this column as occupied

            if solve_nqueens(matrix, row + 1, n, cols_taken):  
                return True  
                    
            matrix[row][col] = 0  # Backtrack  
            cols_taken.remove(col)  # Unmark the column
        

    return False  

def print_matrix(matrix):  
    for row in matrix:  
        print(" ".join(map(str, row)))  
cols_taken = {first_col - 1}
if solve_nqueens(matrix, 0, n,cols_taken):  
    print("Solution found:")  
    print_matrix(matrix)  
else:  
    print("No solution found")
