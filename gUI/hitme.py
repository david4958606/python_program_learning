import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Hit Me!")
mainWindow.geometry("1280x720")
varText = tk.StringVar()
varText.set("Hello! Anybody there?")
s = tk.Label(textvariable=varText, bg="#66ccff")
s.pack()

doYouHit = 0


def hit_me():
    global doYouHit, varText
    if doYouHit == 0:
        doYouHit = 1
        varText.set("Oh! That's hurt!")
    else:
        doYouHit = 0
        varText.set("Stop! I know you are here!")


button = tk.Button(mainWindow,
                   text="Hit Me!",
                   command=hit_me)
button.pack()

mainWindow.mainloop()
