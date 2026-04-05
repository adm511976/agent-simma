from fastapi import APIRouter, Request
from services import *

router = APIRouter()

@router.post("/")
async def handle(request: Request):
    form = await request.form()
    action = form.get("action")

    try:
        if action == "cc":
            return {"id": create_class(form.get("name"))}

        elif action == "ce":
            return {"id": create_element(
                form.get("class"),
                form.get("name")
            )}

        elif action == "cr":
            return {"id": create_relation(
                form.get("name"),
                form.get("from"),
                form.get("to")
            )}

        elif action == "cl":
            return link_elements(
                form.get("from"),
                form.get("to"),
                form.get("type")
            )

        elif action == "cd":
            return {"id": create_diagram(form.get("name"))}

        elif action == "cdq":
            return place_element(
                form.get("diagram"),
                form.get("element"),
                int(form.get("x")),
                int(form.get("y"))
            )

        else:
            return {"error": "unknown action"}

    except Exception as e:
        return {"error": str(e)}