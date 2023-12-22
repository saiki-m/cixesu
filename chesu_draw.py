import tkinter as tk
import copy

board =[
    [7,8,9,-1,11,-1,8,7],
    [6,6,6,-1,-1,-1,6,6],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,-1,5,-1,0,0],
    [1,2,3,-1,-1,-1,2,1]    
]
pre_board = copy.deepcopy(board) 
img = [None]*12

cvs = tk.Canvas(width=640, height=640)
cvs.pack()

def draw_en(x, y, col):
    cvs.create_oval(x+5, y+5, x+75, y+75, outline=col, width=2, tag="select")  #〇を表示 
    
def banmen():
    cvs.delete("all")
    for i in range(1,8):   #マス目を描く
        cvs.create_line(80*i, 0, 80*i, 640, fill="gray", width=3)
        cvs.create_line(0, 80*i, 640, 80*i, fill="gray", width=3)
        
    for y in range(8):
        for x in range(8):
            for i in range(12):
                if board[y][x] == i:
                    cvs.create_image(x*80+40, y*80+40, image=img[i])    