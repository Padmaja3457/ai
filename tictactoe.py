import random

def generateSquare(n):
    magicSquare = [[0 for _ in range(n)] for _ in range(n)]
    i, j, num = 0, 1, 1
    while num <= n * n:
        magicSquare[i][j] = num
        next_i, next_j = (i - 1) % n, (j + 1) % n
        if magicSquare[next_i][next_j]:
            next_i, next_j = (i + 1) % n, j
        i, j, num = next_i, next_j, num + 1
    return magicSquare

def printMagicSquare(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol):
    for row in magicSquare:
        print(' | '.join(
            player_symbol if num in player_moves else
            computer_symbol if num in computer_moves else
            str(num)
            for num in row
        ))
        print('-' * 9)

def checkWin(magicSquare, n, moves):
    magic_constant = n * (n * n + 1) // 2
    rows = [sum(magicSquare[i][j] for j in range(n) if magicSquare[i][j] in moves) == magic_constant for i in range(n)]
    cols = [sum(magicSquare[j][i] for j in range(n) if magicSquare[j][i] in moves) == magic_constant for i in range(n)]
    diags = [sum(magicSquare[i][i] for i in range(n) if magicSquare[i][i] in moves) == magic_constant,
             sum(magicSquare[i][n - i - 1] for i in range(n) if magicSquare[i][n - i - 1] in moves) == magic_constant]
    return any(rows + cols + diags)

def findWinningMove(magicSquare, n, moves, available_numbers):
    return next((num for num in available_numbers if checkWin(magicSquare, n, moves + [num])), None)

def tossForFirstPlayer():
    return random.choice([0, 1])

def getValidInput(prompt, valid_choices):
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice in valid_choices:
                return valid_choices[choice]
            print(f"Invalid choice. Please choose from {list(valid_choices.keys())}.")
        except ValueError as e:
            print("Inavalid input.Choose from available numbers")

def playGame(magicSquare, n):
    player_moves, computer_moves = [], []
    available_numbers = [num for row in magicSquare for num in row]
    printMagicSquare(magicSquare, player_moves, computer_moves, " ", " ")
    
    toss_result = tossForFirstPlayer()
    human_choice = getValidInput('Select "0" or "1" for the toss: ', {'0': 0, '1': 1})
    
    player_symbol, computer_symbol = ('X', 'O') if human_choice == toss_result else ('O', 'X')
    current_player = 'X'
    print(f"{'Human' if human_choice == toss_result else 'Computer'} won the toss!")

    for _ in range(n * n):
        moves, symbol = (computer_moves, computer_symbol) if current_player == computer_symbol else (player_moves, player_symbol)
        if current_player == computer_symbol:
            move = findWinningMove(magicSquare, n, computer_moves, available_numbers) or \
                   findWinningMove(magicSquare, n, player_moves, available_numbers) or \
                   random.choice(available_numbers)
            print(f"Computer's choice: {move}")
        else:
            move = getValidInput(f"Select number from the board: ", {str(num): num for num in available_numbers})
        moves.append(move)
        available_numbers.remove(move)
        printMagicSquare(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol)
        if checkWin(magicSquare, n, moves):
            print(f"{'Computer' if current_player == computer_symbol else 'Player'} wins!")
            return
        current_player = 'O' if current_player == 'X' else 'X'

    print("It's a draw!")

def main():
    while True:
        playGame(generateSquare(3), 3)
        play_again = getValidInput("Would you like to play again? (yes/no or 1/0): ", {'yes': True, '1': True, 'no': False, '0': False})
        if not play_again:
            print("Thanks for playing!")
            break

main()
