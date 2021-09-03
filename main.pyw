from tkinter import *
import os
from PIL import Image, ImageTk
from resizeimage import resizeimage


#====================================================================================================#

root = Tk()

root.geometry("600x550+500+100")
root.title("PC Manager | By AzKaR")
root.config = bg = "white"
root.resizable(0, 0)


img1 = PhotoImage(file="icon\puz.png")
img_contr = PhotoImage(file="icon\conn.png")

# ============TITTLE=============

title = Label(root, image=img1, text="   PC Maneger | By AzKaR", font=(
    "times new roman", 30, 'bold'), padx=10, bg="lightblue", compound=LEFT).place(x=0, y=0, relwidth=1)

# frame1


frame1 = Frame(root, width=200, bg="white")


# ======Label=======
control = Label(frame1, text="Control Pannel", font=(
    "arial", 12, "bold"), fg="black", bg="white")
control.place(x=50, y=120)

mouse = Label(frame1, text="Mouse", font=(
    "arial", 12, "bold"), fg="black", bg="white")
mouse.place(x=50, y=280)

filemanager = Label(frame1, text="My Pc", font=(
    "arial", 12, "bold"), fg="black", bg="white")
filemanager.place(x=50, y=450)


# =======

frame1_1 = Frame(frame1, width=90, height=90, bd=5)

image_control = ImageTk.PhotoImage(file="icon\conn.png")
btn_control = Button(frame1_1, image=image_control, width=90, height=90, bd=0,
                     activebackground="white", cursor="hand2", command=lambda: os.system('devmgmt.msc'))
btn_control.pack()


frame1_1.place(x=50, y=20)

frame1_2 = Frame(frame1, width=90, height=90, bd=5)

# image_mouse=ImageTk.PhotoImage(file="icon\Mouse1.png")
image_mause = Image.open("icon\Mouse1.png")
image_mause = image_mause.resize((90, 90), Image.ANTIALIAS)
image_mause = ImageTk.PhotoImage(image_mause)
btn_mouse = Button(frame1_2, image=image_mause, width=90, height=90, bd=0,
                   activebackground="white", cursor="hand2", command=lambda: os.system('main.cpl'))
btn_mouse.pack()

frame1_2.place(x=50, y=180)


frame1_3 = Frame(frame1, width=90, height=90, bd=5)

# image_mycomputer=ImageTk.PhotoImage(file="icon\MyComputer3.png")#this is not the crop image


image_mycomputer = Image.open("icon\MyComputer3.png")
resized = image_mycomputer.resize((90, 90), Image.ANTIALIAS)
image_mycomputer = ImageTk.PhotoImage(resized)

btn_computer = Button(frame1_3, image=image_mycomputer, width=90, height=90, bd=0,
                      activebackground="white", cursor="hand2", command=lambda: os.system('start..'))
btn_computer.pack()

frame1_3.place(x=50, y=340)


frame1.place(x=0, y=50, relheight=1)

# frame2


frame2 = Frame(root, width=200, bg="white")


# ======Label=======
camera = Label(frame2, text="Camera", font=(
    "arial", 12, "bold"), fg="black", bg="white")
camera.place(x=50, y=120)

search = Label(frame2, text="Taskbar", font=(
    "arial", 12, "bold"), fg="black", bg="white")
search.place(x=50, y=280)

security = Label(frame2, text="Services", font=(
    "arial", 12, "bold"), fg="black", bg="white")
security.place(x=50, y=450)

# ============

frame1_1 = Frame(frame2, width=90, height=90, bd=5)

# image_camra=ImageTk.PhotoImage(file="icon\Camera.png")

image_camra = Image.open("icon\Camera.png")
resized = image_camra.resize((90, 90), Image.ANTIALIAS)
image_camra = ImageTk.PhotoImage(resized)


btn_camra = Button(frame1_1, image=image_camra, width=90, height=90, bd=0, activebackground="white",
                   cursor="hand2", command=lambda: os.system('start microsoft.windows.camera:'))
btn_camra.pack()

frame1_1.place(x=50, y=20)

frame1_2 = Frame(frame2, width=90, height=90, bd=5)

# image_find=ImageTk.PhotoImage(file="icon\Find.png")

image_find = Image.open("icon\kbar.png")
resized = image_find.resize((90, 90), Image.ANTIALIAS)
image_find = ImageTk.PhotoImage(resized)

btn_find = Button(frame1_2, image=image_find, width=90, height=90, bd=0,
                  activebackground="white", cursor="hand2", command=lambda: os.system('taskmgr'))
btn_find.pack()

frame1_2.place(x=50, y=180)


frame1_3 = Frame(frame2, width=90, height=90, bd=5)

# image_security=ImageTk.PhotoImage(file="icon\Security1.png")

image_security = Image.open("icon\services.png")
resieed = image_security.resize((90, 90), Image.ANTIALIAS)
image_security = ImageTk.PhotoImage(resieed)


btn_security = Button(frame1_3, image=image_security, width=90, height=90, bd=0,
                      activebackground="white", cursor="hand2", command=lambda: os.system('services.msc'))
btn_security.pack()

frame1_3.place(x=50, y=340)


frame2.place(x=200, y=50, relheight=1)

# frame3
frame3 = Frame(root, width=200, bg="white")


power = Label(frame3, text="Shutdown", font=(
    "arial", 12, "bold"), fg="black", bg="white")
power.place(x=50, y=120)

network = Label(frame3, text="Network", font=(
    "arial", 12, "bold"), fg="black", bg="white")
network.place(x=50, y=280)

device = Label(frame3, text="Device", font=(
    "arial", 12, "bold"), fg="black", bg="white")
device.place(x=50, y=450)


frame1_1 = Frame(frame3, width=90, height=90, bd=5)

image_off = ImageTk.PhotoImage(file="icon\off.png")
btn_off = Button(frame1_1, image=image_off, width=90, height=90, bd=0,
                 activebackground="white", cursor="hand2", command=lambda: os.system('shutdown /s'))
btn_off.pack()

frame1_1.place(x=50, y=20)

frame1_2 = Frame(frame3, width=90, height=90, bd=5)

# image_network=ImageTk.PhotoImage(file=f"icon\\network.png")

image_network = Image.open("icon\\network.png")
resized = image_network.resize((90, 90), Image.ANTIALIAS)
image_network = ImageTk.PhotoImage(resized)
btn_network = Button(frame1_2, image=image_network, width=90, height=90, bd=0,
                     activebackground="white", cursor="hand2", command=lambda: os.system('ncpa.cpl'))
btn_network.pack()

frame1_2.place(x=50, y=180)


frame1_3 = Frame(frame3, width=90, height=90, bd=5)

image_mobobile = ImageTk.PhotoImage(file="icon\mobile-phone.png")
btn_phone = Button(frame1_3, image=image_mobobile, width=90, height=90, bd=0,
                   activebackground="white", cursor="hand2", command=lambda: os.system('msinfo32'))
btn_phone.pack()

frame1_3.place(x=50, y=340)


frame3.place(x=400, y=50, relheight=1)

prog = Label(root, text="It will show the error",
             bg="red", width=10).pack(fill=X, side=BOTTOM)


mainloop()
