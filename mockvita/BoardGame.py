def calculate_score(board):
    rows = len(board)
    cols = len(board[0])
    score = 0

    # Check horizontal lines
    for row in board:
        current_streak = 1
        for i in range(1, cols):
            if row[i] == row[i - 1]:
                current_streak += 1
            else:
                if current_streak >= 3:
                    score += sum(int(row[j]) for j in range(i - current_streak, i))
                current_streak = 1
        if current_streak >= 3:
            score += sum(int(row[j]) for j in range(cols - current_streak, cols))

    # Check vertical lines
    for col in range(cols):
        current_streak = 1
        for i in range(1, rows):
            if board[i][col] == board[i - 1][col]:
                current_streak += 1
            else:
                if current_streak >= 3:
                    score += sum(
                        int(board[j][col]) for j in range(i - current_streak, i)
                    )
                current_streak = 1
        if current_streak >= 3:
            score += sum(int(board[j][col]) for j in range(rows - current_streak, rows))

    return score


# Example usage
board = [[1, 2, 3, 4], [1, 1, 2, 3], [3, 4, 2, 2], [4, 4, 1, 4]]

print(f"Score: {calculate_score(board)}")
