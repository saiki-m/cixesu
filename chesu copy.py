import tkinter as tk
import random
import copy
import kingg
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
    [7,8,9,-1,11,-1,8,7],
    [6,6,6,-1,-1,-1,6,6],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [0,0,0,-1,-1,-1,0,0],
    [1,2,3,-1,5,-1,2,1]    
]
pre_board = copy.deepcopy(board)
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
        if board[my][mx] == 0:
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx 
            pawn = Pawn(-1, 6)
            pawn.sirusi()    

        if board[my][mx] == -2:
            pawn = Pawn(-1, 0)
            pawn.ugo()
            
        if board[my][mx] == 5:
            pre_y, pre_x = my, mx
            kingg.sirusi(0, my, mx, board)
            print(board)
        
    if proc == 1:
        if board[my][mx] == 6:
            board = copy.deepcopy(pre_board)
            pre_y, pre_x = my, mx 
            pawn = Pawn(1, 0)
            pawn.sirusi()

        if board[my][mx] == -2:
            pawn = Pawn(1, 6)
            pawn.ugo()
            
        if board[my][mx] == 11:
            king = king(-1, 0)

class Pawn():
    def __init__(self, muki, koma):
        self.muki = muki
        self.koma = koma
        
    def sirusi(self):
        global board, proc, Y, X
        if mx != 0 and self.koma <= board[my+self.muki][mx-1] <= self.koma + 5: # ななめ左に相手のこまがあったら
            draw_en(-80, 80*self.muki, "pink")
            board[my+self.muki][mx-1] = -2
        if mx != 7 and self.koma <= board[my+self.muki][mx+1] <= self.koma + 5: # ななめ右にあったら
            draw_en(80, 80*self.muki, "pink")
            board[my+self.muki][mx+1] = -2
            
        if board[my+self.muki][mx] == -1: #1マス先が空いているとき
            draw_en(0, 80*self.muki, "green")
            board[my+self.muki][mx] = -2                    
            if board[my+2*self.muki][mx] == -1 and my == -2.5*self.muki +3.5 :  #2マス先が空いているとき
                draw_en(0, 160*self.muki, "green")
                board[my+2*self.muki][mx] = -2

        if my == anp_y and (mx-1 == anp_x or mx+1 == anp_x):#アンパッサン第2判定：隣にアンパッサンできる相手のポーンがあれば
            Y = 80*self.muki + anp_y*80
            X = anp_x*80
            draw_en(0, 0, "blue")
            board[anp_y+self.muki][anp_x] = -2     #残像マスに移動できるようにする
    
    def ugo(self):
        global board, bt, proc, anp_y, anp_x, pre_board
            
        if anp_y + self.muki == my and anp_x == mx:  #アンパッサン第3判定: アンパッサンするなら
            pre_board[anp_y][anp_x] = -1     #相手のポーンを取る
        anp_y, anp_x = 0, 0
        
        board = copy.deepcopy(pre_board)
        board[pre_y][pre_x] = -1
        board[my][mx] = self.koma
        
        pre_board = copy.deepcopy(board)
        
        banmen()

        if abs(pre_y - my) == 2:  #アンパッサン第1判定:2マス移動後、隣に相手のポーンがあったら
            if (mx != 7 and board[my][mx+1] == 6 - self.koma) or (mx != 0 and board[my][mx-1] == 6 - self.koma):  
                anp_y, anp_x = my, mx

        if my == 3.5 + 3.5*self.muki: #プロモーション
            root.unbind("<Button>", id)    #コマを動かせないよう一時停止
            draw_en(0, 0, "silver")
            for i, a in enumerate(["ルーク","ナイト","ビショップ","クイーン"]):
                bt[i] = tk.Button(root, text= a, font=f14, width=10, command=partial(self.promo, i+(self.koma+1)))
                bt[i].pack(side=tk.LEFT, padx=25)
                
        proc = abs(0.5*self.muki-0.5)   
        
    def promo(self, nari):
        global bt, board, id, pre_board
        
        for i in range(4):
            bt[i].pack_forget()
        
        board[my][mx] = nari
        banmen()
        
        pre_board = copy.deepcopy(board)
        id = root.bind("<Button>", click)

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
    img[i] = tk.PhotoImage(file=str(i)+".png")    #実行するときのディレクトリに注意　cixesuディレまでcdする
    

banmen()
root.mainloop()