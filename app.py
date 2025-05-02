from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize the board
board = [" " for _ in range(9)]
current_player = "X"

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # columns
        (0,4,8), (2,4,6)           # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

@app.route("/")
def index():
    winner = check_winner(board)
    return render_template("index.html", board=board, winner=winner, current_player=current_player)

@app.route("/move/<int:cell>")
def move(cell):
    global current_player
    if board[cell] == " " and check_winner(board) is None:
        board[cell] = current_player
        current_player = "O" if current_player == "X" else "X"
    return redirect(url_for('index'))

@app.route("/reset")
def reset():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
