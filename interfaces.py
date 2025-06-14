from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_help(self, commands):
        pass


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        print("\nКонтакти:")
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")

    def display_notes(self, notes):
        print("\nНотатки:")
        for i, note in enumerate(notes, 1):
            print(f"  {i}. {note}")

    def display_help(self, commands):
        print("\nДоступні команди:")
        for cmd, desc in commands.items():
            print(f"  {cmd} — {desc}")
