from storage import storage

# --- КЛАССЫ ---
def create_class(name):
    if name in storage.data.classes:
        raise Exception(f"Class already exists: {name}")

    cid = storage.generate_id()
    storage.data.classes[name] = {"id": cid, "name": name}
    storage.save()
    return cid


# --- ЭЛЕМЕНТЫ ---
def create_element(class_name, name):
    if class_name not in storage.data.classes:
        raise Exception(f"Class not found: {class_name}")

    eid = storage.generate_id()
    storage.data.elements[eid] = {
        "id": eid,
        "name": name,
        "class": class_name
    }
    storage.save()
    return eid


# --- СВЯЗИ КЛАССОВ ---
def create_relation(name, from_class, to_class):
    if from_class not in storage.data.classes:
        raise Exception("from_class not found")

    if to_class not in storage.data.classes:
        raise Exception("to_class not found")

    rel = {
        "id": storage.generate_id(),
        "name": name,
        "from": from_class,
        "to": to_class
    }

    storage.data.relations.append(rel)
    storage.save()
    return rel["id"]


# --- СВЯЗИ ЭЛЕМЕНТОВ ---
def link_elements(e1, e2, rel_type):
    if e1 not in storage.data.elements:
        raise Exception("element 1 not found")

    if e2 not in storage.data.elements:
        raise Exception("element 2 not found")

    storage.data.links.append({
        "from": e1,
        "to": e2,
        "type": rel_type
    })
    storage.save()
    return "ok"


# --- ДИАГРАММА ---
def create_diagram(name):
    did = storage.generate_id()
    storage.data.diagrams[did] = {"id": did, "name": name}
    storage.save()
    return did


def place_element(diagram_id, element_id, x, y):
    if diagram_id not in storage.data.diagrams:
        raise Exception("diagram not found")

    if element_id not in storage.data.elements:
        raise Exception("element not found")

    storage.data.placements.append({
        "diagram": diagram_id,
        "element": element_id,
        "x": x,
        "y": y
    })
    storage.save()
    return "ok"


# --- DEBUG ---
def get_state():
    return storage.data.dict()


def reset():
    storage.data = type(storage.data)()
    storage.save()
    return "reset"