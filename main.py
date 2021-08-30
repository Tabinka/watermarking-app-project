import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter.filedialog import askopenfile

F_TYPES = [('Image Files', ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp'])]

window = tk.Tk()
window.title("Watermarking app")
window.config(padx=100, pady=100, bg="#DEEDF0")
pos_x = tk.IntVar()
pos_y = tk.IntVar()
width_logo = tk.IntVar()
height_logo = tk.IntVar()
text = tk.StringVar()
color = tk.StringVar()
opacity = tk.IntVar()

bg_image = Image.open("upload-image-icon.png")
bg_resized = bg_image.resize((300, 200))
bg_image_upload = ImageTk.PhotoImage(bg_resized)
upload_button = tk.Button(image=bg_image_upload, bg="#DEEDF0", bd=0, highlightthickness=0,
                          command=lambda: upload_file())
upload_button.grid(row=2, column=1)


def save_image():
    popup = tk.Tk()
    popup.wm_title("Do you wanna save an image?")
    b1 = tk.Button(popup, text="Okay", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def upload_file():
    global img, imgg
    filename = filedialog.askopenfilename(filetypes=F_TYPES)
    imgg = Image.open(filename)
    width, height = imgg.size
    width_new = int(width / 5)
    height_new = int(height / 5)
    img_resized = imgg.resize((width_new, height_new))
    img = ImageTk.PhotoImage(img_resized)
    display_image = tk.Button(image=img, bd=0, highlightthickness=0, bg="#DEEDF0")
    display_image.grid(row=3, column=1, columnspan=2, sticky=tk.W + tk.E)
    upload_button.destroy()
    image_options()


def image_options():
    add_text = tk.Button(text="Add text to image", width=40, bd=0, highlightthickness=0,
                         command=adding_text)
    add_text.grid(row=4, column=1)
    add_logo = tk.Button(text="Add your watermark logo", bd=0, highlightthickness=0, width=40,
                         command=adding_logo)
    add_logo.grid(row=4, column=2)


def adding_logo():
    pos_x_entry = tk.Entry(window, textvariable=pos_x)
    pos_y_entry = tk.Entry(window, textvariable=pos_y)
    width_entry = tk.Entry(window, textvariable=width_logo)
    height_entry = tk.Entry(window, textvariable=height_logo)
    opa = tk.Entry(window, textvariable=opacity)
    sub_btn = tk.Button(window, text='Submit', command=submit)
    pos_x_entry.grid(row=1, column=1)
    pos_y_entry.grid(row=1, column=2)
    width_entry.grid(row=1, column=3)
    height_entry.grid(row=1, column=4)
    opa.grid(row=1, column=5)
    sub_btn.grid(row=1, column=6)


def submit():
    x = pos_x.get()
    y = pos_y.get()
    width = width_logo.get()
    height = height_logo.get()
    opct = opacity.get()
    filename_logo = filedialog.askopenfilename(filetypes=F_TYPES)
    logo_file = Image.open(filename_logo)
    logo_file.putalpha(opct)
    logo = logo_file.resize((width, height))
    imgg.paste(logo, (x, y), logo)
    save_show()


def adding_text():
    pos_x_entry = tk.Entry(window, textvariable=pos_x)
    pos_y_entry = tk.Entry(window, textvariable=pos_y)
    input_text = tk.Entry(window, textvariable=text)
    color_text = tk.Entry(window, textvariable=color)
    sub_btn = tk.Button(window, text='Submit', command=submit_add_text)
    input_text.grid(row=1, column=1)
    pos_x_entry.grid(row=1, column=2)
    pos_y_entry.grid(row=1, column=3)
    color_text.grid(row=1, column=4)
    sub_btn.grid(row=1, column=5)


def submit_add_text():
    x = pos_x.get()
    y = pos_y.get()
    color_text = color.get()
    input_text = text.get()
    draw = ImageDraw.Draw(imgg)
    font = ImageFont.truetype("ArialNarrow.ttf", size=50)
    draw.text((x, y), input_text, fill=color_text, font=font)
    save_show()


def save_show():
    save_btn = tk.Button(window, text="Save image", command=lambda: imgg.save("xoxo.jpg"))
    save_btn.grid(row=2, column=1)
    show_btn = tk.Button(window, text="Show image", command=lambda: imgg.show())
    show_btn.grid(row=2, column=2)


tk.mainloop()
