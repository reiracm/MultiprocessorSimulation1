import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = tkinter.Tk(className = "-Multiprocessor Simulation-")
top.geometry("1100x700")
top.configure(bg = '#2C70A9')

#PROCESSORS
canvas = tkinter.Canvas(top, width=1200, height=700, bg = '#2C70A9')
canvas.create_rectangle(80, 70, 280, 300, fill='#7D8287')
canvas.create_rectangle(330, 70, 530, 300, fill='#7D8287')
canvas.create_rectangle(580, 70, 780, 300, fill='#7D8287')
canvas.create_rectangle(830, 70, 1030, 300, fill='#7D8287')

#BUS
canvas.create_rectangle(80, 400, 1030, 450, fill='#7D8287')

#MEMORY
canvas.create_rectangle(470, 550, 670, 620, fill='#7D8287')

#LINES
canvas.create_line(180, 300, 180, 400)
canvas.create_line(430, 300, 430, 400)
canvas.create_line(180, 300, 180, 400)
canvas.create_line(180, 300, 180, 400)
canvas.pack()
# Code to add widgets will go here...
top.mainloop()
