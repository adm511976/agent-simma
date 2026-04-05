import random

class Executor:
    def __init__(self, api):
        self.api = api
        self.class_ids = {}
        self.element_ids = {}

    def ensure_classes(self):
        for c in ["Система", "Компонент", "Внешняя система"]:
            self.class_ids[c] = self.api.create_class(c)

    def run(self, dsl):
        self.ensure_classes()

        # элементы
        for el in dsl["elements"]:
            eid = self.api.create_element(
                self.class_ids[el["class"]],
                el["name"]
            )
            self.element_ids[el["name"]] = eid

        # связи
        for link in dsl["links"]:
            self.api.link_elements(
                self.element_ids.get(link["from"]),
                self.element_ids.get(link["to"]),
                link["type"]
            )

        # схема
        diagram = self.api.create_diagram(
            model_id="1",  # <-- подставишь
            name=dsl["diagram"]["name"]
        )

        # размещение (просто сетка)
        x, y = 100, 100
        for el_name, eid in self.element_ids.items():
            self.api.place_element(diagram, eid, x, y)
            x += 200
            if x > 1000:
                x = 100
                y += 200