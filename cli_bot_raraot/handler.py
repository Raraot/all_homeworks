from ast import main
from error_handler import error_handler
from file_sorter import sorter
from phonebook import *
from notes import *


@error_handler
def add_birthday(*args) -> None:  # Username birthday
    """
    Is used to add contact birthday
    :param args: Username birthday
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_birthday(
        Birthday(birthday)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_email(*args) -> None:
    """
    Is used to change contact phone
    :param args: Username phone
    :return: None
    """
    name, email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_email(
        Email(email)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_phone(*args) -> None:
    """
    Is used to change contact phone
    :param args: Username phone
    :return: None
    """
    name, phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_phone(
        Phone(phone)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_note(*args) -> None:
    """
    Add new note to notebook

    :param args: None
    :return: None
    """
    name = input("Enter note name: ")
    tags = input("Enter tags for note: ")
    text = input("Enter note text: ")
    print(NBCmd.add_note(name, tags, text, NB))


@error_handler
def birthdays_in(*args) -> None:
    """
    Show birthday persons in given days

    :param args: days
    :return: None
    """
    days = int(args[0]) if args else None
    birthdays = AB.show_near_birthdays(days) if days else AB.show_near_birthdays()
    print(*birthdays, sep='\n')


@error_handler
def delete_birthday(*args) -> None:
    """
    Is used to delete contact birthday

    :param args: contact name
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_birthday()
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_contact(*args):
    """
    Is used to contact from phonebook

    :param args: contact name
    :return: None
    """
    name = args[0]
    result = AB.delete_contact(name)
    print(result)


@error_handler
def delete_email(*args):
    """
    Is used to delete contact email

    :param args: Username email
    :return: None
    """
    name, email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_email(
        email
    )
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_phone(*args):
    """
    Is used to delete contact phone

    :param args: Username phone
    :return: None
    """
    name, phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_phone(
        phone
    )
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_note(*args):
    """
    Is used to delete note from notebook

    :param args: None
    :return: None
    """
    name = input("Enter the name of the note you want to delete: ")
    confirm = input("Do you really want to delete y/n: ")
    if confirm.lower() == "y":
        print(NBCmd.delete_note(name, NB))


