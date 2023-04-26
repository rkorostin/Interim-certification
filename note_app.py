from note import Note
import csv

class NotesApp:
    def __init__(self):
        self.notes = []

    def read_notes(self):
        for note in self.notes:
            print(f"{note.id}: {note.title}\n{note.content}\nДата создания: {note.created_at}\n")

    def add_note(self, title, content):
        note = Note(title, content)
        note.id = len(self.notes) + 1
        self.notes.append(note)
        print("Заметка успешно добавлена")

    def save_notes(self):
        with open("notes.csv", "w", newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["id", "title", "content", "created_at"])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.content, note.created_at.isoformat()])
        print("Заметки успешно сохранены")

    def load_notes(self):
        try:
            with open("notes.csv", "r") as f:
                reader = csv.DictReader(f, delimiter=';')
                self.notes = [Note.from_dict(row) for row in reader]
            print("Заметки успешно загружены")
        except FileNotFoundError:
            print("Сохраненных заметок не найдено")

    def edit_note(self, id, title, content):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.content = content
                print("Примечание успешно отредактировано")
                return
        print("Заметок не найдено")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                print("Примечание успешно удалено")
                return
        print("Заметка не найдена")