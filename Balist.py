


from Tkinter import *

root = Tk()

varListFrame = Frame(root)
varListFrame.grid(row=0, column=0)

grafFrame = Frame(root, bg="white")
grafFrame.grid( row=0, column=1)

controllerFrame = Frame(root)
controllerFrame.grid( row=1, column=1, columnspan=1)


angle = Label(varListFrame, text="Alpha =")
angle.pack()

speedStart = Label(varListFrame, text="Vo =")
speedStart.pack()

height = Label(varListFrame, text="h =")
height.pack()

mass = Label(varListFrame, text="m =")
mass.pack()

heightMax = Label(varListFrame, text="H =")
heightMax.pack()


grafCanvas = Canvas(grafFrame, border=2) 
grafCanvas.pack()


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