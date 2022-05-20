import turtle
import time
import random
import tkinter as tk
import threading
# 弹窗设置
class Ts:
    def dow(self):
        window = tk.Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        a = random.randrange(1, width)
        b = random.randrange(0, height)
        window.title('虎来喽！')
        window.geometry("200x50" + "+" + str(a) + "+" + str(b))
        tk.Label(window,
                 text='虎年快乐虎虎生威',  # 标签的文字
                 bg='red',  # 背景颜色
                 font=('..', 17),  # 字体和字体大小
                 width=18, height=2  # 标签长宽
                 ).pack()  # 固定窗口位置
        window.mainloop()

if __name__ == '__main__':
    i = 0
    # while i<100:
    for i in range(1, 10):

        print(Ts().dow())
        i = i + 1

