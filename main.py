import json
import os
from datetime import datetime

print(os.path.abspath('notes.json'))

notes_file = ("D:\\Geekbrains\\Промежуточная контрольная работа по блоку специализация\\Приложение заметки ("
              "Python)\\notes.json")


def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    else:
        return []


def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file, indent=4)


def list_notes(notes):
    if not notes:
        print("Заметок нет.")
    else:
        for idx, note in enumerate(notes):
            print(f"{idx + 1}. {note['title']} - {note['timestamp']}")


def view_note_details(note):
    print(f"Заголовок: {note['title']}")
    print(f"Дата/время создания: {note['timestamp']}")
    print("Тело заметки:")
    print(note['body'])


def add_note(notes):
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно.")


def edit_note(notes):
    list_notes(notes)
    idx = int(input("Введите номер заметки для редактирования: ")) - 1
    if 0 <= idx < len(notes):
        note = notes[idx]
        title = input("Введите новый заголовок (оставьте пустым для сохранения текущего): ")
        if title:
            note["title"] = title
        body = input("Введите новый текст (оставьте пустым для сохранения текущего): ")
        if body:
            note["body"] = body
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка успешно отредактирована.")
    else:
        print("Некорректный номер заметки.")


def delete_note(notes):
    list_notes(notes)
    idx = int(input("Введите номер заметки для удаления: ")) - 1
    if 0 <= idx < len(notes):
        del notes[idx]
        save_notes(notes)
        print("Заметка успешно удалена.")
    else:
        print("Некорректный номер заметки.")


def view_note(notes):
    list_notes(notes)
    idx = int(input("Введите номер заметки для просмотра: ")) - 1
    if 0 <= idx < len(notes):
        view_note_details(notes[idx])
    else:
        print("Некорректный номер заметки.")


def main():
    notes = load_notes()
    while True:
        print("\nМеню управления заметками:")
        print("1. Просмотреть список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Просмотреть заметку")
        print("6. Выход")
        choice = input("Введите номер выбранного действия: \n")

        if choice == "1":
            list_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            edit_note(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            view_note(notes)
        elif choice == "6":
            print("Выход...")
            break
        else:
            print("Некорректный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
