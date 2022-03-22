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


def p():
    number = int(input('Введите номер документа: '))
    name = ""
    for dictionary in documents:
        if dictionary["number"] == str(number):
            name = dictionary["name"]
    if name != "":
        print(name)
    else:
        print("Документ не найден в базе")


def s():
    number = input("Введите номер документа: ")
    keys = ""
    for key in directories:
        if str(number) in directories.get(key):
            keys = key
    if keys != "":
        print(keys)
    else:
        print("Документ не найден в базе")


def l():
    for dictionary in documents:
        number = dictionary["number"]
        type = dictionary["type"]
        name = dictionary["name"]
        shelves = ""
        for key in directories:
            if number in directories.get(key):
                shelves = key
                break
        print("№: ", number, ", ", "Тип: ", type, ", ", "Владелец: ", name, ", ", "Полка хранения: ", shelves)


def ads():
    number = int(input('Введите номер полки: '))
    shelves = ""
    for key in directories:
        shelves += " " + key
    for key in directories:
        if key == str(number):
            print("Такая полка уже существует. Текущий перечень полок: ", shelves)
            return
    directories.update({str(number): None})
    print("Полка добавлена. Текущий перечень полок:", shelves, number)


def ds():
    number = int(input('Введите номер полки: '))
    for key in directories:
        if key == str(number):
            if directories.get(key) == []:
                shelves1 = ""
                for key2 in directories:
                    if key2 != str(number):
                        shelves1 += " " + key2
                print("Полка удалена. Текущий перечень полок: ", shelves1)
                return

            else:
                shelves2 = ""
                for key2 in directories:
                    shelves2 += " " + key2
                print("На полке есть документы, "
                      "удалите их перед удалением полки."
                      " Текущий перечень полок: ", shelves2)
                return
    shelves3 = ""
    for key2 in directories:
        shelves3 += " " + key2
    print("Такой полки не существует. Текущий перечень полок: ", shelves3)


def ad():
    number = input("Введите номер документа: ")
    type = input("Введите тип документа: ")
    name = input("Введите имя владельца документа: ")
    shelves = input("Введите номер полки для хранения: ")
    contains = False
    for key in directories:
        if key == str(shelves):
            directories.get(key).append(str(number))
            documents.append({"number": str(number), "type": str(type), "name": str(name)})
            contains = True
            break
    if contains:
        print("Документ добавлен. Текущий список документов: ")

    else:
        print("Такой полки не существует. Добавьте полку командой as.")
        print("Текущий список документов: ")
    l()


def d():
    number = input("Введите номер документа: ")
    contains = False
    for dictionary in documents:
        if dictionary["number"] == str(number):
            contains = True
            documents.remove(dictionary)
            break
    if contains:
        print("Документ удален. Текущий список документов: ")
    else:
        print("Документ не найден в базе. Текущий список документов: ")
    l()


def m():
    number = input("Введите номер документа: ")
    new = input("Введите номер полки для хранения: ")
    old = ""
    contains = False
    exists = False
    for shelf in directories:
        if number in directories.get(shelf):
            exists = True
            old = shelf
            break
    if exists:
        for key in directories:
            if key == str(new):
                directories.get(key).append(str(number))
                directories.get(old).remove(str(number))
                contains = True
                break
        if contains:
            print("Документ добавлен. Текущий список документов: ")
        else:
            print("Такой полки не существует. Добавьте полку командой as.")
            print("Текущий список документов: ")
    else:
        print("Документ не найден в базе. Текущий список документов :")
    l()


while True:
    command = input("Введите команду: ")
    if command == 'p':
        p()
    elif command == 's':
        s()
    elif command == 'l':
        l()
    elif command == 'ads':
        ads()
    elif command == 'ds':
        ds()
    elif command == 'ad':
        ad()
    elif command == 'd':
        d()
    elif command == 'm':
        m()
    elif command == 'q':
        break
