# Darts

def create_darts_board(n: int) -> list:
    board = [[0] * n for _ in range(n)]
    
    layers = (n + 1) // 2

    for layer in range(layers):
        value = layer + 1
        
        for i in range(layer, n - layer):
            board[layer][i] = value
            board[n - layer - 1][i] = value
        
        for j in range(layer, n - layer):
            board[j][layer] = value
            board[j][n - layer - 1] = value
    
    return board

def print_board(board: list) -> None:
    for row in board:
        print(' '.join(map(str, row)))

print_board(create_darts_board(int(input())))