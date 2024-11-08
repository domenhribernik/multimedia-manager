
import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        self.setup_menu()
        self.setup_widgets()

    def setup_menu(self):
        menu_bar = tk.Menu(self)

        # Menu 1
        menu_1 = tk.Menu(menu_bar, tearoff=0)
        menu_1.add_command(label="Switch to Tab 1", command=lambda: self.switch_tab(0))  # Switch to Tab 1
        menu_bar.add_cascade(label="Menu 1", menu=menu_1)

        # Menu 2
        menu_2 = tk.Menu(menu_bar, tearoff=0)
        menu_2.add_command(label="Switch to Tab 2", command=lambda: self.switch_tab(1))  # Switch to Tab 2
        menu_bar.add_cascade(label="Menu 2", menu=menu_2)

        self.master.config(menu=menu_bar)

    def setup_widgets(self):
        # Create a notebook (tabbed container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1
        self.tab_1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_1, text="Tab 1")

        # Tab 2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Tab 2")

        # Tab 3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Tab 3")

        # Add some content to the tabs
        label_1 = tk.Label(self.tab_1, text="Content for Tab 1")
        label_1.pack(padx=20, pady=20)

        label_2 = tk.Label(self.tab_2, text="Content for Tab 2")
        label_2.pack(padx=20, pady=20)

        label_3 = tk.Label(self.tab_3, text="Content for Tab 3")
        label_3.pack(padx=20, pady=20)

    def switch_tab(self, index):
        """Switch to the tab specified by the index."""
        self.notebook.select(index)