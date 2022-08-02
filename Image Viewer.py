from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("C:\\Users\\dubem\\OneDrive\\Pictures\\Scoopy.jpg")

Img1 = ImageTk.PhotoImage(Image.open("images/Scoopy.jpg"))
Img2 = ImageTk.PhotoImage(Image.open("images/Gear 5.png"))
Img3 = ImageTk.PhotoImage(Image.open("images/The Grand Canal.jpg"))

Img_list = [Img1, Img2, Img3]

my_label = Label(image=Img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(imageNumber):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image = Img_list[imageNumber-1])
    button_forward = Button(root, text=">>", command=lambda: forward(imageNumber+1))
    button_backward = Button(root, text="<<", command=lambda: backward(imageNumber-1))

    if imageNumber == 3:
        button_forward = Button(root, text=">>", state= DISABLED)

    
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def backward(imageNumber):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image = Img_list[imageNumber-1])
    button_forward = Button(root, text=">>", command=lambda: forward(imageNumber+1))
    button_backward = Button(root, text="<<", command=lambda: backward(imageNumber-1))
    
    if imageNumber == 1:
        button_backward = Button(root, text="<<", state= DISABLED)    

    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_backward = Button(root, text="<<", command=backward, state = DISABLED)
button_exit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)




root.mainloop()
