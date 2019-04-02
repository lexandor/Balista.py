_author__ = 'Alexander Ometov aka PLEXER'
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from math import *

class Balista:
    def __init__(self,  window):
        self.window = window
        # Разметка фреймов
        self.varListFrame         = Frame(self.window)
        self.grafFrame            = Frame(self.window)
        self.controllerFrameLeft  = Frame(self.window)
        self.controllerFrameRight = Frame(self.window)
        # Разметка полей ввода
        self.angleLabel      = Label(self.varListFrame)
        self.angleEntry      = Entry(self.varListFrame) # Поле для ввода угла к горизонту
        self.startSpeedLabel = Label(self.varListFrame)
        self.startSpeedEntry = Entry(self.varListFrame) # Поду для ввода начальной скорости с которой бросили тело.
        # Разметка кнопок
        self.btnBuild      = Button (self.controllerFrameLeft, text="Построить", command=self.plot)
        self.btnClear      = Button (self.controllerFrameLeft, text="Очистить", command=self.clear)
        self.btnLoadGraf   = Button (self.controllerFrameRight, text="Загрузить график", command=self.loadGraf)
        self.btnScreenShot = Button (self.controllerFrameRight, text="|O|", command=self.screenShot)
        self.btnSaveGraf   = Button (self.controllerFrameRight, text="Сохранить график", command=self.saveGraf)
        # Верстка полей ввода
        self.angleLabel.grid(row=0, column=0)
        self.angleEntry.grid(row=0, column=1 )
        self.startSpeedLabel.grid(row=1, column=0)
        self.startSpeedEntry.grid(row=1, column=1)
        # Верстка кнопок
        self.btnBuild.grid(row=0, column=0)
        self.btnClear.grid(row=0, column=1, padx=10)
        self.btnLoadGraf.grid(row=0, column=0, padx=10)
        self.btnScreenShot.grid(row=0, column=1)
        self.btnSaveGraf.grid(row=0, column=2, sticky="e")

    def plot (self):
        
        arrX = []
        arrY = []
        a = int(self.angleEntry.get())
        Vo = int(self.startSpeedEntry.get())
        g = 10
        L = (((Vo**2)*sin(2*a))/g)
        
        for x in range(0, int(L)+1):
            y = ((tan(a)*x) - (g*(x**2))/(2*(Vo**2)*(cos(a)**2)))
            arrX.append(x)
            arrY.append(y)
        x = np.array (arrX)
        y = np.array (arrY)
        

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(x, y,color='blue')

        a.set_title ("BALISTA", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        #canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas = FigureCanvasTkAgg(fig, master=self.grafFrame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def clear(self):
        pass

    def loadGraf(self):
        pass

    def screenShot(self):
        pass

    def saveGraf(self):
        pass

window= Tk()
window.geometry("800x600")
window.title("Balista")
start= Balista(window)
window.mainloop()