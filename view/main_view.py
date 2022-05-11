from tkinter import ttk, PhotoImage
import tkinter as tk

import PIL
from PIL import Image, ImageTk

from controller.main_controller import MainController
from view.base_view import BaseView
from view.utils import gui_images


class MainView(BaseView):
    def __init__(self, m_screen, page_name, controller: MainController, resolution: tuple = (1280, 720), grid_rows=30,
                 grid_cols=30,
                 icon=None):
        super().__init__(m_screen, page_name, resolution, grid_rows, grid_cols, icon)
        self.controller = controller

        # Draw GUI
        self.canvas = tk.Canvas(self.parent, width=self.width, height=self.height)
        self.canvas.configure(bg="lightgray")
        self.canvas.grid(row=0, column=0, rowspan=self.rows, columnspan=self.cols)

        # Background
        self.canvas_bg = ImageTk.PhotoImage(gui_images.background("./resources/bg1.png", resolution))
        self.background = self.canvas.create_image(resolution[0] / 2, 0, anchor="n", image=self.canvas_bg)

        # Header
        # self.header = self.canvas.create_text(resolution[0] / 2, 90, text="Games Manager", fill="black",
        #                                       font=self.heading)

        # Add Game
        self.add_btn_img = ImageTk.PhotoImage(gui_images.button("./resources/add_btn.png", 120, 65))
        self.add_game = self.canvas.create_image(resolution[0] / 3, resolution[1] / 4, image=self.add_btn_img)
        self.canvas.tag_bind(self.add_game, "<ButtonRelease-1>", lambda event: self.controller.add_new_game())

        # Rem Game
        self.rem_btn_img = ImageTk.PhotoImage(gui_images.button("./resources/rem_btn.png", 120, 65))
        self.rem_game = self.canvas.create_image(resolution[0] - (resolution[0] / 3), resolution[1] / 4,
                                                 image=self.rem_btn_img)
        self.canvas.tag_bind(self.rem_game, "<ButtonRelease-1>", lambda event: self.controller.rem_game())

        # Games List
        self.game_list_var = tk.StringVar(value=self.controller.get_info_for_lb_var())
        self.game_list = tk.Listbox(self.parent, listvariable=self.game_list_var, selectmode="extended", bd=0,
                                    selectbackground="black", takefocus=0)
        self.game_list.configure(background="lightgray", font=self.text_bold)
        self.game_list.grid(row=9, column=5, columnspan=20, rowspan=10, sticky="nsew")

        # Run
        self.run_btn_img = ImageTk.PhotoImage(gui_images.button("./resources/run_btn.png", 250, 100))
        self.run_game = self.canvas.create_image(resolution[0] / 2,
                                                 resolution[1] - (resolution[1] / 3.5),
                                                 image=self.run_btn_img)
        self.canvas.tag_bind(self.run_game, "<ButtonRelease-1>", lambda event: self.controller.run_game())

    def refresh_games(self):
        self.game_list.delete(0, "end")
        self.game_list_var = []

        for game in self.controller.get_info_for_lb_var():
            self.game_list_var.append(game)
            self.game_list.insert("end", game)

        self.game_list_var = tk.StringVar(value=self.game_list_var)
