
"""
*******************************************************************
                    Arquitectura de Computadores 2
*******************************************************************
        Programmer: 
                
                Yenira Chacon Molina
                
        Programming language: Python 3.9
        
        Version: 0.19b
        
        Last modified: 17/10/2020
        
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

MEMORY_LIST = [0,"0xFFFF",0,0,0,0,0,0,0,0,0,0,0,0,0,0]

CACHE1 = [0,0,0,0]
CACHE2 = [0,0,0,0]
CACHE3 = [0,0,0,0]
CACHE4 = [0,0,0,0]

CACHE1_VALID = [1,0,1,1]
CACHE2_VALID = [0,0,0,0]
CACHE3_VALID = [0,0,0,0]
CACHE4_VALID = [0,0,0,0]

CACHE1_DIR = [0,0,3,7]
CACHE2_DIR = [0,0,0,0]
CACHE3_DIR = [0,0,0,0]
CACHE4_DIR = [0,0,0,0]

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

canvas = tkinter.Canvas(top, width=1400, height=700, bg = '#2C70A9')


#CACHEL1
def gen_cache_and_processors():
    xp1, xc1 = 50,55
    xp2,xc2 = 295,290
    i = 0

    while(i<4):
        canvas.create_rectangle(xp1, 10, xp2, 300, fill='#7D8287')
        canvas.create_rectangle(xc1, 110, xc2, 230, fill='#BDBDBD')
        xp1 += 250
        xc1 += 250
        xp2 += 250
        xc2 += 250
        i += 1

#CACHE COLUMNS

def cache_columns():
    yv1 = 110
    yv2 = 140
    x1, x2 = 55,85
    i = 0
    j=0
    while(j<4):
        while(i<4):
            canvas.create_rectangle(x1, yv1, x2, yv2, fill='#BDBDBD')
            yv1 += 30
            yv2 += 30
            i += 1

        i = 0
        yv1 = 110
        yv2 = 140
        x1 += 250
        x2 += 250
        j+=1

def cache_mem_columns():
    yv1 = 110
    yv2 = 140
    x1, x2 = 85,180
    i = 0
    j=0
    while(j<4):
        while(i<4):
            canvas.create_rectangle(x1, yv1, x2, yv2, fill='#BDBDBD')
            yv1 += 30
            yv2 += 30
            i += 1

        i = 0
        yv1 = 110
        yv2 = 140
        x1 += 250
        x2 += 250
        j+=1

#CACHE DATA

def cache_draw():
    yv1 = 110
    yv2 = 140
    x1, x2 = 180,275
    i = 0
    j=0
    while(j<4):
        while(i<4):
            canvas.create_rectangle(x1, yv1, x2, yv2, fill='#BDBDBD')
            yv1 += 30
            yv2 += 30
            i += 1

        i = 0
        yv1 = 110
        yv2 = 140
        x1 += 250
        x2 += 250
        j+=1

#CONTROL
def draw_control():
    x1,x2 = 100,150
    i = 0
    while(i<4):
        canvas.create_rectangle(x1, 20, x2, 80, fill='#8A0829')
        x1 += 250
        x2 += 250
        i += 1

#CPU
def draw_cpu():
    x1,x2 = 165,260
    i = 0
    while(i<4):
        canvas.create_rectangle(x1, 20, x2, 70, fill='#6A0888')
        x1 += 250
        x2 += 250
        i += 1

#BUS

canvas.create_rectangle(80, 400, 1030, 450, fill='#7D8287')
canvas.create_rectangle(470, 550, 670, 620, fill='#7D8287')

#MEMORY

def draw_mem():
    x1,x2 = 1100, 1200
    y1,y2 = 100, 150
    i = 0
    j = 0
    while(j < 3):
        while(i < 8):

            canvas.create_rectangle(x1, y1, x2, y2, fill='#B180B6') #1
            y1 += 50
            y2 += 50
            i += 1
            
        y1,y2 = 100,150
        x1 += 150
        x2 += 150
        j += 1
        i = 0
#LINES
def draw_lines():
    x = 180
    i = 0
    while(i<4):
        canvas.create_line(x, 300, x, 400)
        x += 250
        i += 1

#DRAW CACHE VALUES
def draw_cache_values():
    x,y = 65,120
    k = 0
    j = 0
    for i in range(len(CACHE1_VALID)):
        
        canvas.create_text(x, y, text= str(CACHE1_VALID[i]), font = "Lucida")   
        canvas.create_text(x+250, y, text= str(CACHE2_VALID[i]), font = "Lucida")
        canvas.create_text(x+500, y, text= str(CACHE3_VALID[i]), font = "Lucida")        
        canvas.create_text(x+750, y, text= str(CACHE4_VALID[i]), font = "Lucida")        
        y += 30

#DRAW MEMORY VALUES
def draw_mem_values():
    x,y = 120,120
    k = 0
    j = 0
    for i in range(len(CACHE1_DIR)):
        
        canvas.create_text(x, y, text= str(bin(CACHE1_DIR[i])), font = "Lucida")   
        canvas.create_text(x+250, y, text= str(bin(CACHE2_DIR[i])), font = "Lucida")
        canvas.create_text(x+500, y, text= str(bin(CACHE3_DIR[i])), font = "Lucida")        
        canvas.create_text(x+750, y, text= str(bin(CACHE4_DIR[i])), font = "Lucida")        
        y += 30

#DRAW DATA VALUES
def draw_data_values():
    x,y = 230,120
    k = 0
    j = 0
    for i in range(len(CACHE1_DIR)):
        
        canvas.create_text(x, y, text= str(hex(CACHE1[i])), font = "Lucida")   
        canvas.create_text(x+250, y, text= str(hex(CACHE2[i])), font = "Lucida")
        canvas.create_text(x+500, y, text= str(hex(CACHE3[i])), font = "Lucida")        
        canvas.create_text(x+750, y, text= str(hex(CACHE4[i])), font = "Lucida")        
        y += 30

gen_cache_and_processors()
cache_columns()
cache_mem_columns()
cache_draw()
draw_control()
draw_cpu()
draw_mem()
draw_lines()
draw_cache_values()
draw_mem_values()
draw_data_values()
canvas.create_line(570, 450, 570, 550)

#BUTTONS

#Initialize simulation
button = canvas.create_text(150, 600, text="START SIMULATION", font = "Arial")
canvas.tag_bind(button, "<Button-1>", start)
canvas.pack()

#Function that initializes the processor    
def processor(idP):

    while(True):
        global stop_threads
        if stop_threads:
            break
        else:
            x = calculate_instruction(idP)
            print(x)
            time.sleep(2)
        
###########################################################
#-----------------------#THREADING#-----------------------#
###########################################################
    
#Create threads to initialize the 4 processors
def create_threads():
    
    t1 = threading.Thread(target = processor, args = (1,)) 
    t2 = threading.Thread(target = processor, args = (2,))
   # t3 = threading.Thread(target = processor, args = (3,))
    #t4 = threading.Thread(target = processor, args = (4,))

    while(True):
        t1.start()  
        t2.start() 
       # t3.start() 
       # t4.start()
        top.update_idletasks()

###########################################################
#-----------------#INSTRUCTION GENERATOR#-----------------#
###########################################################

#Function that calculates Binomial distribution
def calculate_instruction(ID):
    
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
        return read(ID,direction_generator())
    elif(readCounter>=calcCounter and readCounter>=writeCounter):
        return calc(ID)
    else:
        return write(ID,direction_generator(),data_generator())

###########################################################
#-------------#READ, WRITE AND CALC FUNCTION#-------------#
###########################################################
    
#Fuction that reads from cache
def read(procID,direction):
    draw_processor_id(procID,direction,0)
    if(procID == 1):                #Processor 1
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE1_DIR[0] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE1[0]                            #Return read value
                else:                                           #Invalid bit
                    CACHE1_DIR[0] = direction                   #Write direction in cache
                    CACHE1[0]= MEMORY_LIST[direction]           #Update value
                    CACHE1_VALID[0] = 1
                    draw_cache_valid(procID,0)
                    
            if(CACHE1_DIR[1] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE1[1]                            #Return read value
                else:                                           #Invalid bit
                    CACHE1_DIR[1] = direction                   #Write direction in cache
                    CACHE1[1]= MEMORY_LIST[direction]           #Update value
                    CACHE1_VALID[1] = 1
                    draw_cache_valid(procID,1)
            else:
                MEMORY_LIST[CACHE1_DIR[0]]=CACHE1[0]        #Save the value in memory before replacing it
                CACHE1[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE1_DIR[0] = direction                    #Replace new direction
                CACHE1_VALID[0] = 1                          #Bit valid now
                draw_cache_valid(procID,0)

        if(direction%2 == 1):                                   #Is direction %2?
            if(CACHE1_DIR[2] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE1[2]                            #Return read value
                else:                                           #Invalid bit
                    CACHE1_DIR[2] = direction                   #Write direction in cache
                    CACHE1[2]= MEMORY_LIST[direction]           #Update value
                    CACHE1_VALID[2] = 1
                    draw_cache_valid(procID,2)
                    
            elif(CACHE1_DIR[3] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE1[3]                            #Return read value
                else:                                           #Invalid bit
                    CACHE1_DIR[3] = direction                   #Write direction in cache
                    CACHE1[3]= MEMORY_LIST[direction]           #Update value
                    CACHE1_VALID[3] = 1
                    draw_cache_valid(procID,3)
            else:
                MEMORY_LIST[CACHE1_DIR[2]]=CACHE1[2]        #Save the value in memory before replacing it
                CACHE1[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE1_DIR[2] = direction                    #Replace new direction
                CACHE1_VALID[2] = 1                          #Bit valid now
                draw_cache_valid(procID,2)
                
    if(procID == 2):                #Processor 2
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE2_DIR[0] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE2[0]                            #Return read value
                else:                                           #Invalid bit
                    CACHE2_DIR[0] = direction                   #Write direction in cache
                    CACHE2[0]= MEMORY_LIST[direction]           #Update value
                    CACHE2_VALID[0] = 1
                    draw_cache_valid(procID,0)

                    
            elif(CACHE2_DIR[1] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE2[1]                            #Return read value
                else:                                           #Invalid bit
                    CACHE2_DIR[1] = direction                   #Write direction in cache
                    CACHE2[1]= MEMORY_LIST[direction]           #Update value
                    CACHE2_VALID[1] = 1
                    draw_cache_valid(procID,1)

            else:
                MEMORY_LIST[CACHE2_DIR[0]]=CACHE2[1]        #Save the value in memory before replacing it
                CACHE2[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE2_DIR[0] = direction                    #Replace new direction
                CACHE2_VALID[0] = 1                          #Bit valid now
                draw_cache_valid(procID,0)

       
                
        if(direction%2 == 1):                                   #Is direction %2?
            if(CACHE2_DIR[2] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE2[2]                            #Return read value
                else:                                           #Invalid bit
                    CACHE2_DIR[2] = direction                   #Write direction in cache
                    CACHE2[2]= MEMORY_LIST[direction]           #Update value
                    CACHE2_VALID[2] = 1
                    draw_cache_valid(procID,2)

                    
            elif(CACHE2_DIR[3] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE2[3]                            #Return read value
                else:                                           #Invalid bit
                    CACHE2_DIR[3] = direction                   #Write direction in cache
                    CACHE2[3]= MEMORY_LIST[direction]           #Update value
                    CACHE2_VALID[3] = 1
                    draw_cache_valid(procID,3)

            else:
                MEMORY_LIST[CACHE2_DIR[2]]=CACHE2[2]        #Save the value in memory before replacing it
                CACHE2[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE2_DIR[2] = direction                    #Replace new direction
                CACHE2_VALID[2] = 1                          #Bit valid now
                draw_cache_valid(procID,2)


    if(procID == 3):                #Processor 3
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE3_DIR[0] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE3[0]                            #Return read value
                else:                                           #Invalid bit
                    CACHE3_DIR[0] = direction                   #Write direction in cache
                    CACHE3[0]= MEMORY_LIST[direction]           #Update value
                    CACHE3_VALID[0] = 1
                    draw_cache_valid(procID,0)

                    
            elif(CACHE3_DIR[1] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE3[1]                            #Return read value
                else:                                           #Invalid bit
                    CACHE3_DIR[1] = direction                   #Write direction in cache
                    CACHE3[1]= MEMORY_LIST[direction]           #Update value
                    CACHE3_VALID[1] = 1
                    draw_cache_valid(procID,1)

            else:
                MEMORY_LIST[CACHE3_DIR[0]]=CACHE3[1]        #Save the value in memory before replacing it
                CACHE3[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE3_DIR[0] = direction                    #Replace new direction
                CACHE3_VALID[0] = 1                          #Bit valid now
                draw_cache_valid(procID,0)

                
        if(direction%2 == 1):                                   #Is direction %2?
            if(CACHE3_DIR[2] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE3[2]                            #Return read value
                else:                                           #Invalid bit
                    CACHE3_DIR[2] = direction                   #Write direction in cache
                    CACHE3[2]= MEMORY_LIST[direction]           #Update value
                    CACHE3_VALID[2] = 1
                    draw_cache_valid(procID,2)

                    
            elif(CACHE3_DIR[3] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE3[3]                            #Return read value
                else:                                           #Invalid bit
                    CACHE3_DIR[3] = direction                   #Write direction in cache
                    CACHE3[3]= MEMORY_LIST[direction]           #Update value
                    CACHE3_VALID[3] = 1
                    draw_cache_valid(procID,3)

            else:
                MEMORY_LIST[CACHE3_DIR[2]]=CACHE3[2]        #Save the value in memory before replacing it
                CACHE3[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE3_DIR[2] = direction                    #Replace new direction
                CACHE3_VALID[2] = 1                          #Bit valid now
                draw_cache_valid(procID,2)

                
    if(procID == 4):                #Processor 4
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE4_DIR[0] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE4[0]                            #Return read value
                else:                                           #Invalid bit
                    CACHE4_DIR[0] = direction                   #Write direction in cache
                    CACHE4[0]= MEMORY_LIST[direction]           #Update value
                    CACHE4_VALID[0] = 1
                    draw_cache_valid(procID,0)

                    
            elif(CACHE4_DIR[1] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE4[1]                            #Return read value
                else:                                           #Invalid bit
                    CACHE4_DIR[1] = direction                   #Write direction in cache
                    CACHE4[1]= MEMORY_LIST[direction]           #Update value
                    CACHE4_VALID[1] = 1
                    draw_cache_valid(procID,1)

            else:
                MEMORY_LIST[CACHE4_DIR[0]]=CACHE4[1]        #Save the value in memory before replacing it
                CACHE4[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE4_DIR[0] = direction                    #Replace new direction
                CACHE4_VALID[0] = 1                          #Bit valid now
                draw_cache_valid(procID,0)

                
        if(direction%2 == 1):                                   #Is direction %2?
            if(CACHE4_DIR[2] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE4[2]                            #Return read value
                else:                                           #Invalid bit
                    CACHE4_DIR[2] = direction                   #Write direction in cache
                    CACHE4[2]= MEMORY_LIST[direction]           #Update value
                    CACHE4_VALID[2] = 1
                    draw_cache_valid(procID,2)

                    
            elif(CACHE4_DIR[3] == direction):                     #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    return CACHE4[3]                            #Return read value
                else:                                           #Invalid bit
                    CACHE4_DIR[3] = direction                   #Write direction in cache
                    CACHE4[3]= MEMORY_LIST[direction]           #Update value
                    CACHE4_VALID[3] = 1
                    draw_cache_valid(procID,3)

            else:
                MEMORY_LIST[CACHE4_DIR[2]]=CACHE4[2]        #Save the value in memory before replacing it
                CACHE4[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE4_DIR[2] = direction                    #Replace new direction
                CACHE4_VALID[2] = 1                          #Bit valid now
                draw_cache_valid(procID,2)


#Write Function
def write(procID,direction,data):
    draw_processor_id(procID,direction,data)
    if(procID == 1):                    #Processor 1
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE1_DIR[0] == direction):                      #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    CACHE1[0] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE1[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE1_DIR[0] = direction                    #Replace new direction
                    CACHE1_VALID[0] = 1                          #Bit valid now
                    CACHE1[0] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,0)

            elif(CACHE1_DIR[1] == direction):                    #Is it in the second position?
                if(validate_bit(procID,1)):                     #Is bit valid?
                    CACHE1[1] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE1[1] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE1_DIR[1] = direction                    #Replace new direction
                    CACHE1_VALID[1] = 1                          #Bit valid now
                    CACHE1[1] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,1)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE1_DIR[0]]=CACHE1[1]        #Save the value in memory before replacing it
                CACHE1[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE1_DIR[0] = direction                    #Replace new direction
                CACHE1_VALID[0] = 1                          #Bit valid now
                CACHE1[0] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,0)     
                
        if(direction%2 == 1):                                   #Is direction %2?
            
            if(CACHE1_DIR[2] == direction):                      #Is it in the first position?
                if(validate_bit(procID,2)):                     #Is bit valid?
                    CACHE1[2] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE1[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE1_DIR[2] = direction                    #Replace new direction
                    CACHE1_VALID[2] = 1                          #Bit valid now
                    CACHE1[2] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,2)

                    
            elif(CACHE1_DIR[3] == direction):                    #Is it in the second position?
                if(validate_bit(procID,3)):                     #Is bit valid?
                    CACHE1[3] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE1[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE1_DIR[3] = direction                    #Replace new direction
                    CACHE1_VALID[3] = 1                          #Bit valid now
                    CACHE1[3] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,3)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE1_DIR[3]]=CACHE1[3]        #Save the value in memory before replacing it
                CACHE1[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE1_DIR[3] = direction                    #Replace new direction
                CACHE1_VALID[3] = 1                          #Bit valid now
                CACHE1[3] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,3)


    if(procID == 2):                    #Processor 2
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE2_DIR[0] == direction):                      #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    CACHE2[0] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE2[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE2_DIR[0] = direction                    #Replace new direction
                    CACHE2_VALID[0] = 1                          #Bit valid now
                    CACHE2[0] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,0)
     
            elif(CACHE2_DIR[1] == direction):                    #Is it in the second position?
                if(validate_bit(procID,1)):                     #Is bit valid?
                    CACHE2[1] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE2[1] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE2_DIR[1] = direction                    #Replace new direction
                    CACHE2_VALID[1] = 1                          #Bit valid now
                    CACHE2[1] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,1)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE2_DIR[0]]=CACHE2[0]        #Save the value in memory before replacing it
                CACHE2[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE2_DIR[0] = direction                    #Replace new direction
                CACHE2_VALID[0] = 1                          #Bit valid now
                CACHE2[0] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,0)

                
        if(direction%2 == 1):                                   #Is direction %2?
            
            if(CACHE2_DIR[2] == direction):                      #Is it in the first position?
                if(validate_bit(procID,2)):                     #Is bit valid?
                    CACHE2[2] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE2[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE2_DIR[2] = direction                    #Replace new direction
                    CACHE2_VALID[2] = 1                          #Bit valid now
                    CACHE2[2] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,2)

            elif(CACHE2_DIR[3] == direction):                    #Is it in the second position?
                if(validate_bit(procID,3)):                     #Is bit valid?
                    CACHE2[3] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE2[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE2_DIR[3] = direction                    #Replace new direction
                    CACHE2_VALID[3] = 1                          #Bit valid now
                    CACHE2[3] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,3)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE2_DIR[3]]=CACHE2[3]        #Save the value in memory before replacing it
                CACHE2[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE2_DIR[3] = direction                    #Replace new direction
                CACHE2_VALID[3] = 1                          #Bit valid now
                CACHE2[3] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,3)

                             
    if(procID == 3):                    #Processor 3
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE3_DIR[0] == direction):                      #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    CACHE3[0] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE3[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE3_DIR[0] = direction                    #Replace new direction
                    CACHE3_VALID[0] = 1                          #Bit valid now
                    CACHE3[0] = data                           #Replaces new value with the new data
                    
            elif(CACHE3_DIR[1] == direction):                    #Is it in the second position?
                if(validate_bit(procID,1)):                     #Is bit valid?
                    CACHE3[1] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE3[1] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE3_DIR[1] = direction                    #Replace new direction
                    CACHE3_VALID[1] = 1                          #Bit valid now
                    CACHE3[1] = data                           #Replaces new value with the new data
            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE3_DIR[0]]=CACHE3[0]        #Save the value in memory before replacing it

                CACHE3[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE3_DIR[0] = direction                    #Replace new direction
                CACHE3_VALID[0] = 1                          #Bit valid now
                CACHE3[0] = data                           #Replaces new value with the new data                
                
        if(direction%2 == 1):                                   #Is direction %2?
            
            if(CACHE3_DIR[2] == direction):                      #Is it in the first position?
                if(validate_bit(procID,2)):                     #Is bit valid?
                    CACHE3[2] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE3[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE3_DIR[2] = direction                    #Replace new direction
                    CACHE3_VALID[2] = 1                          #Bit valid now
                    CACHE3[2] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,2)

                    
            elif(CACHE3_DIR[3] == direction):                    #Is it in the second position?
                if(validate_bit(procID,3)):                     #Is bit valid?
                    CACHE3[3] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE3[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE3_DIR[3] = direction                    #Replace new direction
                    CACHE3_VALID[3] = 1                          #Bit valid now
                    CACHE3[3] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,3)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE3_DIR[3]]=CACHE3[3]        #Save the value in memory before replacing it
                CACHE3[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE3_DIR[3] = direction                    #Replace new direction
                CACHE3_VALID[3] = 1                          #Bit valid now
                CACHE3[3] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,3)

                             
    if(procID == 4):                    #Processor 4
        if(direction%2 == 0):                                   #Is direction %2?
            if(CACHE4_DIR[0] == direction):                      #Is it in the first position?
                if(validate_bit(procID,0)):                     #Is bit valid?
                    CACHE4[0] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE4[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE4_DIR[0] = direction                    #Replace new direction
                    CACHE4_VALID[0] = 1                          #Bit valid now
                    CACHE4[0] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,0)

                    
            elif(CACHE4_DIR[1] == direction):                    #Is it in the second position?
                if(validate_bit(procID,1)):                     #Is bit valid?
                    CACHE4[1] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE4[1] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE4_DIR[1] = direction                    #Replace new direction
                    CACHE4_VALID[1] = 1                          #Bit valid now
                    CACHE4[1] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,1)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE4_DIR[0]]=CACHE4[0]        #Save the value in memory before replacing it

                CACHE4[0] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE4_DIR[0] = direction                    #Replace new direction
                CACHE4_VALID[0] = 1                          #Bit valid now
                CACHE4[0] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,0)

                
        if(direction%2 == 1):                                   #Is direction %2?
            
            if(CACHE4_DIR[2] == direction):                      #Is it in the first position?
                if(validate_bit(procID,2)):                     #Is bit valid?
                    CACHE4[2] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE4[2] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE4_DIR[2] = direction                    #Replace new direction
                    CACHE4_VALID[2] = 1                          #Bit valid now
                    CACHE4[2] = data                           #Replaces new value with the new data
                    
            elif(CACHE4_DIR[3] == direction):                    #Is it in the second position?
                if(validate_bit(procID,3)):                     #Is bit valid?
                    CACHE4[3] = data                           #Replaces new value with the new data

                else:                                           #If bit invalid we have to go to memory and bring it
                    CACHE4[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                    CACHE4_DIR[3] = direction                    #Replace new direction
                    CACHE4_VALID[3] = 1                          #Bit valid now
                    CACHE4[3] = data                           #Replaces new value with the new data
                    draw_cache_valid(procID,3)

            else:                                               #Is not in any of the positions
                MEMORY_LIST[CACHE4_DIR[3]]=CACHE4[3]        #Save the value in memory before replacing it
                CACHE4[3] = MEMORY_LIST[direction]          #Cache is replaced by memory value
                CACHE4_DIR[3] = direction                    #Replace new direction
                CACHE4_VALID[3] = 1                          #Bit valid now
                CACHE4[3] = data                           #Replaces new value with the new data
                draw_cache_valid(procID,3)

                
#Function that validates each bit
def validate_bit(procID, index):
    if(procID == 1):                    #Processor 1
        if(CACHE1_VALID[index] == 0):   #Is the bit invalid?
            return False
        else:
            return True
    if(procID == 2):                    #Processor 2
        if(CACHE2_VALID[index] == 0):   #Is the bit invalid?
            return False
        else:
            return True
    if(procID == 3):                    #Processor 1
        if(CACHE3_VALID[index] == 0):   #Is the bit invalid?
            return False
        else:
            return True
    if(procID == 4):                    #Processor 1
        if(CACHE4_VALID[index] == 0):   #Is the bit invalid?
            return False
        else:
            return True
        
#Function that searches in list
def search(list,data):
    for i in range(len(list)):
        if list[i] == data:
            return i
    return False
    

#Creates a calc function
def calc(procID):
    draw_processor_id(procID,0,0)
    return("calc")

#Snooping function
def snooping(procID,direction):
    if(procID == 1):
        if(search(CACHE2_DIR,direction) != False):
            CACHE2_VALID[search(CACHE2_DIR,direction)] = 0
        if(search(CACHE3_DIR,direction) != False):
            CACHE3_VALID[search(CACHE3_DIR,direction)] = 0
        if(search(CACHE4_DIR,direction) != False):
            CACHE4_VALID[search(CACHE4_DIR,direction)] = 0
        else:
            return 0
    if(procID == 2):
        if(search(CACHE1_DIR,direction) != False):
            CACHE1_VALID[search(CACHE1_DIR,direction)] = 0
        if(search(CACHE3_DIR,direction) != False):
            CACHE3_VALID[search(CACHE3_DIR,direction)] = 0
        if(search(CACHE4_DIR,direction) != False):
            CACHE4_VALID[search(CACHE4_DIR,direction)] = 0
        else:
            return 0
    if(procID == 3):
        if(search(CACHE1_DIR,direction) != False):
            CACHE1_VALID[search(CACHE1_DIR,direction)] = 0
        if(search(CACHE2_DIR,direction) != False):
            CACHE2_VALID[search(CACHE2_DIR,direction)] = 0
        if(search(CACHE4_DIR,direction) != False):
            CACHE4_VALID[search(CACHE4_DIR,direction)] = 0
        else:
            return 0
    if(procID == 4):
        if(search(CACHE1_DIR,direction) != False):
            CACHE1_VALID[search(CACHE1_DIR,direction)] = 0
        if(search(CACHE2_DIR,direction) != False):
            CACHE2_VALID[search(CACHE2_DIR,direction)] = 0
        if(search(CACHE3_DIR,direction) != False):
            CACHE3_VALID[search(CACHE3_DIR,direction)] = 0
        else:
            return 0

#Function that draws the instruction that is been executed    
def draw_processor_id(procID,direction,data):
    if (procID == 1):
        canvas.create_rectangle(5, 310, 170, 350, fill='#2C70A9') #1
        canvas.create_text(90, 330, text= "P1:" + str(bin(direction)) + "," + str(data), font = "Lucida")
    if (procID == 2):
        canvas.create_rectangle(280, 310, 425, 350, fill='#2C70A9') #2
        canvas.create_text(360, 330, text= "P2:" + str(bin(direction)) + "," + str(data), font = "Lucida")
    if (procID == 3):
        canvas.create_rectangle(520, 310, 670, 350, fill='#2C70A9') #3
        canvas.create_text(595, 330, text= "P3:" + str(bin(direction)) + "," + str(data), font = "Lucida")
    if (procID == 4):
        canvas.create_rectangle(780, 310, 920, 350, fill='#2C70A9') #4
        canvas.create_text(860, 330, text= "P4:" + str(bin(direction)) + "," + str(data), font = "Lucida")
    else:
        return 0

#Function that draws cache validation status  
def draw_cache_valid(ID,pos):
    if (ID == 1):
        if(pos == 0):
            canvas.create_rectangle(55, 110, 85, 140, fill='#BDBDBD')
            canvas.create_text(90, 120, text= str(CACHE1_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(55, 140, 85, 170, fill='#BDBDBD')
            canvas.create_text(65, 150, text= str(CACHE1_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(55, 170, 85, 200, fill='#BDBDBD')
            canvas.create_text(65, 180, text= str(CACHE1_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(55, 200, 85, 230, fill='#BDBDBD')
            canvas.create_text(65, 210, text= str(CACHE1_VALID[3]), font = "Lucida")
        else:
            return 0
    if (ID == 2):
        if(pos == 0):
            canvas.create_rectangle(305, 110, 335, 140, fill='#BDBDBD')
            canvas.create_text(315, 120, text= str(CACHE2_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(305, 140, 335, 170, fill='#BDBDBD')
            canvas.create_text(315, 150, text= str(CACHE2_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(305, 170, 335, 200, fill='#BDBDBD')
            canvas.create_text(315, 180, text= str(CACHE2_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(305, 200, 335, 230, fill='#BDBDBD')
            canvas.create_text(315, 210, text= str(CACHE2_VALID[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 3):
        if(pos == 0):
            canvas.create_rectangle(555, 110, 585, 140, fill='#BDBDBD')
            canvas.create_text(565, 120, text= str(CACHE3_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(555, 140, 585, 170, fill='#BDBDBD')
            canvas.create_text(565, 150, text= str(CACHE3_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(555, 170, 585, 200, fill='#BDBDBD')
            canvas.create_text(565, 180, text= str(CACHE3_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(555, 200, 585, 230, fill='#BDBDBD')
            canvas.create_text(565, 210, text= str(CACHE3_VALID[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 4):
        if(pos == 0):
            canvas.create_rectangle(805, 110, 835, 140, fill='#BDBDBD')
            canvas.create_text(815, 120, text= str(CACHE4_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(805, 140, 835, 170, fill='#BDBDBD')
            canvas.create_text(815, 150, text= str(CACHE4_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(805, 170, 835, 200, fill='#BDBDBD')
            canvas.create_text(815, 180, text= str(CACHE4_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(805, 200, 835, 230, fill='#BDBDBD')
            canvas.create_text(815, 210, text= str(CACHE4_VALID[3]), font = "Lucida")
        else:
            return 0

#Function that draws the memory status    
def draw_cache_mem(ID,pos):
    if (ID == 1):
        if(pos == 0):
            canvas.create_rectangle(85, 110, 180, 140, fill='#BDBDBD')
            canvas.create_text(90, 120, text= str(CACHE1_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(85, 140, 180, 170, fill='#BDBDBD')
            canvas.create_text(90, 150, text= str(CACHE1_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(85, 170, 180, 200, fill='#BDBDBD')
            canvas.create_text(90, 180, text= str(CACHE1_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(85, 200, 180, 230, fill='#BDBDBD')
            canvas.create_text(90, 210, text= str(CACHE1_VALID[3]), font = "Lucida")
        else:
            return 0

    if (ID == 2):
        if(pos == 0):
            canvas.create_rectangle(305, 110, 335, 140, fill='#BDBDBD')
            canvas.create_text(315, 120, text= str(CACHE2_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(305, 140, 335, 170, fill='#BDBDBD')
            canvas.create_text(315, 150, text= str(CACHE2_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(305, 170, 335, 200, fill='#BDBDBD')
            canvas.create_text(315, 180, text= str(CACHE2_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(305, 200, 335, 230, fill='#BDBDBD')
            canvas.create_text(315, 210, text= str(CACHE2_VALID[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 3):
        if(pos == 0):
            canvas.create_rectangle(555, 110, 585, 140, fill='#BDBDBD')
            canvas.create_text(565, 120, text= str(CACHE3_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(555, 140, 585, 170, fill='#BDBDBD')
            canvas.create_text(565, 150, text= str(CACHE3_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(555, 170, 585, 200, fill='#BDBDBD')
            canvas.create_text(565, 180, text= str(CACHE3_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(555, 200, 585, 230, fill='#BDBDBD')
            canvas.create_text(565, 210, text= str(CACHE3_VALID[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 4):
        if(pos == 0):
            canvas.create_rectangle(805, 110, 835, 140, fill='#BDBDBD')
            canvas.create_text(815, 120, text= str(CACHE4_VALID[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(805, 140, 835, 170, fill='#BDBDBD')
            canvas.create_text(815, 150, text= str(CACHE4_VALID[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(805, 170, 835, 200, fill='#BDBDBD')
            canvas.create_text(815, 180, text= str(CACHE4_VALID[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(805, 200, 835, 230, fill='#BDBDBD')
            canvas.create_text(815, 210, text= str(CACHE4_VALID[3]), font = "Lucida")
        else:
            return 0

#Function that draws data status    
def draw_cache_data(ID,pos):
    if (ID == 1):
        if(pos == 0):
            canvas.create_rectangle(180, 110, 275, 140, fill='#BDBDBD')
            canvas.create_text(230, 120, text= str(CACHE1[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(180, 140, 275, 170, fill='#BDBDBD')
            canvas.create_text(230, 150, text= str(CACHE1[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(180, 170, 275, 200, fill='#BDBDBD')
            canvas.create_text(230, 180, text= str(CACHE1[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(180, 200, 275, 230, fill='#BDBDBD')
            canvas.create_text(230, 210, text= str(CACHE1[3]), font = "Lucida")
        else:
            return 0

    if (ID == 2):
        if(pos == 0):
            canvas.create_rectangle(430, 110, 525, 140, fill='#BDBDBD')
            canvas.create_text(480, 120, text= str(CACHE2[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(430, 140, 525, 170, fill='#BDBDBD')
            canvas.create_text(480, 150, text= str(CACHE2[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(430, 170, 525, 200, fill='#BDBDBD')
            canvas.create_text(480, 180, text= str(CACHE2[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(430, 200, 525, 230, fill='#BDBDBD')
            canvas.create_text(480, 210, text= str(CACHE2[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 3):
        if(pos == 0):
            canvas.create_rectangle(680, 110, 775, 140, fill='#BDBDBD')
            canvas.create_text(730, 120, text= str(CACHE3[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(680, 140, 775, 170, fill='#BDBDBD')
            canvas.create_text(730, 150, text= str(CACHE3[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(680, 170, 775, 200, fill='#BDBDBD')
            canvas.create_text(730, 180, text= str(CACHE3[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(680, 200, 775, 230, fill='#BDBDBD')
            canvas.create_text(730, 210, text= str(CACHE3[3]), font = "Lucida")
        else:
            return 0
        
    elif (ID == 4):
        if(pos == 0):
            canvas.create_rectangle(930, 110, 1025, 140, fill='#BDBDBD')
            canvas.create_text(980, 120, text= str(CACHE4[0]), font = "Lucida")
        if(pos == 1):
            canvas.create_rectangle(930, 140, 1025, 170, fill='#BDBDBD')
            canvas.create_text(980, 150, text= str(CACHE4[1]), font = "Lucida")
        if(pos == 2):
            canvas.create_rectangle(930, 170, 1025, 200, fill='#BDBDBD')
            canvas.create_text(980, 180, text= str(CACHE4[2]), font = "Lucida")
        if(pos == 3):
            canvas.create_rectangle(930, 200, 1025, 230, fill='#BDBDBD')
            canvas.create_text(980, 210, text= str(CACHE4[3]), font = "Lucida")
        else:
            return 0
        
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

#Generates random hexa data
def data_generator():
    
    data = rand.randrange(65535)
    return hex(data)

#Function that draws data on screen an update it
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
