import tkinter as tk
import copy
from functools import partial

my, mx, Y, X = 0, 0, 0, 0
anp_y, anp_x = 0, 0
pre_y, pre_x = -100, -100
proc = 0
fnt = "Times New Roman"
f14 = (fnt, 14)
bt = [None]*4
img = [None]*12
board =[
    [7,8,9,10,11,9,8,7],
    [6,6,6,6,6,6,6,6],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,0,0,0,0,0],
    [1,-1,-1,-1,5,-1,-1,1]    
]
pre_board = copy.deepcopy(board)
my_castle = True
com_castle = True

def draw_en(x, y, col):
    global X, Y
    cvs.create_oval(X+5+x, Y+5+y, X+75+x, Y+75+y, outline=col, width=2, tag="select")  #〇を表示

def click(e):
    global pre_x, pre_y, mx, my, X, Y, board
    cvs.delete("select")
    
    my, mx = int(e.y/80), int(e.x/80)
    Y, X = my*80, mx*80           

    if mx>=7: mx = 7
    elif my>=7: my = 7
    
    draw_en(0, 0, "red")  #クリックしたマスを表示
    
    
    if proc == 0: 
        if board[my][mx] == 0:  #プレイヤーポーンのマス
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx 
            p_mark(-1, 6)
        if board[my][mx] == -2:
            ugo(-1, 0)
        if board[my][mx] == 5:  #プレイヤーキングのマス
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx
            K_mark(6)
        if board[my][mx] == -3:
            ugo(-1, 5)
    elif proc == 1:
        if board[my][mx] == 6:
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx
            p_mark(1, 0)
        if board[my][mx] == -2:
            ugo(1, 6)
        if board[my][mx] == 11:  #プレイヤーキングのマス
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx
            K_mark(0)
        if board[my][mx] == -3:
            ugo(1, 11)
def K_mark(koma): #キングの動けるマスを定義
    global board, sy, sx
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            sy = my + dy
            sx = mx + dx
            if sx<=-1 or sx>=8 or sy<=-1 or sy>=8:
                continue
            if board[sy][sx] == -1:
                draw_en(80*dx, 80*dy, "green")
                board[sy][sx] = -3 
            if koma <= board[sy][sx] <= koma + 5:
                draw_en(80*dx, 80*dy, "pink")
                board[sy][sx] = -3
                
    if my_castle == True:
        if board[my][mx+1] == -3 and board[my][mx+2] == -1:
            board[my][mx+2] = -3
            draw_en(160, 0, "green")
            print(board)
                    
def p_mark(muki, koma): #ポーンの動けるマスを定義
    global board, proc, Y, X
    if mx != 0 and koma <= board[my+muki][mx-1] <= koma + 5: # ななめ左に相手のこまがあったら
        draw_en(-80, 80*muki, "pink")
        board[my+muki][mx-1] = -2
    if mx != 7 and koma <= board[my+muki][mx+1] <= koma + 5: # ななめ右にあったら
        draw_en(80, 80*muki, "pink")
        board[my+muki][mx+1] = -2

    if board[my+muki][mx] == -1: #1マス先が空いているとき
        draw_en(0, 80*muki, "green")
        board[my+muki][mx] = -2                    
        if board[my+2*muki][mx] == -1 and my == -2.5*muki +3.5 :  #2マス先が空いているとき
            draw_en(0, 160*muki, "green")
            board[my+2*muki][mx] = -2

    if my == anp_y and (mx-1 == anp_x or mx+1 == anp_x):#アンパッサン第2判定：隣にアンパッサンできる相手のポーンがあれば
        Y = 80*muki + anp_y*80
        X = anp_x*80
        draw_en(0, 0, "blue")
        board[anp_y+muki][anp_x] = -2     #残像マスに移動できるようにする   

def promo(koma): #ポーンのプロモーション選択
    global board, pre_board, id

    for i in range(4):
        bt[i].pack_forget()

    board[my][mx] = koma
    banmen()
    pre_board = copy.deepcopy(board)
    id = root.bind("<Button>", click)

def ugo(muki, koma): #コマを動かす処理
    global board, bt, proc, anp_y, anp_x, pre_board

    if anp_y + muki == my and anp_x == mx:  #アンパッサン第3判定: アンパッサンするなら
        pre_board[anp_y][anp_x] = -1     #相手のポーンを取る

    anp_y, anp_x = 0, 0
    board = copy.deepcopy(pre_board)
    board[pre_y][pre_x] = -1
    board[my][mx] = koma

    pre_board = copy.deepcopy(board)

    banmen()

    if abs(pre_y - my) == 2:  #アンパッサン第1判定:2マス移動後、隣に相手のポーンがあったら
        if (mx != 7 and board[my][mx+1] == 6 - koma) or (mx != 0 and board[my][mx-1] == 6 - koma):  
            anp_y, anp_x = my, mx

    if (koma == 0 or koma == 6) and my == 3.5 + 3.5*muki: #プロモーション
        root.unbind("<Button>", id)    #コマを動かせないよう一時停止
        draw_en(0, 0, "silver")
        for i, a in enumerate(["ルーク","ナイト","ビショップ","クイーン"]):
            bt[i] = tk.Button(root, text= a, font=f14, width=10, command=partial(promo, i+(koma+1)))
            bt[i].pack(side=tk.LEFT, padx=25)    
    proc = abs(0.5*muki-0.5)       
        
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

root = tk.Tk()
root.title("チェス")
root.resizable(False,False)
id = root.bind("<Button>", click)
cvs = tk.Canvas(width=640, height=640)
cvs.pack()

for i in range(12):
    img[i] = tk.PhotoImage(file=str(i)+".png")

    

banmen()
root.mainloop()