class Game:
    def __init__(self, name, path, id_):
        self.name = name
        self.path = path
        self.id_ = id_

    def to_json(self):
        return {
            "id": self.id_,
            "name": self.name,
            "path": self.path
        }
