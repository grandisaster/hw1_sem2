import sys
from note import Note
import datetime
DIVIDER = 80*'='


class Notebook:
    def __init__(self):
        self.notes = {}
        self.last_id = 1

    def create_note(self, memo, tag):
        current_note = Note(memo, tag, self.last_id)
        self.notes[self.last_id] = current_note
        self.last_id += 1

    def modify(self, note_id, memo=None, tag=None):
        if memo:
            self.notes[note_id].memo = memo
        if tag:
            self.notes[note_id].tag = tag

    def search(self, search_filter):
        found_results = []
        for i in self.notes:
            result = self.notes[i]
            if search_filter in result.memo or search_filter in result.tag:
                found_results.append(result)

        return found_results

    def show(self, notes=None):
        if not notes:
            notes = self.notes
        for note in notes:
            if type(note) == int:
                note = notes[note]
            print(f"""Note id: {note.note_id} \nNote tags: {note.tag}
Note text: {note.memo}""")
