def find_owner_by_number(documents):
    number = input("Введите номер документа: ")
    for document in documents:
        if document['number'] == number:
            return f"Владелец документа: {document['name']}"
    return "Документ не найден"


def find_shelf_by_number(directories):
    number = input("Введите номер документа: ")
    for shelf, documents in directories.items():
        if number in documents:
            return f"Документ хранится на полке: {shelf}"
    return "Документ не найден на полках"


def main():
    documents = [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
    ]

    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    while True:
        command = input("Введите команду (p - узнать владельца документа, s - узнать полку документа, q - выход): ")

        if command == "p":
            print(find_owner_by_number(documents))
        elif command == "s":
            print(find_shelf_by_number(directories))
        elif command == "q":
            break
        else:
            print("Некорректная команда")


if __name__ == "__main__":
    main()