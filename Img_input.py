# インポート
import cv2
import numpy
import tkinter
import tkinter.filedialog
# import ansi_8bit as ansi
import AnsiCreateImg as aci
from PIL import Image, ImageTk, ImageOps
import os
# 定数
# 幅
WIDTH = 640
# 高さ
HEIGHT = 400

# 画像を表示　ー＞　 変換ボタンでANSIに変換する ー＞  ANSIを保存する（とりあえず画像を保存するようなボタンを作りたい）
# UIデザイン
# 解像度変更


def pil_to_cv2(pil_image: Image) -> Image:
    # 'PIL -> CV2'

    # pil_imageをNumPy配列に変換
    pil_image_array = numpy.array(pil_image)
    # RGB -> BGR によりCV2画像オブジェクトに変換
    cv2_image = cv2.cvtColor(pil_image_array, cv2.COLOR_BGR2RGB)
    cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

    print(cv2_image.shape)

    return cv2_image


# 関数(開く)
def f_open():

    # グローバル変数
    global image
    global cv2_image

    # ファイルダイアログ
    name = tkinter.filedialog.askopenfilename(
        title="ファイル選択", initialdir="C:/", filetypes=[("Image File", "*.png")])

    # 画像ロード
    image = Image.open(name)
    cv2_image = pil_to_cv2(image)

    # image = tkinter.PhotoImage(file=name)
    image = Image.open(name)
    image_dummy = image
    image = ImageOps.pad(image_dummy, (WIDTH, HEIGHT))
    image = ImageTk.PhotoImage(image=image)

    # キャンバスに表示
    canvas.create_image(WIDTH / 2, HEIGHT / 2, image=image)


def f_save_16():
    main.filename = tkinter.filedialog.asksaveasfilename(
        initialdir="/", title="Save as", filetypes=[("text file", "*.txt")])
    ansi_class = aci.AnsiCreateImage()
    ansi_class.f_conversion_4bit(cv2_image, main.filename)


def f_save_256():
    main.filename = tkinter.filedialog.asksaveasfilename(
        initialdir="/", title="Save as", filetypes=[("text file", "*.txt")])
    ansi_class = aci.AnsiCreateImage()
    # print(dir(ansi_class))
    ansi_class.f_conversion_8bit(cv2_image, main.filename)


def f_save_24bit():
    main.filename = tkinter.filedialog.asksaveasfilename(
        initialdir="/", title="Save as", filetypes=[("text file", "*.txt")])
    image.f_conversion_24bit(cv2_image, main.filename)


# 関数(閉じる)
def f_close():

    # キャンバスクリア
    canvas.delete("all")


# メイン画面作成
main = tkinter.Tk()

# 画面サイズ設定
main.geometry("640x400")

filepath = "AnsiCreateImg.py"
print("カレントパス", os.getcwd())
print("filepath が指す絶対パス", os.path.abspath(filepath))
print("ファイルが存在するかどうか", os.path.isfile(filepath))


# メニューバー作成
menubar = tkinter.Menu(main)

# ファイルメニュー作成
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="開く", command=f_open)
filemenu.add_command(label="16色で保存", command=f_save_16)
filemenu.add_command(label="256色で保存（推奨)", command=f_save_256)
# filemenu.add_command(label="24bitで保存(未完成：押しても反応しません。")
filemenu.add_command(label="閉じる", command=f_close)
filemenu.add_separator()
filemenu.add_command(label="終了", command=main.quit)

# メニュー設定
menubar.add_cascade(label="ファイル", menu=filemenu)

# メニューバー配置
main.config(menu=menubar)

# キャンバス作成・配置
canvas = tkinter.Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack()

# # ボタン作成
# btn = tkinter.Button(main, text="ボタン")
# # ボタン表示
# btn.place(x=125, y=230, width=150, height=40)

# イベントループ
main.mainloop()
