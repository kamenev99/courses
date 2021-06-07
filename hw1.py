from tkinter import *
root=Tk()
root.title("человек")
root.geometry("1000x1000")
canvas=Canvas(root, width="600",height="600")
canvas.pack()
canvas.create_oval(150,50,350,250,fill="yellow")
canvas.create_oval(180,120,200,140,fill="black")
canvas.create_oval(300,120,320,140,fill="black")
canvas.create_rectangle(200,250,300,450,fill="black")
canvas.create_line(230,450,200,550)
canvas.create_line(270,450,300,550)
canvas.create_line(200,270,170,370)
canvas.create_line(300,270,330,370)

              
