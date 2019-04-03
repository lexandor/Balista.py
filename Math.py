_author__ = 'Alexander Ometov aka PLEXER'
from config import *

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from math import *
from datetime import datetime

class Balista:
    def __init__(self,  window):
        self.window = window
        # Разметка фреймов
        self.varListFrame         = Frame(self.window)
        self.grafFrame            = Frame(self.window, width=500, height=500)
        self.controllerFrameLeft  = Frame(self.window)
        self.controllerFrameRight = Frame(self.window)
        # Разметка полей ввода
        self.angleLabel       = Label(self.varListFrame, text="A = ")
        self.angleEntry       = Entry(self.varListFrame) # Поле для ввода угла к горизонту
        self.startSpeedLabel  = Label(self.varListFrame, text="Vo = ")
        self.startSpeedEntry  = Entry(self.varListFrame) # Поле для ввода начальной скорости с которой бросили тело.
        self.massLabel        = Label(self.varListFrame, text="m =")
        self.massEntry        = Entry(self.varListFrame) # Поле для ввода массы
        self.timeLabel        = Label(self.varListFrame, text="t =")
        self.distanceLabel    = Label(self.varListFrame, text="L =")
        self.isWindy          = Checkbutton(self.varListFrame, text="Есть ли ветер?", state=ACTIVE)
        self.resistForceLabel = Label(self.varListFrame, text="Fсопр =")
        self.resistForceEntry = Entry(self.varListFrame)
        self.betaAngleLabel   = Label(self.varListFrame, text="B =")
        self.betaAngleEntry   = Entry(self.varListFrame)  
        self.viscosityLabel   = Label(self.varListFrame, text="k =")
        self.viscosityEntry   = Entry(self.varListFrame)

        # Разметка кнопок
        self.btnBuild      = Button (self.controllerFrameLeft, text="Построить", command=self.plot)
        self.btnClear      = Button (self.controllerFrameLeft, text="Очистить", command=self.clear)
        self.btnLoadGraf   = Button (self.controllerFrameRight, text="Загрузить график", command=self.loadGraf, state=DISABLED)
        self.btnScreenShot = Button (self.controllerFrameRight, text="|O|", command=self.screenShot, state=DISABLED)
        self.btnSaveGraf   = Button (self.controllerFrameRight, text="Сохранить график", command=self.saveGraf, state=DISABLED)
        # Верстка фреймов
        self.varListFrame.grid(row=0, column=0, sticky=NW, pady=40, padx=15)      
        self.grafFrame.grid(row=0, column=1, pady=20)
        self.controllerFrameLeft.grid(row=1, column=0, sticky=SW, padx=15)
        self.controllerFrameRight.grid(row=1, column=1, sticky=SE)
        # Верстка полей ввода
        self.angleLabel.grid(row=0, column=0)
        self.angleEntry.grid(row=0, column=1 )
        self.startSpeedLabel.grid(row=1, column=0)
        self.startSpeedEntry.grid(row=1, column=1)
        self.massLabel.grid(row=2, column=0)
        self.massEntry.grid(row=2, column=1)
        self.timeLabel.grid(row=3, column=0)
        self.distanceLabel.grid(row=4, column=0)
        self.isWindy.grid(row=5, columnspan=2)
        if self.isWindy:#.state() == ACTIVE: # NEED TO FIX, SOME BAG
            self.resistForceLabel.grid(row=6, column=0)
            self.resistForceEntry.grid(row=6, column=1)
            self.betaAngleLabel.grid(row=7, column=0)
            self.betaAngleEntry.grid(row=7, column=1)
            self.viscosityLabel.grid(row=8, column=0)
            self.viscosityEntry.grid(row=8, column=1)
        # Верстка кнопок
        self.btnBuild.grid(row=0, column=0)
        self.btnClear.grid(row=0, column=1, padx=10)
        self.btnLoadGraf.grid(row=0, column=0, padx=10)
        self.btnScreenShot.grid(row=0, column=1)
        self.btnSaveGraf.grid(row=0, column=2, sticky="e")    

    def plot (self):
        
        arrX = []
        arrY = []
        a    = int(self.angleEntry.get())
        Vo   = int(self.startSpeedEntry.get())
        #m    = int(self.massEntry.get())
        g    = 10 # g = (G*m*M)/((R+y)**2)
        L    = (((Vo**2)*sin(2*a))/g)
        self.distanceLabel.configure(text="L = " + str(round(L, 1)))
        for x in range(0, int(L)+1):
            y = ((tan(a)*x) - (g*(x**2))/(2*(Vo**2)*(cos(a)**2)))
            arrX.append(x)
            arrY.append(y)
        x = np.array (arrX)
        y = np.array (arrY)
        
        if logGraf == True:
            # логирует массив точек горафика в файл. Можно отключить в настройках(конфиге)
            file = open('log/'+datetime.now().strftime('%H_%M_%S')+'.txt', 'w')
            file.write(str(arrX) + '\n' + str(arrY))
            file.close

        fig = Figure(figsize=(7,5)) #66
        a = fig.add_subplot(111)
        a.plot(x, y,color='blue')

        #a.set_title ("BALISTA", fontsize=12)
        a.set_ylabel("Y", fontsize=10)
        a.set_xlabel("X", fontsize=10)

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
window.geometry(str(window_width)+'x'+str(window_heigth))
window.title("Balista")
start= Balista(window)
window.mainloop()