
"""
*******************************************************************
                    Arquitectura de Computadores 2
*******************************************************************
        Programmer: 
                
                Yenira Chacon Molina
                
        Programming language: Python 3.8
        
        Version: 0.19b
        
        Last modified: 16/10/2020
        
        Description:    
                    Multiprocessor Simulator
*******************************************************************
"""

##IMPORTS##

import tkinter
import threading
import time
from numpy import random
import random as rand


###############################################################
#---------------------#GLOBAL VARIABLES#----------------------#
###############################################################

MEMORY_LIST = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stop_threads = False

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

#End simulation
##button = canvas.create_text(150, 650, text="END SIMULATION", font = "Arial")
##canvas.tag_bind(button, "<Button-1>", end)


canvas.pack()


#Function that initializes the processor    
def processor(idP):

    while(True):
        global stop_threads
        if stop_threads:
            break
        else:
            x = calculate_instruction()
            print(x)
            time.sleep(5)
        
###########################################################
#-----------------------#THREADING#-----------------------#
###########################################################
    
#Create threads to initialize the 4 processors
def create_threads():
    
    t1 = threading.Thread(target = processor, args = (1,)) 
    t2 = threading.Thread(target = processor, args = (2,))
    t3 = threading.Thread(target = processor, args = (3,))
    t4 = threading.Thread(target = processor, args = (4,))

    while(True):
        t1.start()  
        t2.start() 
        t3.start() 
        t4.start()
        top.update_idletasks()

###########################################################
#-----------------#INSTRUCTION GENERATOR#-----------------#
###########################################################

#Function that calculates Binomial distribution
def calculate_instruction():
    
    x = random.binomial(n=2, p=0.5, size=11)
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

#Fuction that reads from main memory
def read():
    direction = direction_generator()
    return("Reading in direction:" + str(direction))

#function that writes a data in main memory
def write():
    
    data = data_generator()
    direction = direction_generator()
    MEMORY_LIST[direction]= data
    draw_data(direction,data)
    
    print("MEMORY LIST:" + str(MEMORY_LIST))
    return("Writing in direction" + str(direction) + "data:" + str(data))

#Creates a calc function
def calc():
    return("calc")

###########################################################
#------------------#DIRECTION GENERATOR#------------------#
###########################################################

#Function that calculates direction with Poisson Distribution
def direction_generator():
    
    x = random.poisson(lam=9, size=20)
    l = list(x)
    
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = l.count(0), l.count(1), l.count(2), l.count(3), l.count(4), l.count(5), l.count(6), l.count(7), l.count(8), l.count(9), l.count(10), l.count(11), l.count(12), l.count(13), l.count(14), l.count(15)

    if(a >= b and a >=c and a >= d and a >= e and a >=f and a >= g and a >= h and a >= i and a >= j and a >= k and a >=l and a >= m and a >= n and a >= o and a >= p):
        return 0
    elif(b >= a and b >=c and b >= d and b >= e and b >=f and b >= g and b >= h and b >= i and b >= j and b >= k and b >= l and b >= m and b >= n and b >= o and b >=p):
        return 1
    elif(c >= a and c >= b and c >= d and c >= e and c >=f and c >= g and c >= h and c >= i and c >=j and c >= k and c >=l and c >= m and c >= n and c >= o and c >= p):
        return 2
    elif(d >= a and d >= b and d >= c and d >= e and d >= f and d >= g and d >= h and d >= i and d >= j and d >= k and d >= l and d >= m and d >= n and d >= o and d >= p):
        return 3
    elif(e >= a and e >= b and e >= c and e >= d and e >= f and e >= g and e >= h and e >= i and e >= j and e >= k and e >= l and e >= m and e >= n and e >= o and e >= p):
        return 4
    elif(f >= a and f >= b and f >= c and f >= d and f >= e and f >= g and f >= h and f >= i and f >= j and f >= k and f >= l and f >= m and f >= n and f >= o and f >= p):
        return 5
    elif(g >= a and g >= b and g >= c and g >= d and g >= e and g >= f and g >= h and g >= i and g >= j and g >= k and g >= l and g >= m and g >= n and g >= o and g >= p):
        return 6
    elif(h >= a and h >= b and h >= c and h >= d and h >= e and h >= f and h >= g and h >= i and h >= j and h >= k and h >= l and h >= m and h >= n and h >= o and h >= p):
        return 7
    elif(i >= a and i >= b and i >= c and i >= d and i >= e and i >= f and i >= g and i >= h and i >= j and i >= k and i >= l and i >= m and i >= n and i >= o and i >= p):
        return 8
    elif(j >= a and j >= b and j >= c and j >= d and j >= e and j >= f and j >= g and j >= h and j >= i and j >= k and j >= l and j >= m and j >= n and j >= o and j >= p):
        return 9
    elif(k >= a and k >= b and k >= c and k >= d and k >= e and k >= f and k >= g and k >= h and k >= i and k >= j and k >= l and k >= m and k >= n and k >= o and k >= p):
        return 10
    elif(l >= a and l >= b and l >= c and l >= d and l >= e and l >= f and l >= g and l >= h and l >= i and l >= j and l >= k and l >= m and l >= n and l >= o and l >= p):
        return 11
    elif(m >= a and m >= b and m >= c and m >= d and m >= e and m >= f and m >= g and m >= h and m >= i and m >= j and m >= k and m >= l and m >= n and m >= o and m >= p):
        return 12
    elif(n >= a and n >= b and n >= c and n >= d and n >= e and n >= f and n >= g and n >= h and n >= i and n >= j and n >= k and n >= l and n >= m and n >= o and n >= p):
        return 13
    elif(o >= a and o >= b and o >= c and o >= d and o >= e and o >= f and o >= g and o >= h and o >= i and o >= j and o >= k and o >= l and o >= m and o >= n and o >= p):
        return 14
    else:
        return 15

