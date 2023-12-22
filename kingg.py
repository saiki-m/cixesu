import tkinter as tk
import copy
import chesu
sy = 0
sx = 0
    
def sirusi(my, mx):
    global board
    board = copy.deepcopy(chesu.board)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            sx = mx + dx
            sy = my + dy
            if sx<=-1 or sx>=8 or sy<=-1 or sy>=8:
                continue
            if board[sy][sx] == -1:
                board[sy][sx] = -3           
    return board 