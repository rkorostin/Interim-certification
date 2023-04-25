import datetime

class Note:
    def __init__(self, title, content):
        self.id = None
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, dict):
        note = cls(dict["title"], dict["content"])
        note.id = int(dict["id"])
        note.created_at = datetime.datetime.fromisoformat(dict["created_at"])
        return note