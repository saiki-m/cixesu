import tkinter as tk
import copy
import pawn
import kingg
import chesu_draw as cd

my, mx, Y, X = 0, 0, 0, 0
pre_y, pre_x = -100, -100
proc = 0


def click(e):
    global pre_x, pre_y, mx, my, X, Y
    cd.cvs.delete("select")
    
    my, mx = int(e.y/80), int(e.x/80)
    Y, X = my*80, mx*80           

    if mx>=7: mx = 7
    elif my>=7: my = 7
    
    cd.draw_en(X, Y, "red")  #クリックしたマスを表示

    if proc == 0:
        if cd.board[my][mx] == 0:
            cd.board = copy.deepcopy(cd.pre_board)
            pre_y, pre_x = my, mx 
            pawn.sirusi(-1, 6, my, mx)    

        if cd.board[my][mx] == -2:
            pawn.ugo()
            
    if proc == 1:
        if cd.board[my][mx] == 6:
            cd.board = copy.deepcopy(cd.pre_board)
            pre_y, pre_x = my, mx 
            pawn.sirusi(1, 0, my, mx)

        if cd.board[my][mx] == -2:
            pawn.ugo()
            

root = tk.Tk()
root.title("チェス")
root.resizable(False,False)
id = root.bind("<Button>", click)

for i in range(12):
    cd.img[i] = tk.PhotoImage(file=str(i)+".png")    #実行するときのディレクトリに注意　cixesuディレまでcdする

cd.banmen()
root.mainloop()