from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Welcome to Python Programming!")

#add Button widget

btn = Button(window, text="Click to add name!", fg="blue")
btn.place(x=80,y=100)

#Add Label widget

lbl = Label(window, text="Student Personal Information", fg="blue", bg="orange")
lbl.place(relx=.5,y=50,anchor="center")
lbl2 = Label(window,text = "Gender",fg="blue")
lbl2.place(x=80,y=150)
lbl3 = Label(window, text= "Favorite Sports",fg="blue")
lbl3.place(x=80,y=210)
lbl4 = Label(window,text="Subjects",fg="blue")
lbl4.place(x=80,y=270)

#Add text field widget

txtfld = Entry(window,bd = 3, font=("Verdana",16))
txtfld.place(x=200,y=100)

#Add radio button

v1 = StringVar()
v2 = StringVar()
v1.set(1)
r1 = Radiobutton(window, text ="Male",value=v1)
r1.place(x=80,y=180)

r2 = Radiobutton(window,text = "Female", value=v2)
r2.place(x=200,y=180)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox = Checkbutton(window,text="basketball",variable=v3)
chkbox2 = Checkbutton(window,text="volleyball",variable=v4)
chkbox3 = Checkbutton(window,text="tennis",variable=v5)
chkbox.place(x=80,y=240)
chkbox2.place(x=180,y=240)
chkbox3.place(x=280,y=240)

var = StringVar()
var.set("Arithmetic")
data1 = "Arithmetic"
data2 = "Reading"
data3 = "Writing"
lstbox = Listbox(window,height=5,selectmode="multiple")
lstbox.insert(END,data1,data2,data3)
lstbox.place(x=80,y=300)


window.mainloop()

