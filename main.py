from notes import add_note, show_notes

print("=" * 40)
print("📝 Clipboard Notes")
print("=" * 40)

while True:
    print("\n1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        note = input("Enter note: ").strip()

        if note:
            add_note(note)
            print("✅ Note saved.")
        else:
            print("❌ Note cannot be empty.")

    elif choice == "2":
        show_notes()

    elif choice == "3":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
