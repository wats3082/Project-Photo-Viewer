from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  # Make sure you have Pillow installed (pip install pillow)

class PhotoViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer")
        self.root.geometry("800x600")  # Adjust the window size
        self.image_list = []  # List to hold the image paths
        self.current_image_index = 0  # Index of the current image

        # Frame for displaying image
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

        # Canvas to display the image
        self.canvas = Canvas(self.frame)
        self.canvas.pack(fill=BOTH, expand=True)

        # Buttons for navigation
        self.prev_button = Button(self.root, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=LEFT, padx=10, pady=10)

        self.next_button = Button(self.root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=RIGHT, padx=10, pady=10)

        # Button to load images from file dialog
        self.load_button = Button(self.root, text="Load Images", command=self.load_images)
        self.load_button.pack(side=BOTTOM, pady=10)

    def load_images(self):
        """Allow user to select multiple images and add them to the image list."""
        file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_paths:
            self.image_list = file_paths
            self.current_image_index = 0  # Reset to first image
            self.display_image()

    def display_image(self):
        """Display the current image in the canvas."""
        if self.image_list:
            image_path = self.image_list[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.ANTIALIAS)  # Resize image to fit the window
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=photo, anchor=NW)
            self.canvas.image = photo  # Keep a reference to the image

    def show_previous_image(self):
        """Show the previous image in the list."""
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)  # Wrap around to last image
            self.display_image()

    def show_next_image(self):
        """Show the next image in the list."""
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)  # Wrap around to first image
            self.display_image()

# Create the Tkinter window
root = Tk()

# Create the PhotoViewer object
photo_viewer = PhotoViewer(root)

# Start the Tkinter main loop
root.mainloop()












"""


from tkinter import *
from tkinter import IntVar, messagebox

root = Tk()
root.title("This is a frame.")
root.geometry("400x700")
# root.iconbitmap('input pathway here for different window icon')

frame = LabelFrame(root, padx=10, pady=20)
frame.pack(padx=20, pady=20)

button = Button(frame, text="Dont click here.")
# dont put this in root, add it to frame instead
button.grid(row=0, column=0)
button2 = Button(frame, text="Or here....")
# you can also use grid and pack together when working with frames
button2.grid(row=1, column=0)


# radio buttons or the round buttons next to menu


def Click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# using a kinter variable here, not python
r: IntVar = IntVar()  # lets kinter update changes throught the entire program
r.set("1")

# create a Python tuple list for wanted radio options
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),  # first thing is option shows on screen, 2nd is the value it passes
    ("Mushroom", "Mushroom"),
    ("Olive", "Olive"),
]
pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)  # loop to create alot of buttons easier

# radio1 = Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda : Click(r.get()))  # when they click this one, it is option 1
# radio1.pack()
# radio2 = Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda : Click(r.get()))  # when they click this one, it is option 2
# radio2.pack()
# myLabel = Label(root, text= r.get())
# myLabel.pack()
myButton = Button(root, text="Add to Cart...", command=lambda: Click(pizza.get()))
myButton.pack()


# MESSAGE BOX
# can use showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def Popup():
    response = messagebox.askyesno("This is my popbox", "Hello World")
    print(response)
    if response == 1:
        Label(root, text="You clicked Yes").pack()
    else:
        Label(root, text="You clicked No").pack()


Button(root, text="popup", command=Popup).pack()

# SLIDERS
# notice how you have to use an underscore for the from, also how it is called Scale not slider
slider1 = Scale(root, from_=0, to=100)
slider1.pack()
slider2 = Scale(root, from_=0, to=10, orient=HORIZONTAL)
slider2.pack()

# CHECKBOXES

def Show():
    label4 = Label(root, text=var.get()).pack()


var = StringVar()
checkbox1 = Checkbutton(root, text="check here to add fries and a drink +$4",variable=var, onvalue="On", offvalue="Off")
checkbox1.deselect()
checkbox1.pack()
myButton4 = Button(root, text="Show Selection", command=Show).pack()



# DROP DOWN BOX

clicked = StringVar()
clicked.set("Monday")
dropdown1 = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
dropdown1.pack()
print(clicked.get())



root.mainloop()
"""
