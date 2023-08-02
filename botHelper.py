from collections import UserDict

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid input."
    return wrapper


class Name:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def update(self, value):
        self.value = value

class Phone:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def update(self, value):
        if not value.isdigit():
            raise ValueError
        if not (7 <= len(value) <= 15):
            raise ValueError
        self.value = value

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, index):
        if 0 <= index < len(self.phones):
            del self.phones[index]

    def edit_phone(self, index, new_number):
        if 0 <= index < len(self.phones):
            self.phones[index].update(new_number)

    def __str__(self):
        phone_str = ", ".join(str(phone) for phone in self.phones)
        return f"Name: {self.name}, Phones: {phone_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search(self, query):
        results = []
        for record in self.data.values():
            if query in record.name.value:
                results.append(record)
            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
                    break
        return results

contacts = AddressBook()

@input_error
def add_contact(name, phone):
    record = Record(Name(name))
    record.add_phone(phone)
    contacts.add_record(record)
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(name, phone):
    if name in contacts.data:
        record = contacts.data[name]
        record.edit_phone(0, phone)
        return f"Phone number for {name} updated to {phone}."
    else:
        raise KeyError

@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts.data[name].phones[0]}."

def show_all_contacts():
    if contacts.data:
        return "\n".join([str(record) for record in contacts.data.values()])
    else:
        return "No contacts found."
    
def main():
    while True:
        user_input = input("Enter a command: ").lower().split(" ", 2)
        command = user_input[0]

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                name = user_input[1]
                phone = user_input[2]
                response = add_contact(name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please.")
        elif command == "change":
            try:
                name = user_input[1]
                phone = user_input[2]
                response = change_contact(name, phone)
                print(response)
            except IndexError:
                print("Give me name and phone please.")
        elif command == "phone":
            try:
                name = user_input[1]
                response = get_phone(name)
                print(response)
            except IndexError:
                print("Enter user name.")
        elif command == "show":
            if user_input[1] == "all":
                print(show_all_contacts())
        elif command in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
