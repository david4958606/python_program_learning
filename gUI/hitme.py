import tkinter as tk
import random

mainWindow = tk.Tk()
mainWindow.title("Hit Me!")
mainWindow.geometry("1280x720")
varText = tk.StringVar()
varText.set("Hello! Anybody there?")
s = tk.Label(textvariable=varText, bg="#66ccff", font=("方正楷体_GBK", 14))
s.pack()


def hit_me():
    global varText
    do_you_hit = random.randint(1, 3)
    if do_you_hit == 1:
        varText.set("1. Oh! That's hurt!")
    elif do_you_hit == 2:
        varText.set("2. Stop! I know you are here!")
    elif do_you_hit == 3:
        varText.set("3. FUCK YOU!!!")


button = tk.Button(mainWindow,
                   text="Hit Me!",
                   command=hit_me)
button.pack()

mainWindow.mainloop()
