import tkinter as tk
from tkinter import colorchooser, filedialog

class DigitalWhiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        self.root.geometry("1000x600")

        # Canvas setup
        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Initial settings
        self.pen_color = "black"
        self.pen_width = 2
        self.eraser_on = False

        # Buttons for controls
        self.control_frame = tk.Frame(self.root, bg="lightgrey", height=40)
        self.control_frame.pack(fill=tk.X)

        self.color_button = tk.Button(self.control_frame, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.eraser_button = tk.Button(self.control_frame, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.control_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.control_frame, text="Save", command=self.save_canvas)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.pen_size_label = tk.Label(self.control_frame, text="Pen Size:")
        self.pen_size_label.pack(side=tk.LEFT, padx=5)

        self.pen_size_slider = tk.Scale(self.control_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_pen_size)
        self.pen_size_slider.set(self.pen_width)
        self.pen_size_slider.pack(side=tk.LEFT, padx=5)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.last_x = None
        self.last_y = None

    def choose_color(self):
        color = colorchooser.askcolor(color=self.pen_color)[1]
        if color:
            self.pen_color = color
            self.eraser_on = False

    def toggle_eraser(self):
        self.eraser_on = not self.eraser_on
        if self.eraser_on:
            self.pen_color = "white"
        else:
            self.pen_color = "black"

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.save_to_file(file_path)

    def save_to_file(self, file_path):
        try:
            from PIL import Image, ImageDraw
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image = Image.new("RGB", (canvas_width, canvas_height), "white")
            draw = ImageDraw.Draw(image)

            for item in self.canvas.find_all():
                coords = self.canvas.coords(item)
                if len(coords) == 4:  # Line
                    x1, y1, x2, y2 = coords
                    fill = self.canvas.itemcget(item, "fill")
                    width = self.canvas.itemcget(item, "width")
                    draw.line((x1, y1, x2, y2), fill=fill, width=int(width))

            image.save(file_path)
            print(f"Canvas saved as {file_path}")
        except ImportError:
            print("Pillow library is required to save the canvas. Install it using 'pip install pillow'.")

    def change_pen_size(self, event):
        self.pen_width = int(self.pen_size_slider.get())

    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=self.pen_width, capstyle=tk.ROUND, smooth=True)
            self.last_x = x
            self.last_y = y

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalWhiteboard(root)
    root.mainloop()
