


from tkinter import *

root = Tk()

varListFrame = Frame(root)
varListFrame.grid(row=0, column=0)

grafFrame = Frame(root, bg="black")
grafFrame.grid( row=0, column=1, pady=20)

controllerFrame = Frame(root)
controllerFrame.grid( row=1, column=0, columnspan=1)


angle = Label(varListFrame, text="Alpha =")
angle.grid( row=0, column=0)
angleEntry = Entry(varListFrame)
angleEntry.grid( row=0, column=1)

speedStart = Label(varListFrame, text="Vo =")
speedStart.grid( row=1, column=0)
speedStartEntry = Entry(varListFrame)
speedStartEntry.grid( row=1, column=1)

height = Label(varListFrame, text="h =")
height.grid( row=2, column=0)
heightEntry = Entry(varListFrame)
heightEntry.grid( row=2, column=1)

mass = Label(varListFrame, text="m =")
mass.grid( row=3, column=0)
massEntry = Entry(varListFrame)
massEntry.grid( row=3, column=1)

heightMax = Label(varListFrame, text="H =")
heightMax.grid( row=4, column=0)
heightMaxEntry = Entry(varListFrame)
heightMaxEntry.grid( row=4, column=1)


grafCanvas = Canvas(grafFrame, width=500, height=500, bg='white') 
grafCanvas.pack(pady = 1, padx = 1)
# Начало координат Х=10 Y=490
grafCanvas.create_line(10, 490, 490, 490, width=1, arrow=LAST) # X Ось
grafCanvas.create_line(10, 490, 10, 10, width=1, arrow=LAST) # Y Ось


btnClear = Button(controllerFrame, text="Clear")
btnClear.pack(side=LEFT)

btnBuild = Button(controllerFrame, text="Build")
btnBuild.pack(side=LEFT)

btnLoadGraf = Button(controllerFrame, text="loadGraf")
btnLoadGraf.pack(side=RIGHT)

btnScreenShot = Button(controllerFrame, text="|*|")
btnScreenShot.pack(side=RIGHT)

btnSaveGraf = Button(controllerFrame, text="SaveGraf")
btnSaveGraf.pack(side=RIGHT)







root.mainloop()