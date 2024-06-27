from tkinter import *
from tkinter import ttk


class Window:
    # Initialize tkinter instance
    def __init__(self, window, widget):
        self._window = window
        self._widget = widget
        self._frame = ttk.Frame(self._window)

    # Creating a window object, defining multiple properties
    def configure_window(self):
        self._window.geometry("600x600")
        self._window.configure(background="black")
        self._window.resizable(False, False)
        self._window.title("Test Title Project")

    # Creating widgets to display and interact with inside the window's app
    def create_widgets(self):
        self._widget.Button(
            self._window, text="Exit App", command=self._window.destroy
        ).grid(column=0, row=0)

    @property
    def frame(self):
        return self._frame


def main():
    wind = Window(Tk(), ttk)
    wind.configure_window()
    wind.create_widgets()
    wind._window.mainloop()


if __name__ == "__main__":
    main()
