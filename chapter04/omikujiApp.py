import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉","中吉","小吉","凶"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
#画面を作る
root.geometry("200x100")
#画面を作る(横x縦は半角英数字で指定)
lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)
#ボタンで関数を実行するように修正する

lbl.pack()
#画面にラベルを配置する(packの命令を時効した順に上から配置されていく。)
btn.pack()
#画面にボタンを配置する
tk.mainloop()
#作ったウィンドウを表示する(作った画面がこの命令で動き始める。)