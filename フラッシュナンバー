import tkinter as tk
import random
a = 0
fnt = ("Times New Roman", 14)

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)

    def create_label(self, a):
        self.label = tk.Label(self, text=a, font=fnt)
        self.label.pack()
        self.root.after(1000, self.delete_label)
    def delete_label(self):
        self.label.destroy()
        num()
        self.root.after(5000, self.create_label, a)
    def create_entry(self):
        entry1 = tk.Entry(self, font=fnt)
        entry1.pack(side="bottom")
        entry1.focus_force()

def num():
    global a
    a = random.randint(100,1000)
    return a

root = tk.Tk()
root.title('フラッシュナンバー')
root.geometry('400x300')
app = Application(root=root)
num()
app.create_label(a)
app.create_entry()
app.mainloop()
