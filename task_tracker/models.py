import uuid
from datetime import datetime

class Task:
    def __init__(self, description):
        now = datetime.now().isoformat()
        self.id = str(uuid.uuid4())
        self.description = description
        self.status = "todo"
        self.createdAt = now
        self.updatedAt = now

    def to_dict(self):
        return self.__dict__