@error_handler
def edit_birthday(*args) -> None:
    """
    Changing birthday

    :param args: username new birthday date
    :return: None
    """
    name, new_birthday, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_birthday(
        Birthday(new_birthday)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_email(*args) -> None:
    """
    Is used to change contact email

    :param args: Username old_email, new_email
    :return: None
    """
    name, old_email, new_email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_email(
        old_email, Email(new_email)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_phone(*args):
    """
    Is used to change contact phone

    :param args: Username old_phone new_phone
    :return: None
    """
    name, old_phone, new_phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_phone(
        old_phone, Phone(new_phone)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_note(*args):
    """
    Is used to edit note in notebook

    :param args: None
    :return: None
    """
    name = input("Enter the name of the note you want to edit: ")

    if name not in NB.data:
        raise KeyError(f'Note with name {name} does not find')
    else:

        print(f"Old  text note: {NBCmd.get_note(name, NB)}")
        new_note = input("Edit text note: ")
        print(NBCmd.edit_note(name, new_note, NB))
   

@error_handler
def edit_tag(*args):
    """
    Is used to edit tag in notebook

    :param args: None
    :return: None
    """
    name = input("Enter the name of the note where you want to edit tags: ")

    if name not in NB.data:
        raise KeyError(f'Note with name {name} does not find')
    else:

        print(f"Old  tags: {', '.join(NBCmd.get_tags(name, NB))}")
        new_tags = input("Edit tags: ")
        print(NBCmd.edit_tags(name, new_tags, NB))        


@error_handler
def new_contact(*args) -> None:
    """
    Adding new contact to your phonebook

    :param args: query
    :return: None
    """
    name = Name(args[0])
    record = Record(name)
    for arg in args[1:]:

        if arg.isdigit():
            record.add_phone(Phone(arg))

        elif '@' in arg:
            record.add_email(Email(arg))

        else:
            record.add_birthday(Birthday(arg))

    AB.add_contact(record)


@error_handler
def change_phonebook(*args) -> None:
    """
    Changing phonebook

    :param args: book name
    :return: None
    """
    book_name = args[0]
    AB.change_book(book_name)


@error_handler
def change_notebook(*args) -> None:
    """
    Changing notebook

    :param args: book name
    :return: None
    """
    book_name = args[0]
    NB.change_book(book_name)


@error_handler
def find_note(*args):
    request = input("Enter a query to search: ")
    print(SNBCmd.find_note(request, NB))


@error_handler
def find_phonebook(*args) -> None:
    """
    Performing search in all contacts data in current phonebook

    :param args: search query
    :return: None

    """
    information = [AB.find_record(arg) for arg in args]
    for answer in information:

        for username, fields in answer.items():

            if len(fields) == 1 and username == fields[0]:  # username is a key
                print(f"Looks like you are looking for {username} contact")
            else:
                print(f"Looks like you are looking for {username} data:")
                for field in fields:
                    print(field[0], end=': ')
                    print(*field[1:], sep=', ')


@error_handler
def find_tag(*args):
    """
    Performing search in current notebook

    :param args: None
    :return: None

    """
    print(SNBCmd.find_tag("available", NB))
    tag = input("Enter a tag: ")
    print(SNBCmd.find_tag(tag, NB)) 


@error_handler
def show_contact(*args) -> None:
    # """
    # Is used to show one exact contact data

    # :param args: contact name
    # :return: None
    # """
    # name = args[0]
    # contact_info = AB.show_record_data(name)

    # for field in contact_info:
    #     print(*field)
    name = args[0]
    ssc = ShowSomeContact()
    ssc.print_data(AB, name)

@error_handler
def show_contacts(*args) -> None:
    # """
    # Show all phonebook records separated on pages

    # :param args: records per page
    # :return:
    # """
    # records_per_page = int(args[0]) if args else None

    # pages = AB.show_contacts(records_per_page) if records_per_page else AB.show_contacts()

    # for page in pages:
    #     for data in page:
    #         print(*data)
    records_per_page = int(args[0]) if args else None
    sac = ShowAllContacts()
    sac.print_data(AB, records_per_page)


def show_help(*args):
    helps = """\nPHONEBOOK COMMANDS:
'new contact <name> <phone> <email*> <birthday*>' - add new contact, * - optional
'add phone <name> <phone>' - add to your contact phone, format - 10 numbers
'edit birthday <name> <new_data>' - change already created birthday date, format - dd-mm-yyyy
'edit email <name> <old_data> <new_data>' - change already created email, format - example@gmail.com
'edit phone <name> <old_data> <new_data>' - change already created phone, format - 10 numbers
'delete birthday <name>' - delete already created birthday date
'delete email <name> <deleted_data>' - delete already created email address
'delete phone <name> <deleted_data>'  - delete already created phone number
'find phonebook <any data>' - <any data> to search data in phonebook
'show help' - show information for all commands
'show contacts' - show all contacts
'birthdays in <days>' -  to find users who has birthday in given gap. Days is not obligatory parameter\n
NOTES COMMANDS:
'add note'    - add a new note (all commands without parameters)
'delete note' - delete a note
'edit note'   - note editing
'edit tag'    - editing note tags
'find note'   - search for a note by name or text
'find tag'    - search for a note by tag
'show notes'  - display all notes
'show note'   - display a some note
'sort tag'    - a command that displays notes sorted by tags\n
OTHER COMMANDS:
'change phonebook'- change information in phonebook
'sort folder'     - sorted all your file in folder <path in your OS>\n"""
    print(helps)


@error_handler
def show_note(*args):
    """
    Show note in notebook

    :param args: None
    :return: None
    """
    name = input("Enter the name of the note you want to view: ")
    print(SNBCmd.show_some_note(name, NB))

    
@error_handler
def show_notes(*args):
    """
    Show all notes in notebook

    :param args: None
    :return: None
    """
    print(SNBCmd.show_all_notes(NB))


@error_handler
def sort_folder(*args) -> None:
    """
    Is used to sort given folder in categories

    :param args: OS path
    :return: None
    """
    if len(args) != 1:
        raise ValueError('Wrong path buddy')
    print(sorter(args[0]))


@error_handler
def sort_tag(*args):
    """
    Show sorted tags from notebook

    :param args: None
    :return: None
    """
    print(SNBCmd.sort_tag(NB))


def suitable_command(input_command: str) -> str:
    """
    Recursive function which is trying to find correct command in case of wrong command

    :param input_command: command to be found on
    :return: the best suitable command
    """
    for command in OPERATIONS. keys():
        if input_command in command:
            return command
    return suitable_command(input_command[:-1])


def wrong_command(*args):
    """
    Show more suitable command in it was wrong

    :param args: command action
    :return: None
    """
    input_command = f"{args[0]} {args[1]}"
    print(f"Maybe you mean {suitable_command(input_command)}")


def input_parser(user_input: str) -> list:
    """
    Is used to parse user input

    :param user_input: input string
    :return: list with query
    """
    stop_word = ('stop', 'exit', 'goodbye')
    for word in stop_word:
        if word in user_input.lower():
            return ['break', []]

    user_input = user_input.split()
    return ['wrong', 'command'] if len(user_input) < 2 else user_input


OPERATIONS = {
    'add birthday': add_birthday,
    'add email': add_email,
    'add phone': add_phone,
    'add note': add_note,
    'birthdays in': birthdays_in,
    'change notebook': change_notebook,
    'change phonebook': change_phonebook,
    'delete birthday': delete_birthday,
    'delete contact': delete_contact,
    'delete email': delete_email,
    'delete phone': delete_phone,
    'delete note': delete_note,
    'edit birthday': edit_birthday,
    'edit email': edit_email,
    'edit phone': edit_phone,
    'edit note': edit_note,
    'edit tag': edit_tag,
    'find tag': find_tag,
    'find note': find_note,
    'find phonebook': find_phonebook,
    'new contact': new_contact,
    'show contact': show_contact,
    'show contacts': show_contacts,
    'show help': show_help,
    'show note': show_note,
    'show notes': show_notes,
    'sort folder': sort_folder,
    'sort tag': sort_tag,
}

AB = AddressBook()
NB = NotesBook()
NBCmd = NotesCommands()
SNBCmd = ShowNotesCommands()

def handler() -> None:
    """
    Handler function which is accumulating all operations with phonebooks, notebooks and folder sorting

    :params: None
    :return: None
    """
    print('>>> Greetings! I am your CLI helper. Enter show help to see what can i do.'
          '\n>>> Or try yourself :)')
    while True:
        command, data_type, *query = input_parser(input('<<< '))
        if command == 'break':
            print('\nGoodbye! I will be waiting for you comeback :)')
            break

        action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
        if action.__name__ == 'wrong_command':
            action(command, data_type)

        else:

            if not query:
                query = []

            action(*query)
