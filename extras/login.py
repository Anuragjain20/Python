from tkinter import *
from PIL import Image, ImageTk
from tkinter import Canvas
from tkinter import messagebox
with open("login.txt","r") as op:
    p = list(op.read().split("\n"))



root = Tk()
root.geometry("800x500+400+150")
root.iconbitmap("Awicons-Vista-Artistic-Folder-my-pictures.ico")
background = "light green"
root.configure(bg = background)
root.title("Login System")


titlelabel = Label(root,font = ("arial",30,"bold","italic"),text = "Login System",width = 30,bg = background,fg = "blue" )
titlelabel.place(x = 70 ,y = 10 )

load = Image.open("AvatarMaker.png")
img = ImageTk.PhotoImage(load)
imglabel  = Label(root,image = img,width = 100)
imglabel.place(x = 400,y = 100)

def onclick():
    name1 = nameEntry.get()
    pass1 = passwordEntry.get()
    var = name1+" "+pass1
    nameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    for i in p:
        if var == i:
            messagebox.showinfo("welcome","You are logged in")
            return
    else:
        messagebox.showwarning("warning","error")






namelabel = Label(root,text = "Name",bg = background,font = ("arial",20,"bold"),fg = "red")
namelabel.place(x = 200,y = 230)

nameEntry = Entry(root,font = ("arial",20,"bold"),width = 20)
nameEntry.place(x= 370,y = 230)

passwordlabel = Label(root,text = "Password",bg = background,font = ("arial",20,"bold"),fg = "red")
passwordlabel.place(x = 200,y = 290)

passwordEntry = Entry(root,font = ("arial",20,"bold"),width = 20)
passwordEntry.place(x= 370,y = 290)

btn = Button(root,text = "Login",bg = "Black",fg = "white",font = ("arial",15,"bold"),command = onclick)

btn.place(x = 420,y = 360)






root.mainloop()