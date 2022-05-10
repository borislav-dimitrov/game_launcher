from model.dao.json_repo import JsonOperations
from model.entities.game import Game


class GenericRepository(JsonOperations):
    def __init__(self):
        super().__init__()
        self._entities = {}
        self._id = 0

    # region GET
    def get_all(self):
        return list(self._entities)

    def get_by_attrib(self, attr_name: str, attr_val: any, exact_val=True):
        result = []

        try:
            for entity in self._entities:
                found = getattr(self._entities[entity], attr_name, "<attr not found>")
                if found == "<attr not found>":
                    raise AttributeError(f"Entity doesn't have attribute '{attr_name}'!")

                if exact_val:
                    if attr_val == found:
                        result.append(self._entities[entity])
                else:
                    if isinstance(attr_val, str):
                        if attr_val.lower() in found.lower():
                            result.append(self._entities[entity])
                    elif attr_val in found:
                        result.append(self._entities[entity])

            if len(result) > 0:
                return result
            else:
                return None
        except Exception as ex:
            return ex

    def get_by_id(self, id_: int):
        try:
            return self._entities[id_]
        except Exception as ex:
            return ex

    # endregion

    # region CRUD
    def create(self, entity):
        if not isinstance(entity, Game):
            raise TypeError(f"{entity} is not a valid Game Object!")

        # assign id
        if entity.id_ is None:
            self._id += 1
            entity.id_ = self._id

        self._entities[entity.id_] = entity
        return self._entities[entity.id_]

    def del_by_id(self, id_: int):
        old = self._entities[id_]
        del self._entities[id_]
        return old

    # endregion

    # region OTHER
    def count(self):
        return len(self._entities)
    # endregion
