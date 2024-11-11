import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.setup_widgets()

        
    def setup_widgets(self):
        # Create a notebook (tabbed container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Tab 1: Video Editing
        self.tab_video = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_video, text="Video Editing")
        self.setup_video_editing_tab()

        # Tab 2: Audio Editing
        self.tab_audio = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_audio, text="Audio Editing")
        self.setup_audio_editing_tab()

        # Tab 3: Settings
        self.tab_settings = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_settings, text="Settings")
        self.setup_settings_tab()

    def setup_video_editing_tab(self):
        # Create a PanedWindow and place it with grid
        self.paned = ttk.PanedWindow(self.tab_video, orient="vertical")
        self.paned.grid(row=0, column=0, sticky="nsew", padx=20, pady=5)
        
        # Make the `tab_video` area expandable
        self.tab_video.rowconfigure(0, weight=1)
        self.tab_video.columnconfigure(0, weight=1)

        # Video Treeview
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)
        
        self.pane_1.grid(row=0, column=0, sticky="nsew")
        self.pane_1.rowconfigure(0, weight=1)
        self.pane_1.columnconfigure(0, weight=1)

        self.video_scrollbar = ttk.Scrollbar(self.pane_1, orient="vertical")
        self.video_scrollbar.grid(row=0, column=1, sticky="ns")

        self.video_treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.video_scrollbar.set,
            height=10,
        )
        self.video_treeview.grid(row=0, column=0, sticky="nsew")
        self.video_scrollbar.config(command=self.video_treeview.yview)

        self.video_treeview.column("#0", anchor="w", width=120)
        self.video_treeview.heading("#0", text="Item", anchor="center")

        # Separator
        self.separator = ttk.Separator(self.pane_1, orient="horizontal")
        self.separator.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

        # Audio Treeview
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=1)
        
        self.pane_2.grid(row=1, column=0, sticky="nsew")
        self.pane_2.rowconfigure(0, weight=1)
        self.pane_2.columnconfigure(0, weight=1)

        self.audio_scrollbar = ttk.Scrollbar(self.pane_2, orient="vertical")
        self.audio_scrollbar.grid(row=0, column=1, sticky="ns")

        self.audio_treeview = ttk.Treeview(
            self.pane_2,
            selectmode="browse",
            yscrollcommand=self.audio_scrollbar.set,
            height=10,
        )
        self.audio_treeview.grid(row=0, column=0, sticky="nsew")
        self.audio_scrollbar.config(command=self.audio_treeview.yview)

        self.audio_treeview.column("#0", anchor="w", width=120)
        self.audio_treeview.heading("#0", text="Item", anchor="center")

    def setup_audio_editing_tab(self):
        label_audio = tk.Label(self.tab_audio, text="Audio Editing Tools and Options")
        label_audio.pack(padx=20, pady=20)

    def setup_settings_tab(self):
        label_settings = tk.Label(self.tab_settings, text="Application Settings")
        label_settings.pack(padx=20, pady=20)