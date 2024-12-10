from tkinter import *
import time
import keyboard
from nau import *
from enemic import *



tk = Tk()

w = Canvas(tk, width = 800, height = 600)
w.pack()

enemics = []
enemics.append(Enemic(50,50,50,35,1))
enemics.append(Enemic(50,150,50,35,1.25)) 
enemics.append(Enemic(50,250,50,35,1.5))

projectils=[]

nau = Nau(400,500,40,25)

t = 0

while True:
    w.delete('all')
    #Aplicar moviments als elements
    if keyboard.is_pressed('left arrow'):
        nau.moure(-1)
    if keyboard.is_pressed('right arrow'):
        nau.moure(1)
    if keyboard.is_pressed('spacebar'):
        nau.dispara(projectils)
    for e in enemics:
        e.moure()      
        e.pinta(w)
    for p in projectils:
        p.moure()
        p.pinta(w)
    nau.pinta(w)
    
    w.update()
    #pausa
    time.sleep(5/100)#pausa durant els segons especificats
    #w.mainloop()
