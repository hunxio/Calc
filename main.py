from tkinter import *
from tkinter import ttk

def main():
    # Initialize tkinter instance
    window = Tk() 
    # Creating a window object, defining multiple properties
    frame = ttk.Frame(window)
    window.geometry("600x600")
    window.configure(background="black")
    window.resizable(False, False)
    # Window Title
    window.title("Test Title Project")
    window.mainloop()

if __name__ == "__main__":
    main()