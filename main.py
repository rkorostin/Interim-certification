from note import Note
from note_app import NotesApp
import datetime

app = NotesApp()

while True:
    command = input("Введите команду (read, add, save, load, edit, delete, search, exit): ")

    if command == "read":
        app.read_notes()

    elif command == "add":
        title = input("Введите название заметки: ")
        content = input("Введите содержимое заметки: ")
        app.add_note(title, content)

    elif command == "save":
        app.save_notes()

    elif command == "load":
        app.load_notes()

    elif command == "edit":
        id = int(input("Введите id заметки: "))
        title = input("Введите название новой заметки: ")
        content = input("Введите новое содержимое заметки: ")
        app.edit_note(id, title, content)

    elif command == "delete":
        id = int(input("Введите id заметки: "))
        app.delete_note(id)
    
    elif command == "search":
        start_date = datetime.datetime.strptime(input("Введите начальную дату (в формате ГГГГ-ММ-ДД): "), "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(input("Введите конечную дату (в формате ГГГГ-ММ-ДД): "), "%Y-%m-%d").date()
        app.search_notes(start_date, end_date)

    elif command == "exit":
        break

    else:
        print("Недопустимая команда")