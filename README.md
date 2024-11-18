It looks like you're trying to create a photo viewer in Python using Tkinter, but the code you've provided is more of a general-purpose GUI application with a variety of widgets like buttons, radio buttons, checkboxes, and sliders. 

To help you build a simple **photo viewer** using Tkinter, I'll modify your existing code to load and display images. The photo viewer will allow you to browse images, display them in a window, and add simple controls like next/previous buttons to navigate through them.

Here's how you can do it:



### Key Features:
1. **Load Images**: You can load multiple images by selecting them via a file dialog (`Load Images` button).
2. **Display Image**: The image is displayed inside a Tkinter `Canvas` widget. The image will be resized to fit the window size, and the user can view it.
3. **Navigation**: The user can navigate through the images using the "Previous" and "Next" buttons. The images will loop (wrap around).
4. **Pillow Library**: The code uses the `Pillow` library (`PIL`) for image handling. If you don't have it installed, you can install it via pip:
   ```
   pip install pillow
   ```

### How it Works:
1. The `load_images` function opens a file dialog allowing the user to select multiple images. The file paths are stored in the `image_list`.
2. The `display_image` function displays the current image from the `image_list` onto the canvas.
3. The "Previous" and "Next" buttons let the user navigate through the images in the list.

With this setup, you have a simple but functional photo viewer application using Tkinter and Pillow. Let me know if you'd like to add more features!
