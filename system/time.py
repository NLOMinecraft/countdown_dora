from datetime import datetime
import time
import tkinter as tk
from dateutil.relativedelta import relativedelta
from art import text2art

target_date = datetime(2112, 9, 3, 0, 0, 0)

mode = input("表示タイプ(TEXT, ASCII, GUI, GUI-ASC): ").upper()

def get_countdown_text():
    now = datetime.now()
    if now >= target_date:
        return "カウントダウン終了"

    diff = relativedelta(target_date, now)
    return f"残り {diff.years}年 {diff.months}ヶ月 {diff.days}日 {diff.hours:02d}時 {diff.minutes:02d}分 {diff.seconds:02d}秒"

if mode in ["TEXT", "ASCII"]:
    while True:
        countdown_text = get_countdown_text()
        if countdown_text == "カウントダウン終了":
            print("\nカウントダウン終了")
            break

        if mode == "TEXT":
            print(f"\r{countdown_text}", end="")
        elif mode == "ASCII":
            art = text2art(countdown_text)
            print(art, end="")

        time.sleep(1)

elif mode in ["GUI", "GUI-ASC"]:
    root = tk.Tk()
    root.title("ドラえもんまでカウントダウン")
    root.geometry("1000x400")
    bg_color = "black" if mode == "GUI-ASC" else "white"
    fg_color = "cyan" if mode == "GUI-ASC" else "blue"

    label = tk.Label(root, text="", font=("Courier", 14), fg=fg_color, bg=bg_color, justify="left")
    label.pack(expand=True)

    def update_gui():
        countdown_text = get_countdown_text()
        if countdown_text == "カウントダウン終了":
            label.config(text="カウントダウン終了")
            return

        if mode == "GUI":
            label.config(text=countdown_text)
        else:  # GUI-ASC
            art = text2art(countdown_text)
            label.config(text=art)

        root.after(1000, update_gui)

    update_gui()
    root.mainloop()


