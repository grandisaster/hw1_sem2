from notebook import *

notebook = Notebook()


def searching():
    searching_option = input("Search for: ")
    notes = notebook.search(searching_option)
    notebook.show(notes)


def modification():
    note_id = int(input("Enter a note id: "))
    if note_id in range(1, notebook.last_id + 1):
        memo, tags = input("Enter a memo: "), input("Enter tags: ")
        notebook.modify(note_id, tags, memo)
    else:
        return(print('Id is not found'))


def addition():
    memo, tag = input("Enter a memo: "), input("Enter tag: ")
    notebook.create_note(memo, tag)
    print("Your note has been added.")


def quit_app():
    print("Thank you for using your Notebook today.")
    sys.exit(0)


choices = [(1, "Show all notes", notebook.show), (2, "Search notes", searching),
           (3, "Add note", addition), (4, "Modify note", modification), (5, "Quit", quit_app)]


def menu():
    print(DIVIDER, f"""\nNotebook Menu: \n1. Show all Notes \n2. Search Notes \n3. Add Note
4. Modify Note \n5. Quit""")


def app():
    while True:
        menu()
        choice = int((input("Enter an option: ")))
        if choice in range(1, 6):
            print(DIVIDER)
            action = choices[choice-1][2]()
        else:
            print(f"{choice} is not a valid choice")


if __name__ == '__main__':
    app()