###########################################################
#---------------------#GENERATE DATA#---------------------#
###########################################################

def data_generator():
    
    data = rand.randrange(65535)
    return hex(data)

top.update()

def draw_data(pos,data):

    print("Esta es la posicion: " + str(pos))
    if(pos == 0):
        canvas.create_rectangle(1100, 50, 1200, 100, fill='#B180B6') #1
        canvas.create_text(1150, 73, text=str(data), font = "Arial")
    elif(pos == 1):
        canvas.create_rectangle(1100, 100, 1200, 150, fill='#B180B6') #2
        canvas.create_text(1150, 123, text=str(data), font = "Arial")
    elif(pos == 2):
        canvas.create_rectangle(1100, 150, 1200, 200, fill='#B180B6') #3
        canvas.create_text(1150, 173, text=str(data), font = "Arial")
    elif(pos == 3):
        canvas.create_rectangle(1100, 200, 1200, 250, fill='#B180B6') #4
        canvas.create_text(1150, 223, text=str(data), font = "Arial")
    elif(pos == 4):
        canvas.create_rectangle(1100, 250, 1200, 300, fill='#B180B6') #5
        canvas.create_text(1150, 273, text=str(data), font = "Arial")
    elif(pos == 5):
        canvas.create_rectangle(1100, 300, 1200, 350, fill='#B180B6') #6
        canvas.create_text(1150, 323, text=str(data), font = "Arial")
    elif(pos == 6):
        canvas.create_rectangle(1100, 350, 1200, 400, fill='#B180B6') #7
        canvas.create_text(1150, 373, text=str(data), font = "Arial")
    elif(pos == 7):
        canvas.create_rectangle(1100, 400, 1200, 450, fill='#B180B6') #8
        canvas.create_text(1150, 423, text=str(data), font = "Arial")
    elif(pos == 8):
        canvas.create_rectangle(1250, 50, 1350, 100, fill='#B180B6') #9
        canvas.create_text(1300, 73, text=str(data), font = "Arial")
    elif(pos == 9):
        canvas.create_rectangle(1250, 100, 1350, 150, fill='#B180B6') #10
        canvas.create_text(1300, 123, text=str(data), font = "Arial")
    elif(pos == 10):
        canvas.create_rectangle(1250, 150, 1350, 200, fill='#B180B6') #11
        canvas.create_text(1300, 173, text=str(data), font = "Arial")
    elif(pos == 11):
        canvas.create_rectangle(1250, 200, 1350, 250, fill='#B180B6') #12
        canvas.create_text(1300, 223, text=str(data), font = "Arial")
    elif(pos == 12):
        canvas.create_rectangle(1250, 250, 1350, 300, fill='#B180B6') #13
        canvas.create_text(1300, 273, text=str(data), font = "Arial")
    elif(pos == 13):
        canvas.create_rectangle(1250, 300, 1350, 350, fill='#B180B6') #14
        canvas.create_text(1300, 323, text=str(data), font = "Arial")
    elif(pos == 14):
        canvas.create_rectangle(1250, 350, 1350, 400, fill='#B180B6') #15
        canvas.create_text(1300, 373, text=str(data), font = "Arial")
    else:
        canvas.create_rectangle(1250, 400, 1350, 450, fill='#B180B6') #16
        canvas.create_text(1300, 423, text=str(data), font = "Arial")


top.mainloop()
