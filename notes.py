FILE = "notes.txt"


def add_note(note):
    with open(FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def show_notes():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            print("\n📭 No notes yet.")
            return

        print("\n📋 Your Notes")
        print("-" * 30)

        for number, note in enumerate(notes, 1):
            print(f"{number}. {note.strip()}")

    except FileNotFoundError:
        print("\n📭 No notes yet.")
