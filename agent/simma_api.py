import requests

class SimmaAPI:
    def __init__(self, base_url: str, sid: str):
        self.base_url = base_url
        self.sid = sid

    def _call(self, action: str, params: dict):
        payload = {
            "action": action,
            "sid": self.sid,
            **params
        }

        response = requests.post(self.base_url, data=payload)
        response.raise_for_status()

        try:
            return response.json()
        except:
            return response.text

    # --- МЕТАМОДЕЛЬ ---
    def create_class(self, name):
        return self._call("cc", {"name": name})

    def create_relation(self, name, from_class, to_class):
        return self._call("cr", {
            "name": name,
            "from": from_class,
            "to": to_class
        })

    # --- МОДЕЛЬ ---
    def create_element(self, class_id, name):
        return self._call("ce", {
            "class": class_id,
            "name": name
        })

    def link_elements(self, e1, e2, rel):
        return self._call("cl", {
            "from": e1,
            "to": e2,
            "type": rel
        })

    # --- СХЕМА ---
    def create_diagram(self, model_id, name):
        return self._call("cd", {
            "model": model_id,
            "name": name
        })

    def place_element(self, diagram_id, element_id, x, y):
        return self._call("cdq", {
            "diagram": diagram_id,
            "element": element_id,
            "x": x,
            "y": y
        })