_author__ = 'ALeX'
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from math import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window) # alpha
        self.box2 = Entry(window) # Vo
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.box2.pack ()
        self.button.pack()

    def plot (self):
        
        arrX = []
        arrY = []
        a = int(self.box.get())
        Vo = int(self.box2.get())
        g = 10
        L = (((Vo**2)*sin(2*a))/g)
        
        for x in range(0, int(L)+1):
            y = ((tan(a)*x) - (g*(x**2))/(2*(Vo**2)*(cos(a)**2)))
            arrX.append(x)
            arrY.append(y)
        x= np.array (arrX)
        y= np.array (arrY)
        

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(x, y,color='blue')
       # a.invert_yaxis()

        a.set_title ("BALISTA", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

window= Tk()
start= mclass (window)
window.mainloop()