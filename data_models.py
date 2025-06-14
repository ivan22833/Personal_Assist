class DataStorage:
    def __init__(self):
        self.contacts = {}
        self.notes = []

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def add_note(self, note):
        self.notes.append(note)
