

from math import *
from tkinter import *

root = Tk()
root.title('Balista.py')
root.geometry("800x600")

varListFrame = Frame(root)
varListFrame.grid(row=0, column=0, sticky=NW, pady=40, padx=15)

grafFrame = Frame(root, bg="black")
grafFrame.grid( row=0, column=1, pady=20)

controllerFrameLeft = Frame(root)
controllerFrameLeft.grid(row=1, column=0, sticky=SW, padx=15)
controllerFrameRight = Frame(root)
controllerFrameRight.grid(row=1, column=1, sticky=SE)

angle = Label(varListFrame, text="Alpha =")
angle.grid( row=0, column=0)
angleEntry = Entry(varListFrame)
angleEntry.grid( row=0, column=1)

speedStart = Label(varListFrame, text="Vo =")
speedStart.grid( row=1, column=0)
speedStartEntry = Entry(varListFrame)
speedStartEntry.grid( row=1, column=1)

time = Label(varListFrame, text="t =")
time.grid( row=2, column=0)
timeEntry = Entry(varListFrame)
timeEntry.grid( row=2, column=1)

height = Label(varListFrame, text="h =")
height.grid( row=3, column=0)
heightEntry = Entry(varListFrame)
heightEntry.grid( row=3, column=1)

mass = Label(varListFrame, text="m =")
mass.grid( row=4, column=0)
massEntry = Entry(varListFrame)
massEntry.grid( row=4, column=1)

heightMax = Label(varListFrame, text="H =")
heightMax.grid( row=5, column=0)
heightMaxEntry = Entry(varListFrame)
heightMaxEntry.grid( row=5, column=1)


grafCanvas = Canvas(grafFrame, width=500, height=500, bg='white') 
grafCanvas.pack(pady = 1, padx = 1)
# Начало координат Х=10 Y=490
grafCanvas.create_line(10, 490, 490, 490, width=1, arrow=LAST) # X Ось
grafCanvas.create_line(10, 490, 10, 10, width=1, arrow=LAST) # Y Ось





x = 10
y = 490

def graf_dot():
    #global x
    #global y
    #print(" global y : " + str(y))
    #print(" global x : " + str(x))

    #== Получение значений из полей
    Vo = int(speedStartEntry.get())
    t  = int(timeEntry.get())
    m  = int(massEntry.get())
    h  = int(heightEntry.get())
    H  = int(heightMaxEntry.get())
    a  = int(angleEntry.get())
    g  = 10
    
    L = (((Vo**2)*sin(2*a))/g) # Длинна полета
    k = L/490 # Коэффицент отображения, нужен чтобя график уместился на холсте

    #начало координат:
    #xo = 10
    #yo = 490
    
    #formula -->  y = (tan(a)*x) - (g*(x**2))/(2*(Vo**2)*(cos(a)**2))
 

    for x in range(0, 490):
        y = 490 - ((tan(a)*x) - (g*(x**2))/(2*(Vo**2)*(cos(a)**2)))
        
        if (y == 491):
            break
        else:
            grafCanvas.create_oval(x + 10, y, x + 10, y, width=1, outline="black")
        print(x)
        print(y)
    
    #grafCanvas.create_oval(k * x, k * y, k * x, k * y, width=1, outline="black")

    #root.after(1, graf_dot)

def clearGraf():
    grafCanvas.delete("all")
    grafCanvas.create_line(10, 490, 490, 490, width=1, arrow=LAST) # X Ось
    grafCanvas.create_line(10, 490, 10, 10, width=1, arrow=LAST) # Y Ось

btnBuild = Button(controllerFrameLeft, text="Build", command=graf_dot)
btnBuild.grid(row=0, column=0)

btnClear = Button(controllerFrameLeft, text="Clear", command=clearGraf)
btnClear.grid(row=0, column=1, padx=10)

btnLoadGraf = Button(controllerFrameRight, text="loadGraf")
btnLoadGraf.grid(row=0, column=0, padx=10)

btnScreenShot = Button(controllerFrameRight, text="|*|")
btnScreenShot.grid(row=0, column=1)

btnSaveGraf = Button(controllerFrameRight, text="SaveGraf")
btnSaveGraf.grid(row=0, column=2, sticky=E)







root.mainloop()