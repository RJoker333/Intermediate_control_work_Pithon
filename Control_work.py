import json
import datetime

class Note:
    def __init__(self, id, title, body, created=None, updated=None):
        self.id = id
        self.title = title
        self.body = body
        self.created = created if created else datetime.datetime.now()
        self.updated = updated if updated else datetime.datetime.now()

class NotesApp:
    def __init__(self):
        self.notes = []

    def load_notes(self, file):
        try:
            with open(file, "r") as f:
                data = json.load(f)
                self.notes = [Note(**item) for item in data]
        except FileNotFoundError:
            pass

    def save_notes(self, file):
        data = [note.__dict__ for note in self.notes]
        with open(file, "w") as f:
            json.dump(data, f, default=str)

    def add_note(self, title, body):
        id = len(self.notes) + 1
        note = Note(id, title, body)
        self.notes.append(note)

    def edit_note(self, id, title, body):
        note = self.get_note_by_id(id)
        if note:
            note.title = title
            note.body = body
            note.updated = datetime.datetime.now()

    def delete_note(self, id):
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)

    def print_notes(self):
        for note in self.notes:
            print(f"Id: {note.id}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Created: {note.created}")
            print(f"Updated: {note.updated}")
            print()

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None


if __name__ == "__main__":
    app = NotesApp()
    app.load_notes("notes.json")

    while True:
        print("1. Add note")
        print("2. Edit note")
        print("3. Delete note")
        print("4. View notes")
        print("5. Save and quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            app.add_note(title, body)
        elif choice == "2":
            id = int(input("Enter note id: "))
            title = input("Enter new note title: ")
            body = input("Enter new note body: ")
            app.edit_note(id, title, body)
        elif choice == "3":
            id = int(input("Enter note id: "))
            app.delete_note(id)
        elif choice == "4":
            app.print_notes()
        elif choice == "5":
            app.save_notes("notes.json")
            break
        else:
            print("Invalid choice. Please try again.")

    