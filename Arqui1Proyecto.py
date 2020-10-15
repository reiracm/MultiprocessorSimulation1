
"""
*******************************************************************
                    Arquitectura de Computadores 2
*******************************************************************
        Programmer: 
                
                Yenira Chacon Molina
                
        Programming language: Python 3.9
        
        Version: 0.19b
        
        Last modified: 18/06/2020
        
        Description:    
                    Multiprocessor Simulator
*******************************************************************
"""

##IMPORTS##

import tkinter
import threading
from numpy import random

###############################################################
#--------------------#GRAPHICS AND EVENTS#--------------------#
###############################################################
    
top = tkinter.Tk(className = "-Multiprocessor Simulation-")

top.geometry("1400x700")

top.configure(bg = '#2C70A9')

#Function that starts the program
def start(event):
    create_threads()


#PROCESSORS

canvas = tkinter.Canvas(top, width=1400, height=700, bg = '#2C70A9')

canvas.create_rectangle(80, 70, 280, 300, fill='#7D8287')

canvas.create_rectangle(330, 70, 530, 300, fill='#7D8287')

canvas.create_rectangle(580, 70, 780, 300, fill='#7D8287')

canvas.create_rectangle(830, 70, 1030, 300, fill='#7D8287')

#CACHEL1

canvas.create_rectangle(100, 240, 260, 280, fill='#BDBDBD')

canvas.create_rectangle(350, 240, 510, 280, fill='#BDBDBD')

canvas.create_rectangle(600, 240, 760, 280, fill='#BDBDBD')

canvas.create_rectangle(850, 240, 1010, 280, fill='#BDBDBD')

#CONTROL

canvas.create_rectangle(100, 100, 150, 220, fill='#8A0829')

canvas.create_rectangle(350, 100, 400, 220, fill='#8A0829')

canvas.create_rectangle(600, 100, 650, 220, fill='#8A0829')

canvas.create_rectangle(850, 100, 900, 220, fill='#8A0829')

#CPU

canvas.create_rectangle(165, 100, 260, 220, fill='#6A0888')

canvas.create_rectangle(415, 100, 510, 220, fill='#6A0888')

canvas.create_rectangle(670, 100, 760, 220, fill='#6A0888')

canvas.create_rectangle(915, 100, 1010, 220, fill='#6A0888')


#BUS

canvas.create_rectangle(80, 400, 1030, 450, fill='#7D8287')



#MEMORY

canvas.create_rectangle(470, 550, 670, 620, fill='#7D8287')

canvas.create_rectangle(1100, 50, 1200, 100, fill='#B180B6') #1

canvas.create_rectangle(1100, 100, 1200, 150, fill='#B180B6') #2

canvas.create_rectangle(1100, 150, 1200, 200, fill='#B180B6') #3

canvas.create_rectangle(1100, 200, 1200, 250, fill='#B180B6') #4

canvas.create_rectangle(1100, 250, 1200, 300, fill='#B180B6') #5
    
canvas.create_rectangle(1100, 300, 1200, 350, fill='#B180B6') #6

canvas.create_rectangle(1100, 350, 1200, 400, fill='#B180B6') #7

canvas.create_rectangle(1100, 400, 1200, 450, fill='#B180B6') #8

canvas.create_rectangle(1250, 50, 1350, 100, fill='#B180B6') #9

canvas.create_rectangle(1250, 100, 1350, 150, fill='#B180B6') #10

canvas.create_rectangle(1250, 150, 1350, 200, fill='#B180B6') #11

canvas.create_rectangle(1250, 200, 1350, 250, fill='#B180B6') #12

canvas.create_rectangle(1250, 250, 1350, 300, fill='#B180B6') #13
    
canvas.create_rectangle(1250, 300, 1350, 350, fill='#B180B6') #14

canvas.create_rectangle(1250, 350, 1350, 400, fill='#B180B6') #15

canvas.create_rectangle(1250, 400, 1350, 450, fill='#B180B6') #16



#LINES

canvas.create_line(180, 300, 180, 400)

canvas.create_line(430, 300, 430, 400)

canvas.create_line(680, 300, 680, 400)

canvas.create_line(930, 300, 930, 400)

canvas.create_line(570, 450, 570, 550)

#BUTTONS

#Initialize simulation
button = canvas.create_text(150, 600, text="START SIMULATION", font = "Arial")
canvas.tag_bind(button, "<Button-1>", start)

#Opens Memory Window to check spaces
##button = canvas.create_text(570, 583, text="MEMORY", font = "Arial")
##canvas.tag_bind(button, "<Button-1>", openMemoryWindow)

canvas.pack()


###########################################################
#-----------------------#THREADING#-----------------------#
###########################################################

#Create threads to initialize the 4 processors
def create_threads():
    
    t1 = threading.Thread(target = processor, args = (1,)) 
    t2 = threading.Thread(target = processor, args = (2,))
    t3 = threading.Thread(target = processor, args = (3,))
    t4 = threading.Thread(target = processor, args = (4,))
   
    t1.start()  
    t2.start() 
    t3.start() 
    t4.start()
  
    t1.join() 
    t2.join()
    t3.join()
    t4.join()
  
    # Threads successfully executed 
    print("Processors executed!")

#Function that initializes the processor    
def processor(idP):
    
    if (idP == 1):
        print("Es el procesador 1")
    elif (idP == 2):
        print("Es el procesador 2")
    elif (idP == 3):
        print("Es el procesador 3")
    else:
        print("Es el procesador 4")

###########################################################
#-----------------#INSTRUCTION GENERATOR#-----------------#
###########################################################

#Function that calculates Binomial distribution
def calculate_instruction():
    
    x = random.binomial(n=2, p=0.5, size=10)
    print(x)
    calcCounter = 0
    readCounter = 0
    writeCounter = 0
    i = 0

    while(i<=9):

        if(x[i] == 0):
            calcCounter += 1
        elif(x[i] == 1):
            readCounter += 1
        else:
            writeCounter += 1
        i += 1
    if(calcCounter>=readCounter and calcCounter>=writeCounter):
        return calc()
    elif(readCounter>=calcCounter and readCounter>=writeCounter):
        return read()
    else:
        return write()




def read():
    print("read")

def write():
    print("write")

def calc():
    print("calc")

top.mainloop()


