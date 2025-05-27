import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from loader import ParticipantLoader
from pair_generator import SecretSantaEngine

#This Class has methods to do the following :
#  * create GUI Widgets/Components
#  * call loader for loading current year employees and previous year employees 
#  * call pair_generator for generating the pairs with constraints
#  * create UI components that display the generated pairs

class SecretSantaGUI:

    #Initialisation
    def __init__(self, root):
        self.root = root
        self.root.title("Secret Santa Generator")
        self.main_frame = tk.Frame(self.root, bg="#ADD8E6")
        self.main_frame.pack(fill="both", expand=True)

        self.participants = []
        self.engine = None
        self.last_year_data = {}
        self.last_year_pairs = None

        self.create_widgets()

    #Creation of the UI Components
    def create_widgets(self):
        style = ttk.Style()

        style.theme_use("default")  

        style.configure("TButton",
                font=("Segoe UI", 10),
                padding=6,
                background="#00008B",
                foreground="white")

        style.configure("TLabel",
                font=("Segoe UI", 11),
                foreground="#333")
    
        style.configure("Header.TLabel",
                font=("Segoe UI", 16, "bold"),
                foreground="#2E8B57")

        self.img = tk.PhotoImage(file="Label_img.png")
        ttk.Label(self.main_frame, text="Secret Santa Generator", style="Header.TLabel", image=self.img, compound="left").pack(pady=10)
        

        ttk.Button(self.main_frame, text="Load Participants", command=self.load_csv).pack(pady=5)
        ttk.Button(self.main_frame, text="Load Last Year's Pairs", command=self.load_last_year).pack(pady=5)
        
        self.generate_button = ttk.Button(self.main_frame, text="Generate Pairs",command=self.generate_pairs, state=tk.DISABLED)
        self.generate_button.pack(pady=5)
        self.save_button = ttk.Button(self.main_frame, text="Save Pairs",command=self.save_csv,  state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.tree = ttk.Treeview(self.main_frame, columns=("giver", "receiver"), show="headings")
        self.tree.configure(style="Disbaled.Treeview")
        
    #Loading the input csv file 
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.participants = ParticipantLoader.load_from_csv(file_path)
            self.engine = SecretSantaEngine(self.participants)
            self.display_message(f"Loaded {len(self.participants)} participants.")
            self.generate_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_last_year(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.last_year_pairs,self.last_year_data = ParticipantLoader.load_previous_pairs(file_path)
            self.display_message("Last year's pairs loaded.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
    #Generating the employee and secret santa pairs
    def generate_pairs(self):
        try:
            self.engine = SecretSantaEngine(self.participants, self.last_year_pairs, self.last_year_data)
            pairs = self.engine.generate_pairs()
            self.display_pairs(pairs)
            self.save_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #Displaying the generated pairs
    def display_pairs(self, pairs):
        
        self.tree.heading("giver", text="Giver")
        self.tree.heading("receiver", text="Receiver")
        self.tree.pack(pady=10)
        self.tree.configure(style="Treeview")

        for giver, receiver in pairs:
            self.tree.insert("", "end", values=(giver, receiver))
        
        self.tree.configure(style="Disbaled.Treeview")

        
    #Displaying message to user
    def display_message(self, message):
        messagebox.showinfo("Info",message)

    #Saving generated pairs to file
    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.engine.save_pairs_to_csv(file_path)
            messagebox.showinfo("Success", f"Pairs saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
