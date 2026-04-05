def to_dsl(data: dict) -> dict:
    elements = []
    links = []

    # система
    elements.append({
        "name": data["system"],
        "class": "Система"
    })

    # компоненты
    for c in data.get("components", []):
        elements.append({"name": c, "class": "Компонент"})

    # внешние системы
    for ext in data.get("external_systems", []):
        elements.append({"name": ext, "class": "Внешняя система"})

    # связи
    for rel in data.get("interactions", []):
        links.append({
            "from": rel["from"],
            "to": rel["to"],
            "type": rel["type"]
        })

    return {
        "elements": [...],
        "links": [...],
        "diagram": {
            "name": data["system"]
        }
    }