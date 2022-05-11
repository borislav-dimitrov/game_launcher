import os

from model.dao.generic_repo import GenericRepository
from model.services.game_service import GameService
from tkinter import filedialog as fd
from tkinter import messagebox


class MainController:
    def __init__(self, service: GameService = None, view=None):
        self.view = view
        self.service = service

    def startup(self):
        repo = GenericRepository()
        self.service = GameService(repo)
        self.service.load()
        # set the entities id counter
        self.service.calc_id()

    def custom_exit(self):
        self.service.save()

    def get_info_for_lb_var(self):
        return self.service.get_info_for_lb_var()

    def add_new_game(self):
        filetypes = (('Applications', '*.exe'),)

        path = fd.askopenfilename(
            title="Select game to add",
            initialdir="/",
            filetypes=filetypes)

        if path:
            name = path.split("/")[-1]
            self.service.create(name, path)
            self.view.refresh_games()

    def rem_game(self):
        lb_selection = self.view.game_list.curselection()
        if len(lb_selection) < 1:
            messagebox.showerror("Error!", "Make a selection first!")
            return

        answer = messagebox.askyesno("Are you sure?", "Are you sure you want to delete this game/s from the list?")
        if not answer:
            return

        for item in lb_selection:
            lb_selection_id = self.view.game_list.get(item).split("|")[0].strip()
            self.service.del_by_id(int(lb_selection_id))

        self.view.refresh_games()

    def run_game(self):
        lb_selection = self.view.game_list.curselection()
        if len(lb_selection) == 0:
            messagebox.showerror("Error!", "Make a selection first!")
            return
        if len(lb_selection) > 1:
            messagebox.showerror("Error!", "Make select one game at a time!")
            return

        lb_selection_id = self.view.game_list.get(lb_selection).split("|")[0].strip()
        game = self.service.get_by_id(int(lb_selection_id))
        if ".exe" in game.path:
            os.startfile(game.path)
            quit(0)
        else:
            messagebox.showerror("Error!", "Not a valid game path!")
