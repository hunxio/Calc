from tkinter import *
from tkinter import ttk

def main():
    # Initialize tkinter instance
    window = Tk() 
    # Creating a window object, defining the size and if it can be resized
    frame = ttk.Frame(window)
    window.geometry("600x600")
    window.resizable(False, False)
    window.title("Test Title Project")
    window.mainloop()

if __name__ == "__main__":
    main()