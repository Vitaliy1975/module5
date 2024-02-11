def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name. Input correct name, please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        return "Contact is already in contacts. Not added."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args,contacts):
    name,phone=args
    if name not in contacts.keys():
        return "Not found."
    contacts[name]=phone
    return "Contact updated."

@input_error
def show_phone(args,contacts):
    name=args[0]
    if name not in contacts.keys():
        return "Not found"
    return contacts.get(name)

@input_error
def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command=="change":
            print(change_contact(args,contacts))
        elif command=="phone":
            print(show_phone(args,contacts))
        elif command=="all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
