# ImageViewer
from tkinter import *
from PIL import Image, ImageTk
#the big idea is to define the widget, create the widget , then you have to add widget to screen

root = Tk()
root.title("Learn to use Images")
root.title(geography = "600x600")

myImg3 = ImageTk.PhotoImage(Image.open("istockphoto-1255835530-170667a.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("istockphoto-1268675353-170667a.jpg"))
myImg1 = ImageTk.PhotoImage(Image.open("photo.jpg"))

image_list = [myImg1, myImg2, myImg3]
click_count = 0
image_number = 1

myLabel = Label(image=myImg1)
myLabel.grid(row=0, column=0, columnspan=3)  # we make it span 3 because we want 3 buttons underneath

# status bar to show which image is on the screen
status_bar = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E) #stick it to the east or right side of window
# len will give you the length of a file and must cast it as a string



def ForwardFunction(image_number):
    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()  # we use this to delete current image before dispaying second image
    myLabel = Label(image=image_list[
        image_number - 1])  # use to access next image in array above, minus one because the index starts at 0
    buttonForward = Button(root, text=">>>>>", command=lambda: ForwardFunction(image_number + 1))
    buttonBack = Button(root, text="<<<<<<", command=lambda: BackFunction(image_number - 1))

    if image_number == 3:
        buttonForward = Button(root, text=">>>>>", state=DISABLED)  # use this to disable list at the end of images

    myLabel.grid(row=0, column=0, columnspan=3)  # use this to put the new image on screen
    buttonBack.grid(row=3, column=0)
    buttonForward.grid(row=3, column=2)
    status_bar = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                       anchor=E)  # stick it to the east or right side of window
    status_bar.grid(row=4, column=0, columnspan=3, sticky=W + E)


def BackFunction(image_number):
    global myLabel
    global buttonForward
    global buttonBack

    myLabel.grid_forget()  # we use this to delete current image before dispaying second image
    myLabel = Label(image=image_list[
        image_number - 1])  # you have to minus one because the index starts at 0
    buttonForward = Button(root, text=">>>>>", command=lambda: ForwardFunction(image_number + 1))
    buttonBack = Button(root, text="<<<<<<", command=lambda: BackFunction(image_number - 1))

    if image_number == 1:
        buttonBack = Button(root, text="<<<<<<", state=DISABLED)  # use this to disable list at the end of images

    myLabel.grid(row=0, column=0, columnspan=3)  # use this to put the new image on screen
    buttonBack.grid(row=3, column=0)
    buttonForward.grid(row=3, column=2)
    status_bar = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                       anchor=E)  # stick it to the east or right side of window
    status_bar.grid(row=4, column=0, columnspan=3, sticky=W + E)

if click_count != 0:
    buttonBack = Button(root, text="<<<<", command=lambda: BackFunction(2))
else:
    buttonBack = Button(root, text="<<<<", state=DISABLED)
buttonExit = Button(root, text="Exit", command=root.quit)
buttonForward = Button(root, text=">>>>", command=lambda: ForwardFunction(2))
# you pass 2 because the first time you click the forward button you want the second image in the list

buttonBack.grid(row=3, column=0)
buttonExit.grid(row=3, column=1)
buttonForward.grid(row=3, column=2, pady=10)
status_bar.grid(row=4, column=0, columnspan=3, sticky=W+E)
# use sticky coordinates to tell it to stretch in any direction, in this case west to east or the whole bottom


root.mainloop()
