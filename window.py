from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)                
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Project")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)
        info = Menu(menu)
        info.add_command(label='Info', command=self.message)
        menu.add_cascade(label='Info', menu=info)
        click = Menu(menu)
        click.add_command(label='Click Here', command=self.button_clicked)
        menu.add_cascade(label='Click Here', menu=click)

    def showImg(self):
        load = Image.open("dog.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showText(self):
        text = Label(self, text="So cute!")
        text.pack()

    def message(self):
        messagebox.showinfo( "Hey curious", "This is just a test :)")
    
    def button_clicked(self):
        text = Label(self, text="Well done")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop() 