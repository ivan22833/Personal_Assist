from interfaces import ConsoleInterface
from data_models import DataStorage

def main():
    storage = DataStorage()
    ui = ConsoleInterface()

    commands = {
        "add contact": "Додати контакт",
        "add note": "Додати нотатку",
        "show contacts": "Показати всі контакти",
        "show notes": "Показати всі нотатки",
        "help": "Показати список команд",
        "exit": "Вийти з програми"
    }

    print("Вітаю! Це ваш персональний помічник.")

    while True:
        command = input("\nВведіть команду: ").strip().lower()

        if command == "add contact":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            storage.add_contact(name, phone)
            print("Контакт додано.")

        elif command == "add note":
            note = input("Нотатка: ")
            storage.add_note(note)
            print("Нотатку додано.")

        elif command == "show contacts":
            ui.display_contacts(storage.contacts)

        elif command == "show notes":
            ui.display_notes(storage.notes)

        elif command == "help":
            ui.display_help(commands)

        elif command == "exit":
            print("До побачення!")
            break

        else:
            print("Невідома команда. Введіть 'help', щоб побачити список команд.")

if __name__ == "__main__":
    main()
