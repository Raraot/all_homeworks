from ast import main
from error_handler import error_handler

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models import Note, Phonebook

engine = create_engine("sqlite:///my_notebook.db")
Session = sessionmaker(bind=engine)
session = Session()


@error_handler
def add_note(*args) -> None:
    name = input("Enter note name: ")
    tag = input("Enter one tag for note: ")
    text = input("Enter note text: ")
    note = Note(name=name, text=text, tag=tag)
    session.add(note)
    session.commit()
    print(f'Note with name \033[47m\033[30m {name} \033[0m successfully added.')


@error_handler
def delete_contact(*args):
    fullname = input("Enter the fullname of the CONTACTs you want to delete: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        confirm = input("Do you really want to delete y/n: ")
        if confirm.lower() == "y":
            note_to_delete = session.query(Phonebook).filter_by(fullname=fullname).one()
            session.delete(note_to_delete)
            session.commit()
            print(f'Contact with name \033[47m\033[30m {fullname} \033[0m deleted.')


@error_handler
def delete_email(*args):
    fullname = input("Enter the fullname of the CONTACTs where you want to delete EMAIL: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        confirm = input("Do you really want to delete PHONE y/n: ")
        if confirm.lower() == "y":
            session.query(Phonebook).filter_by(fullname=fullname).update({Phonebook.email: ' '}, synchronize_session=False)
            session.commit()
            print(f'Phone numbers \033[47m\033[30m {fullname}s \033[0m has been deleted.')


@error_handler
def delete_phone(*args):
    fullname = input("Enter the fullname of the CONTACTs where you want to delete PHONE: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        confirm = input("Do you really want to delete PHONE y/n: ")
        if confirm.lower() == "y":
            session.query(Phonebook).filter_by(fullname=fullname).update({Phonebook.phone: ' '}, synchronize_session=False)
            session.commit()
            print(f'Phone numbers \033[47m\033[30m {fullname}s \033[0m has been deleted.')


@error_handler
def delete_note(*args):
    name = input("Enter the name of the note you want to delete: ")
    alls = session.query(Note).all()
    alli = []
    for a in alls:
        alli.append(a.name)
    if name not in alli:
        print(f'\033[33mNote with name \033[47m\033[30m {name} \033[0m\033[33m does not find\033[0m')
    else:
        confirm = input("Do you really want to delete y/n: ")
        if confirm.lower() == "y":
            note_to_delete = session.query(Note).filter_by(name=name).one()
            session.delete(note_to_delete)
            session.commit()
            print(f'Note with name \033[47m\033[30m {name} \033[0m deleted.')


@error_handler
def edit_email(*args) -> None:
    fullname = input("Enter the fullname of the CONTACTs where you want to edit EMAIL: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        edite = session.query(Phonebook).filter_by(fullname=fullname).one()
        print(f"Old  email: {edite.email}")
        new_email = input("New email: ")
        session.query(Phonebook).filter_by(fullname=fullname).update({Phonebook.email: new_email}, synchronize_session=False)
        session.commit()
        print(f'Email contact named \033[47m\033[30m {fullname} \033[0m edited.')


@error_handler
def edit_phone(*args):
    fullname = input("Enter the fullname of the CONTACTs where you want to edit PHONE: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        edite = session.query(Phonebook).filter_by(fullname=fullname).one()
        print(f"Old  phone: {edite.phone}")
        new_phone = input("New phone: ")
        session.query(Phonebook).filter_by(fullname=fullname).update({Phonebook.phone: new_phone}, synchronize_session=False)
        session.commit()
        print(f'Phone contact named \033[47m\033[30m {fullname} \033[0m edited.')


@error_handler
def edit_note(*args):
    name = input("Enter the name of the note you want to edit: ")
    alls = session.query(Note).all()
    alli = []
    for a in alls:
        alli.append(a.name)
    if name not in alli:
        print(f'\033[33mNote with name \033[47m\033[30m {name} \033[0m\033[33m does not find\033[0m')
    else:
        note_to_edite = session.query(Note).filter_by(name=name).one()
        print(f"Old  text note: {note_to_edite.text}")
        new_note = input("Edit text note: ")
        session.query(Note).filter_by(name=name).update({Note.text: new_note}, synchronize_session=False)
        session.commit()
        print(f'Note with name \033[47m\033[30m {name} \033[0m edited.')


@error_handler
def edit_tag(*args):
    name = input("Enter the name of the note where you want to edit TAG:")
    alls = session.query(Note).all()
    alli = []
    for a in alls:
        alli.append(a.name)
    if name not in alli:
        print(f'\033[33mNote with name \033[47m\033[30m {name} \033[0m\033[33m does not find\033[0m')
    else:
        note_to_edite = session.query(Note).filter_by(name=name).one()
        print(f"Old  TAG: {note_to_edite.tag}")
        new_tag = input("New TAG: ")
        session.query(Note).filter_by(name=name).update({Note.tag: new_tag}, synchronize_session=False)
        session.commit()
        print(f'Note with name \033[47m\033[30m {name} \033[0m updated tag.')



def new_contact(*args) -> None:
    fullname = input("Enter contacts fullname: ")
    phone = input("Enter contacts phone: ")
    email = input("Enter contacts email: ")
    phonebook = Phonebook(fullname=fullname, phone=phone, email=email)
    session.add(phonebook)
    session.commit()
    print(f'Contact with name \033[47m\033[30m {fullname} \033[0m successfully added.')


@error_handler
def find_note(*args):
    request = input("Enter a query to search in notes: ")
    # print(SNBCmd.find_note(request, NB))

    nnn = session.query(Note).all()
    print(33 * '.' + '\nI find next notes: \n' + 33 * '.')
    for n in nnn:
        if (request in n.name) or (request in n.text):
            print(f"       ID:  {n.id}\nName note:  {n.name}\nText note:  {n.text}\n      Tag:  {n.tag}")
            print(33 * '.')



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
    taggg = input("Enter a tag: ")
    nnn = session.query(Note).filter(Note.tag == taggg).all()
    print(33 * '.' + '\nI find next notes with this tag: \n' + 33 * '.')
    for n in nnn:
        print(f"       ID:  {n.id}\nName note:  {n.name}\nText note:  {n.text}\n      Tag:  {n.tag}")
        print(33*'.')


@error_handler
def show_contact(*args) -> None:
    fullname = input("Enter fullname of the contact you want to view: ")
    alls = session.query(Phonebook).all()
    alli = []
    for a in alls:
        alli.append(a.fullname)
    if fullname not in alli:
        print(f'\033[33mContact with fullname \033[47m\033[30m {fullname} \033[0m\033[33m does not find\033[0m')
    else:
        nnn = session.query(Phonebook).filter(Phonebook.fullname == fullname).all()
        for n in nnn:
            print(f"      ID:  {n.id}\nFullname:  {n.fullname}\n   Phone:  {n.phone}\n   Email:  {n.email}")
            print(33 * '.')


@error_handler
def show_contacts(*args) -> None:
    nnn = session.query(Phonebook).all()
    print(33 * '.'+'\nALL CONTACTS: \n'+33 * '.')
    for n in nnn:
        print(f"      ID:  {n.id}\nFullname:  {n.fullname}\n   Phone:  {n.phone}\n   Email:  {n.email}")
        print(33*'.')


def show_help(*args):
    helps = """\nPHONEBOOK COMMANDS:
'new contact' - add new contact  (all commands without parameters)
'edit email' - change already created email
'edit phone' - change already created phone
'delete email' - delete already created email address
'delete phone'  - delete already created phone number
'find phonebook' - to search data in phonebook
'help' - show information for all commands
'show contact' - show one contact by name
'show contacts' - show all contacts\n
NOTES COMMANDS:
'add note'    - add a new note (all commands without parameters)
'delete note' - delete a note
'edit note'   - note editing
'edit tag'    - editing note tags
'find note'   - search for a note by name or text
'find tag'    - search for a note by tag
'show notes'  - display all notes
'show note'   - display a some note\n"""
    print(helps)


@error_handler
def show_note(*args):
    name = input("Enter the name of the note you want to view: ")
    alls = session.query(Note).all()
    alli = []
    for a in alls:
        alli.append(a.name)
    if name not in alli:
        print(f'\033[33mNote with name \033[47m\033[30m {name} \033[0m\033[33m does not find\033[0m')
    else:
        nnn = session.query(Note).filter(Note.name == name).all()
        for n in nnn:
            print(f"       ID:  {n.id}\nName note:  {n.name}\nText note:  {n.text}\n      Tag:  {n.tag}")
            print(33*'.')

    
@error_handler
def show_notes(*args):
    nnn = session.query(Note).all()
    print(33 * '.'+'\nALL NOTES: \n'+33 * '.')
    for n in nnn:
        print(f"       ID:  {n.id}\nName note:  {n.name}\nText note:  {n.text}\n      Tag:  {n.tag}")
        print(33*'.')


def wrong_command(*args):
    print('Such a command does not exist. Enter >> help << to see all command.')


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
    'add note': add_note,
    'new note': add_note,
    'delete contact': delete_contact,
    'delete email': delete_email,
    'delete phone': delete_phone,
    'delete note': delete_note,
    'edit email': edit_email,
    'edit phone': edit_phone,
    'edit note': edit_note,
    'edit tag': edit_tag,
    'find tag': find_tag,
    'find note': find_note,
    'find phonebook': find_phonebook,
    'add contact': new_contact,
    'new contact': new_contact,
    'show contact': show_contact,
    'show contacts': show_contacts,
    'help': show_help,
    'show note': show_note,
    'show notes': show_notes,
}


def handler() -> None:

    print('I am your CLI helper. Enter >> help << to see all command.')
    while True:
        command, data_type, *query = input_parser(input('<<< '))
        if command == 'break':
            print('\nGoodbye!')
            break

        action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
        if action.__name__ == 'wrong_command':
            action(command, data_type)

        else:
            if not query:
                query = []

            action(*query)
