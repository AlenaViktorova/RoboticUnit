def draw_key(canvas, key, x, y, width, height, key_color="white", border_color="black", text_color="black"):
    # Create a rectangle representing the key
    key_id = canvas.create_rectangle(x, y, x + width, y + height, fill=key_color, outline=border_color, tags=key)
    # Place the key label in the center of the rectangle
    canvas.create_text(x + width / 2, y + height / 2, text=key, fill=text_color, font=("Helvetica", 12, "bold"))


def change_key_background_color(canvas, key, color):
    # Change the background color of the specified key
    canvas.itemconfig(key, fill=color)