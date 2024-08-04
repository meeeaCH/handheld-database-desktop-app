import tkinter as tk                
from tkinter import messagebox


class Platfrom_Window(tk.Frame):
    def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="""Platfrom Window Temp
You will be able to add New Platfroms to the database""",font=('Arial', 18)) # , font=styles.title_Font
            label.pack(side="top", fill="x", pady=10)
            button = tk.Button(self, text="Go Back",
                            command=lambda: controller.show_frame("Menu_Window"))
            button.pack(anchor = "s", side="left", padx=20, pady=12)

            # Making the HELP button
            help = tk.Button(self, text="Help", font=('Arial', 10), command=self.help_Btn_Func) 
            help.pack(anchor = "s", side="right", padx=20, pady=12)
            
        # Defining the HELP button's function
    def help_Btn_Func(self):
        main_menu = """HERE GOES THE HELP FOR THIS SECTION.
"""
        messagebox.showinfo("Platfrom Info", main_menu) 