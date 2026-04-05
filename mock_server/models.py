from pydantic import BaseModel
from typing import Dict, List

class StorageModel(BaseModel):
    classes: Dict[str, dict] = {}
    elements: Dict[str, dict] = {}
    relations: List[dict] = []
    links: List[dict] = []
    diagrams: Dict[str, dict] = {}
    placements: List[dict] = []