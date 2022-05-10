from model.dao.generic_repo import GenericRepository
from os.path import exists

from model.entities.game import Game
from tkinter import messagebox


class GameService:
    def __init__(self, repo: GenericRepository):
        self._repo = repo

    # region GET
    def find_all(self):
        return self._repo.get_all()

    def get_by_id(self, id_: int):
        result = self._repo.get_by_id(id_)
        if isinstance(result, Exception):
            messagebox.showerror("Error!", result)
        else:
            return result

    def get_by_attribute(self, attr_name: str, attr_val: any, exact_val=True):
        result = self._repo.get_by_attrib(attr_name, attr_val, exact_val)
        if isinstance(result, Exception):
            messagebox.showerror("Error!", result)
        else:
            return result

    # endregion

    # region CRUD
    def create(self, name: str, path: str, id_: int = None) -> Game | Exception:
        try:
            if len(name) < 4:
                raise Exception(f"Failed creating Game Object! Name should be at least 3 characters long!")
            if len(path) < 4:
                raise Exception(f"Failed creating Game Object! Invalid game path!")
            if not exists(path):
                raise Exception(f"Failed creating Game Object! Game path not found!")

            game = Game(name, path, id_)
            return self._repo.create(game)
        except Exception as ex:
            return ex

    def del_by_id(self, id_: int) -> Game | Exception:
        try:
            return self._repo.del_by_id(id_)
        except Exception as ex:
            return ex

    # endregion

    # region Save\Load\Reload
    def save(self):
        self._repo.save("./model/data/data.json")

    def load(self):
        try:
            loaded = self._repo.load("./model/data/data.json")
            if loaded is not None:
                for item in loaded:
                    id_, name, path = loaded[item].values()
                    new = Game(name, path, id_)
                    self._repo.create(new)

        except Exception as ex:
            return ex

    def reload(self):
        self.save()
        self.load()

    # endregion

    # region OTHER
    def calc_id(self):
        id_ = 0
        for item in self._repo._entities:
            if item > id_:
                id_ = item
        self._repo._id = id_

    # endregion

    # region VIEW FUNCS
    def get_info_for_lb_var(self):
        result = []

        for game in self._repo._entities:
            result.append(f"{self._repo._entities[game].id_} | {self._repo._entities[game].name}")

        return result

    # endregion
