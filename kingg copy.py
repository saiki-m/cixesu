import tkinter as tk
import copy
import chesu
sy = 0
sx = 0

#def draw_en(x, y, col):
 #   global X, Y
  #  
   # create_oval(X+5+x, Y+5+y, X+75+x, Y+75+y, outline=col, width=2, tag="select")  #〇を表示
    
def sirusi(koma, my, mx):
    global board
    board = copy.deepcopy(chesu.board)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            sx = mx + dx
            sy = my + dy
            if sx<=-1 or sx>=8 or sy<=-1 or sy>=8:
                continue
            if board[sy][sx] == -1:
                print(board[sy][sx])
                #draw_en(sx*80, sy*80, "green")
                board[sy][sx] = -2           
    return board 