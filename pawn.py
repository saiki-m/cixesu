import tkinter as tk
import random
import copy
import chesu_draw as cd
from functools import partial

anp_y, anp_x = 0, 0
fnt = "Times New Roman"
f14 = (fnt, 14)
bt = [None]*4
    
def sirusi(muki, koma, my, mx):
    global board, proc, Y, X
    
    if mx != 0 and koma <= board[my+muki][mx-1] <= koma + 5: # ななめ左に相手のこまがあったら
        cd.draw_en(-80, 80*muki, "pink")
        board[my+muki][mx-1] = -2
    if mx != 7 and koma <= board[my+muki][mx+1] <= koma + 5: # ななめ右にあったら
        cd.draw_en(80, 80*muki, "pink")
        board[my+muki][mx+1] = -2
        
    if board[my+muki][mx] == -1: #1マス先が空いているとき
        cd.draw_en(0, 80*muki, "green")
        board[my+muki][mx] = -2                    
        if board[my+2*muki][mx] == -1 and my == -2.5*muki +3.5 :  #2マス先が空いているとき
            cd.draw_en(0, 160*muki, "green")
            board[my+2*muki][mx] = -2

    if my == anp_y and (mx-1 == anp_x or mx+1 == anp_x):#アンパッサン第2判定：隣にアンパッサンできる相手のポーンがあれば
        Y = 80*muki + anp_y*80
        X = anp_x*80
        cd.draw_en(0, 0, "blue")
        board[anp_y+muki][anp_x] = -2     #残像マスに移動できるようにする

def ugo(muki, koma, my, mx, pre_y, pre_x):
    global board, bt, proc, anp_y, anp_x, pre_board
    
    if anp_y + muki == my and anp_x == mx:  #アンパッサン第3判定: アンパッサンするなら
        pre_board[anp_y][anp_x] = -1     #相手のポーンを取る
    anp_y, anp_x = 0, 0
    
    board = copy.deepcopy(pre_board)
    board[pre_y][pre_x] = -1
    board[my][mx] = koma
    
    pre_board = copy.deepcopy(board)
    print(pre_board)
    cd.banmen()

    if abs(pre_y - my) == 2:  #アンパッサン第1判定:2マス移動後、隣に相手のポーンがあったら
        if (mx != 7 and board[my][mx+1] == 6 - koma) or (mx != 0 and board[my][mx-1] == 6 - koma):  
            anp_y, anp_x = my, mx

    if my == 3.5 + 3.5*muki: #プロモーション
        chesu.root.unbind("<Button>", id)    #コマを動かせないよう一時停止
        cd.draw_en(0, 0, "silver")
        for i, a in enumerate(["ルーク","ナイト","ビショップ","クイーン"]):
            bt[i] = tk.Button(chesu.root, text= a, font=f14, width=10, command=partial(promo, i+(koma+1)))
            bt[i].pack(side=tk.LEFT, padx=25)
            
    proc = abs(0.5*muki-0.5)   
    
def promo(nari):
    global bt, board, id, pre_board
    my = chesu.my
    mx = chesu.mx
    for i in range(4):
        bt[i].pack_forget()
    
    board[my][mx] = nari
    cd.banmen()
    
    pre_board = copy.deepcopy(board)
    id = chesu.root.bind("<Button>", chesu.click)