import json
import os
from models import StorageModel
import uuid

DB_FILE = "db.json"

class Storage:
    def __init__(self):
        self.data = StorageModel()
        self.load()

    def load(self):
      if os.path.exists(DB_FILE):
          with open(DB_FILE, "r", encoding="utf-8") as f:
              content = f.read().strip()
              if not content:
                  self.data = StorageModel()
              else:
                  self.data = StorageModel(**json.loads(content))

    def save(self):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data.dict(), f, ensure_ascii=False, indent=2)

    def generate_id(self):
        return str(uuid.uuid4())

storage = Storage()
