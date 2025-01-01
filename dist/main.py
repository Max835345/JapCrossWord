from tkinter import *
from tkinter import ttk
import os

from PIL import ImageTk, Image

k = 0


class Main():
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.root.title("JapCrossWord")
        self.root.geometry("450x430")
        self.root.iconbitmap('fuji.ico')
        self.root.resizable(width=False, height=False)
        self.root["bg"] = "#3C3C3C"
        self.frm.grid()
        self.FirstWindow()

    def FirstWindow(self):
        self.label = Label(text="JapCrossWord", font=('Handjet', 28), background='#3C3C3C', fg='white')
        self.label.place(x=100, y=40)
        self.btn1 = Button(text="Играть", background="#3C3C3C", foreground="#ccc", font=('inter', 14), width=20,
                           height=2, activebackground="#515151", command=lambda: self.FirstWindowPlay())
        self.btn1.place(x=115, y=110)
        self.btn2 = Button(text="Инструкция", background="#3C3C3C", foreground="#ccc", font=('inter', 14), width=20,
                           height=2, activebackground="#515151", command=lambda: self.os())
        self.btn2.place(x=115, y=195)
        self.btn3 = Button(text="Выход", background="#3C3C3C", foreground="#ccc", font=('inter', 14),
                           command=self.root.destroy, width=20, height=2, activebackground="#515151")
        self.btn3.place(x=115, y=280)
        self.root.mainloop()

    def DestroyFirstWindow(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.label.destroy()

    def os(self):
        ret = os.system('Инструкция.docx')

    def FirstWindowPlay(self):
        self.root.destroy()
        GRID_SIZE = 10  # Ширина и высота игрового поля
        self.idl = [3, 4, 10, 12, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 38,
                    40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 56, 57, 58, 59, 60, 67, 68, 69, 70, 74, 75, 80, 83, 85, 86,
                    89, 90, 96, 97, 98, 99]
        SQUARE_SIZE = 40  # Размер одной клетки на поле
        y = 2
        x = 2
        k = 0  # Кол-во ошибок

        clicked = set()  # Создаем сет для клеточек, по которым мы кликнули

        def click(event):
            global k
            ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
            idslist = (
            1, 2, 5, 6, 7, 8, 9, 11, 13, 16, 17, 30, 31, 39, 45, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73,
            76, 77, 78, 79, 81, 82, 84, 87, 88, 91, 92, 93, 94, 95, 100)
            d = 0
            for i in idslist:
                if ids == i:
                    d = 1
                    k = k + 1
            if d == 1:
                c.itemconfig(CURRENT, fill="red")  # Иначе красим в зеленый
                c.update()
            else:
                c.itemconfig(CURRENT, fill="black")  # Иначе красим в зеленый
                c.update()
                for i in self.idl:
                    if ids == i:
                        self.idl.remove(i)
            if k >= 4:
                self.LossWindow()
            if self.idl == []:
                self.WinWindow()

        def clear(event):

            ids = c.find_withtag(CURRENT)[0]  # Определяем по какой клетке кликнули
            c.itemconfig(CURRENT, fill="grey")  # Иначе красим в зеленый
            c.update()

        self.root = Tk()
        self.root.iconbitmap('fuji.ico')
        self.root.title("JapCrossWorld")
        self.root.resizable(width=False, height=False)
        c = Canvas(self.root, width=(GRID_SIZE * SQUARE_SIZE) + 2 * SQUARE_SIZE,
                   height=(GRID_SIZE * SQUARE_SIZE) + 2 * SQUARE_SIZE)
        c.bind("<Button-1>", click)
        c.bind("<Button-3>", clear)
        c.pack()

        xcod = {'0': '2\n1', '1': '1\n2\n3', '2': '9', '3': '7\n1', '4': '4\n5', '5': '5', '6': '4', '7': '2\n1',
                '8': '1\n2\n2', '9': '4', '10': '', '11': ''}
        ycod = {'1': '1 1', '2': '4', '3': '1 3 1', '4': '5 1', '5': '3 2', '6': '4 2', '7': '5 1', '8': '6 1',
                '9': '2 3 2', '10': '2 6', '11': '', '12': ''}
        for i in range(GRID_SIZE + 2):
            for j in range(GRID_SIZE + 2):
                if i == 0:
                    label = Label(text=xcod[str(j)], font=13)
                    label.pack()
                    if y == 4 or y == 7 or y == 8 or y == 11:
                        label.place(x=(SQUARE_SIZE * y) + 18, y=55)
                    elif y == 2 or y == 5 or y == 6 or y == 9:
                        label.place(x=(SQUARE_SIZE * y) + 18, y=38)
                    else:
                        label.place(x=(SQUARE_SIZE * y) + 18, y=20)
                    y = y + 1
                elif j == 0:
                    label = Label(text=ycod[str(i)], font=13)
                    label.pack()
                    if x == 3:
                        label.place(x=61, y=(SQUARE_SIZE * x) + 7)
                    elif x == 4 or x == 10:
                        label.place(x=36, y=(SQUARE_SIZE * x) + 7)
                    else:
                        label.place(x=49, y=(SQUARE_SIZE * x) + 7)
                    x = x + 1
                elif (j != 0 and i != 0) and (j != 1 and i != 1):
                    c.create_rectangle(i * SQUARE_SIZE, j * SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE,
                                       j * SQUARE_SIZE + SQUARE_SIZE, fill='grey')

        self.root.mainloop()

    def LossWindow(self):
        global k
        self.root.destroy()
        self.root = Tk()
        self.img = ImageTk.PhotoImage(Image.open("lose.png"))
        self.frm = ttk.Frame(self.root, padding=10)
        self.root.title("JapCrossWord")
        self.root.iconbitmap('fuji.ico')
        self.root.geometry("350x200")
        self.root.resizable(width=False, height=False)
        self.root["bg"] = "#fff"
        self.frm.grid()
        self.label = Label(self.root, image=self.img, border=0)
        self.label.place(x=100, y=0)
        self.btn5 = Button(text="Выход", background="#f8f8f8", foreground="#ccc", font=14,
                           command=lambda: self.root.destroy(),
                           width=17, height=2, activebackground="#515151", fg='black')
        self.btn5.place(x=180, y=145)
        self.btn6 = Button(text="Играть снова", background="#f8f8f8", foreground="#ccc", font=14,
                           width=17, height=2, activebackground="#515151", fg='black',
                           command=lambda: self.FirstWindowPlay())
        self.btn6.place(x=5, y=145)
        k = 0

    def WinWindow(self):
        global k
        self.root.destroy()
        self.root = Tk()
        self.img = ImageTk.PhotoImage(Image.open("champagne.png"))
        self.frm = ttk.Frame(self.root, padding=10)
        self.root.title("JapCrossWord")
        self.root.iconbitmap('fuji.ico')
        self.root.geometry("350x200")
        self.root.resizable(width=False, height=False)
        self.root["bg"] = "#fff"
        self.frm.grid()
        self.label = Label(self.root, image=self.img, border=0)
        self.label.place(x=100, y=0)
        self.btn5 = Button(text="Выход", background="#f8f8f8", foreground="#ccc", font=14,
                           command=lambda: self.root.destroy(),
                           width=17, height=2, activebackground="#515151", fg='black')
        self.btn5.place(x=180, y=145)
        self.btn6 = Button(text="Играть снова", background="#f8f8f8", foreground="#ccc", font=14,
                           width=17, height=2, activebackground="#515151", fg='black',
                           command=lambda: self.FirstWindowPlay())
        self.btn6.place(x=5, y=145)
        k = 0



if __name__ == "__main__":
    app = Main()
