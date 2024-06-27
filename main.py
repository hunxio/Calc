from tkinter import *
from tkinter import ttk


class Window:
    # Initialize tkinter instance
    def __init__(self, root, widget):
        self._root = root
        self._widget = widget
        self._frame = ttk.Frame(self._root)

    # Creating a window object, defining multiple properties
    def configure_window(self):
        self._root.geometry("600x600")
        self._root.configure(background="white")
        self._root.resizable(False, False)
        self._root.title("Test Title Project")

    # Creating widgets to display and interact with inside the window's app
    def create_widgets(self):
        input_bar = self._widget.Entry(self._root, width=20).grid(column=0, row=0)
        enter_btn = self._widget.Button(self._root, text="Enter").grid(column=1, row=0)
        quit_btn = self._widget.Button(
            self._root, text="Exit App", command=self._root.destroy
        ).grid(column=0, row=1)


def main():
    root = Window(Tk(), ttk)
    root.configure_window()  # Loads window
    root.create_widgets()  # Loads widgets
    root._root.mainloop()  # Mantains the window always open


if __name__ == "__main__":
    main()
