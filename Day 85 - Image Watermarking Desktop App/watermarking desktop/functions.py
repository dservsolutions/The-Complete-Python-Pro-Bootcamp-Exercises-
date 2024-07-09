from tkinter import NW, filedialog, Image, Canvas, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import main

# IMG Size Vars
new_height = 800
new_width = 600
original_img = None


def load_image():
    global original_img
    filetypes = [("Image Files", "*.jpg *.jpeg")]
    file_path = filedialog.askopenfilename(filetypes=filetypes)

    if file_path:
        # Loading the Original IMG
        original_img = Image.open(file_path)

        # Resizing the Original IMG
        resized_img = original_img.resize((new_height, new_width))

        # Loading the resized IMG to the PhotoImage Object
        photo = ImageTk.PhotoImage(resized_img)

        # Creating the Canvas Object
        canvas = Canvas(width=500, height=500)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.image = photo
        # canvas.grid(column=1, row=4)
        canvas.pack()
        main.label_info.pack()
        main.label_info.config(text=f"Format: {original_img.format}")
    else:
        print("Please select a valid photo")


def add_watermark():
    global original_img
    text = main.text_box.get()
    warning = "Please write some text for add a Watermark!!!"
    filetype = [("Filetypes", "*.jpeg *.jpg")]
    output_path = filedialog.asksaveasfile(filetypes=filetype)
    if text == "":
        messagebox.showinfo("Error", warning)
    else:
        img_to_draw = original_img
        draw = ImageDraw.Draw(img_to_draw)

        # Define Font
        font = ImageFont.load_default()

        # Get image size
        width, height = img_to_draw.size

        # Get text size
        bbox = draw.textbbox((500, 500), text=text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        print(f"Text width: {text_width}, text height: {text_height}")

        # Draw a Text
        draw.text((text_width, text_height), text, (255, 255, 255), font=font)
        img_to_draw.save(output_path)
        messagebox.showinfo("Success", f"{text} added successfully.")
