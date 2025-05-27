import tkinter as tk
from gui import SecretSantaGUI

#Starting point of execution which in turn calls the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SecretSantaGUI(root)
    root.mainloop()
