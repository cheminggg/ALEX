from tkinter import *

win = Tk()
win.title("voice")

win.geometry("800x500+300+200")
win.resizable(FALSE, FALSE)
# win['bg'] = '#361fa6'
win['bg'] = '#3f189e'


def btnexit():
    btn.config(exit())


btn = Button(win, text="Exit", command=btnexit)
btn.place(x=740, y=0)


pdfimg = PhotoImage(file="pdf.png")
pdfbtn = Button(win, image=pdfimg)
pdfbtn.place(x=250, y=200)

voice = PhotoImage(file="voice1.png")
pdfbtn = Button(win, image=voice, bd=0)
pdfbtn.place(x=350, y=200)

img = PhotoImage(file="ai1.png")
lbl = Label(image=img)
lbl.place(x=450, y=200)


img1 = PhotoImage(file="voicerasm1.png")
lbl = Label(image=img1, bd=0)
lbl.place(x=200, y=300)


win.mainloop()
