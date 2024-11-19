import streamlit as st
import numpy as np

st.title("Tic Tac Toe")

# Initialize the board
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
if 'current_player' not in st.session_state:
    st.session_state.current_player = 1

def check_winner(board):
    for i in range(3):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != 0:
            return board[i, 0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != 0:
            return board[0, i]
    if board[0, 0] == board[1, 1] == board[2, 2] != 0:
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != 0:
        return board[0, 2]
    if np.all(board != 0):
        return -1
    return 0

def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current_player = 1

winner = check_winner(st.session_state.board)

if winner == 0:
    st.write(f"Player {st.session_state.current_player}'s turn")
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            if st.session_state.board[i, j] == 0:
                if cols[j].button(f" ", key=f"{i}-{j}"):
                    st.session_state.board[i, j] = st.session_state.current_player
                    st.session_state.current_player = 3 - st.session_state.current_player
                    st.experimental_rerun()
            else:
                cols[j].button(f"{st.session_state.board[i, j]}", key=f"{i}-{j}", disabled=True)
else:
    if winner == -1:
        st.write("It's a draw!")
    else:
        st.write(f"Player {winner} wins!")
    if st.button("Reset Game"):
        reset_game()
        st.experimental_rerun()