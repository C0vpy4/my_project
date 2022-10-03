from tkinter import *
from commands import Commands
import tksvg

class Window():


    

    window = Tk()
    window.title("хай")
    window.geometry("600x450")
    # BACKGROUND
    #back_image = tksvg.SvgImage(master=window, file="c.svg", scale=1)
    label = Label(bg="#2592d1",  borderwidth=100000)
    label.pack()

    # BUTTONS 
    button_timetables = Button(window,text="Расписание", background="green", fg="blue", width=19, height=10, command=Commands.timetables_show)
    button_timetables.place(relx=0.1,rely=0.1)

    button_changes = Button(window, text="Изменения в расписание",background="green", fg="blue", width=19, height=10, command=Commands.changes)
    button_changes.place(relx=0.4, rely=0.1)

    button_help = Button(window, text="Help", background="red", fg="yellow", width=10, height=2, command=Commands.help)
    button_help.place(relx=0.45, rely=0.88)

    window.mainloop()




if __name__ == "__main__":
    Window()    