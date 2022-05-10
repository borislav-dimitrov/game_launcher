from tkinter import ttk
import tkinter as tk

from controller.main_controller import MainController
from view.base_view import BaseView


class MainView(BaseView):
    def __init__(self, m_screen, page_name, controller: MainController, resolution: tuple = (1280, 720), grid_rows=30,
                 grid_cols=30,
                 icon=None):
        super().__init__(m_screen, page_name, resolution, grid_rows, grid_cols, icon)
        self.controller = controller

        # Draw GUI
        self.header_lbl = ttk.Label(self.parent, text="Hello", font=self.text_bold, anchor="center")
        self.header_lbl.grid(row=2, column=0, columnspan=self.cols, sticky="we")

        # Add Game
        self.add_game = ttk.Button(self.parent, text="ADD", command=lambda: self.controller.add_new_game())
        self.add_game.grid(row=6, column=3, columnspan=7, rowspan=2, sticky="nsew")

        # Rem Game
        self.rem_game = ttk.Button(self.parent, text="REM", command=lambda: self.controller.rem_game())
        self.rem_game.grid(row=6, column=19, columnspan=7, rowspan=2, sticky="nsew")

        # Games List
        self.game_list_var = tk.StringVar(value=self.controller.get_info_for_lb_var())
        self.game_list = tk.Listbox(self.parent, listvariable=self.game_list_var, selectmode="extended")
        self.game_list.grid(row=9, column=3, columnspan=23, rowspan=10, sticky="nsew")

        # Run
        self.run_game = ttk.Button(self.parent, text="RUN", command=lambda: self.controller.run_game())
        self.run_game.grid(row=20, column=7, columnspan=15, rowspan=2, sticky="nsew")

    def refresh_games(self):
        self.game_list.delete(0, "end")
        self.game_list_var = []

        for game in self.controller.get_info_for_lb_var():
            self.game_list_var.append(game)
            self.game_list.insert("end", game)

        self.game_list_var = tk.StringVar(value=self.game_list_var)
