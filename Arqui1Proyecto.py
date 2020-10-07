import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3


def clicked(event):
    
    print("pressed")
    
top = tkinter.Tk(className = "-Multiprocessor Simulation-")

top.geometry("1100x700")

top.configure(bg = '#2C70A9')



#PROCESSORS

canvas = tkinter.Canvas(top, width=1200, height=700, bg = '#2C70A9')

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



#LINES

canvas.create_line(180, 300, 180, 400)

canvas.create_line(430, 300, 430, 400)

canvas.create_line(680, 300, 680, 400)

canvas.create_line(930, 300, 930, 400)

canvas.create_line(570, 450, 570, 550)

button = canvas.create_text(150, 600, text="START SIMULATION", font = "Arial")

canvas.tag_bind(button, "<Button-1>", clicked)

canvas.pack()


# Code to add widgets will go here...

top.mainloop()
