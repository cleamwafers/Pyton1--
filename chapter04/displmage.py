import tkinter as tk
#ウィンドウを表示するモジュール
import tkinter.filedialog as fd
#ファイスダイアログを使うモジュール
import PIL.Image
#画像を扱うモジュール
import PIL.ImageTk
#tkinterで作った画面上に画像を表示させるモジュール

def dispPhoto(path):
    #画像ファイルを表示する関数
    newImage = PIL.Image.open(path).resize((300,300))
    #画像を読み込む
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
#上記3つはイメージをラベルに表示する

def openFile():
    #ファイルダイアログを開くための関数
    fpath = fd.askopenfilename()
    """
    ファイルダイアログを開いて、選択したファイル名を取得する(ファイルダイアログが出て居る間はここの行で止まった状態になる。)
    OpenまたはCancelボタンをクリックすると、選んだファイル名がfpath変数に入ってきて、次の行へ進む。
    Cancelボタンを選ぶと変数の中に空っぽな値として入ってくる。
    """

    if fpath:
    #調べている。もしファイル名があったら・・・
        dispPhoto(fpath)
        #そのファイル名で関数を呼び出す
root = tk.Tk()
root.geometry("400x350")
#上記２つは画面を作る

btn = tk.Button(text="ファイルを開く", command = openFile)
#ボタンを作って関数を指定する(ボタンがクリックされたらファイルダイアログを開く関数を実行する。)
imageLabel = tk.Label()
#画面表示用のラベルを作る
btn.pack()
#画面にボタンを配置する(btn→imageLabelの順でpack命令をしているのでボタン、画像ラベルの順で配置される。)
imageLabel.pack()
#画面にラベルを配置する
tk.mainloop()
#作ったウィンドウを表示する

"""
プログラムは上から順番に実行していく。
関数は関数を呼び出すところより上に書く。
例1:『commmand = openfile』を書くならopenFile関数はそれより上に。
例2:openFile関数の中で『disPhoto(fpath)』を呼び出すなら、disPhoto関数はopenFile関数より上に書かなければいけない。
"""