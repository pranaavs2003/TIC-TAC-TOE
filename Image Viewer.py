from tkinter import *
from PIL import ImageTk,Image

currentImage = 0
root = Tk()
root.title('Image Viewer')
root.iconbitmap('icons/Sbstnblnd-Plateau-Apps-image-viewer.ico')


#Importing Images
pic1 = ImageTk.PhotoImage(Image.open('images\pic1.jpg'))
pic2 = ImageTk.PhotoImage(Image.open('images\pic2.jpg'))
pic3 = ImageTk.PhotoImage(Image.open('images\pic3.jpg'))
pic4 = ImageTk.PhotoImage(Image.open('images\pic4.jpg'))
pic5 = ImageTk.PhotoImage(Image.open('images\pic5.jpg'))


#Displaying First image
mylable = Label(image=pic1)
mylable.grid(row=0, column=0, columnspan=3)
image_list=[pic1,pic2,pic3,pic4,pic5]


#Status Bar
txt=f'Image {currentImage+1} of {len(image_list)}'
status_bar = Label(root, text=txt, bd=1, relief=SUNKEN, anchor=E, padx=9)
status_bar.grid(row=2, column= 0, columnspan=3, sticky=E+W)


#Button Functions
def nextImage(image_number):
    global currentImage
    global mylable
    global image_list
    currentImage+=1

    if currentImage < len(image_list):
        mylable.grid_forget()
        mylable = Label(image=image_list[currentImage])
        mylable.grid(row=0, column=0, columnspan=3)
    else:
        currentImage = 0
        mylable.grid_forget()
        mylable = Label(image=image_list[currentImage])
        mylable.grid(row=0, column=0, columnspan=3)

    # Status Bar
    txt = f'Image {currentImage + 1} of {len(image_list)}'
    status_bar = Label(root, text=txt, bd=1, relief=SUNKEN, anchor=E, padx=9)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=E + W)


def prevImage(image_number):
    global currentImage
    global mylable
    global image_list
    currentImage-=1

    if currentImage > -1:
        mylable.grid_forget()
        mylable = Label(image=image_list[currentImage])
        mylable.grid(row=0, column=0, columnspan=3)
    else:
        currentImage = len(image_list)-1
        mylable.grid_forget()
        mylable = Label(image=image_list[currentImage])
        mylable.grid(row=0, column=0, columnspan=3)

    # Status Bar
    txt = f'Image {currentImage + 1} of {len(image_list)}'
    status_bar = Label(root, text=txt, bd=1, relief=SUNKEN, anchor=E, padx=9)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=E + W)

#Buttons
Button_exit = Button(root, text='Exit', command=root.quit)
Button_exit.grid(row=1,column=1)
Button_next = Button(root, text='>>', command=lambda: nextImage(currentImage))
Button_next.grid(row=1 ,column=2)
Button_prev = Button(root, text='<<', command=lambda: prevImage(currentImage))
Button_prev.grid(row=1 ,column=0)



root.mainloop()

