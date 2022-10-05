from collections import UserDict
from datetime import datetime
from pathlib import Path
from abc import ABC, abstractmethod
import pickle


class INotesBook(ABC):

    @abstractmethod
    def change_book(self, book_name):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_in_file(self):
        pass

class INotesCommands(ABC):

    @abstractmethod
    def add_note(self, name, tags, note, notesbook):
        pass

    @abstractmethod
    def delete_note(self, name, notesbook):
        pass

    @abstractmethod
    def edit_note(self, name, note, notesbook):
        pass

    @abstractmethod
    def get_note(self, name,  notesbook):
        pass

    @abstractmethod
    def edit_tags(self, name, tags, notesbook):
        pass

    @abstractmethod
    def get_tags(self, name,  notesbook):
        pass

class IShowNotesCommands(ABC):

    @abstractmethod
    def show_some_note(self, name,  notesbook):
        pass

    @abstractmethod
    def show_all_notes(self, notesbook):
        pass

    @abstractmethod
    def find_note(self, request, notesbook):
        pass

    @abstractmethod
    def find_tag(self, tag, notesbook):
        pass

    @abstractmethod
    def sort_tag(self, notesbook):
        pass

class NotesBook(INotesBook, UserDict):

    def __init__(self):
        super().__init__(self)

        self.__book_name = 'notebook'
        self.__path = self.__path_file()
        self.data = self.__restore()

    def __path_file(self) -> Path:
        """
        Path where self data is stored

        :return: Path
        """
        BASE_DIR = Path(__file__).parent
        path = BASE_DIR.joinpath('data')
        path.mkdir(exist_ok=True)
        path = path.joinpath(f'{self.__book_name}.note')
        return path

    def __restore(self):
        """
        Is used to restore saved book if it exists

        :return: saved or empty book
        """
        if self.__path.exists() and self.__path.is_file():
            with open(self.__path, 'rb') as file:
                try:
                    book = pickle.load(file)
                    if not isinstance(book, NotesBook):  # If data not AddressBook object
                        print(f'Wrong data in {self.__book_name}\nBook has not been restored')
                        return {}
                except EOFError:  # If file is empty
                    return {}
            print(f'{self.__book_name} data has been restored')
            return book.data
        else:  # If file does not exist
            return {}

    def change_book(self, book_name: str) -> None:

        self.__book_name = book_name
        self.__path = self.__path_file()
        self.data = self.__restore()

    def read_file(self) -> None:
        try:
            with open(self.__path, 'rb') as fh:
                unpacked = pickle.load(fh)
                self.data = unpacked
        except FileNotFoundError:
            self.data = {}

    def save_in_file(self) -> None:
        with open(self.__path, 'wb') as fh:
            pickle.dump(self, fh)

class NotesCommands(INotesCommands):

    def add_note(self, name: str, tags: str, note: str, notesbook: NotesBook) -> str:
        """the function of adding a new note"""
        notesbook.read_file()
        create = datetime.now()
        if name not in notesbook.data:   
            list_tags = []
            for i in tags.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('  ', ' ').split(' '):
                list_tags.append(i)
            note_data = {"tags": list_tags, "create": create.strftime("%d.%m.%Y %H:%M"), "note": note}
            notesbook.data[name] = note_data
            notesbook.save_in_file()
            return (f'Note with name \033[47m\033[30m {name} \033[0m successfully added.')
        else:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m exists, if you want to change it enter the command: edit note\033[0m')

    def delete_note(self, name: str, notesbook: NotesBook) -> str:
        """function to delete a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            del notesbook.data[name]
            notesbook.save_in_file()
            return (f'Note with name \033[47m\033[30m {name} \033[0m deleted.')

    def edit_note(self, name: str, note: str, notesbook: NotesBook) -> str:
        """note editing function"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            notesbook.data[name]["note"] = note
            notesbook.save_in_file()
            return (f'Note with name \033[47m\033[30m {name} \033[0m edited.')

    def get_note(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the content of a note, for example, for editing the text of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["note"]

    def edit_tags(self, name: str, tags: str, notesbook: NotesBook) -> str:
        """function of editing tags in a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            list_tags = []
            for i in tags.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('  ', ' ').split(' '):
                list_tags.append(i)
            notesbook.data[name]["tags"] = list_tags
            notesbook.save_in_file()
            return (f'Tags in note \033[47m\033[30m {name} \033[0m edited.')

    def get_tags(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the tags of a note, for example, for editing the tags of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["tags"]    

class ShowNotesCommands(IShowNotesCommands):
    def show_some_note(self, name: str,  notesbook: NotesBook) -> str:
        """function to display some note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            result = f'''\n  name:  {name}\n  tags:  {", ".join(notesbook.data[name]["tags"])}\ncreate:  {notesbook.data[name]["create"]}\n  note:  {notesbook.data[name]["note"]}\n'''
            return result

    def show_all_notes(self, notesbook: NotesBook) -> str:
        """function to display all notes"""
        notesbook.read_file()
        result = "\033[32m\n*** ALL YOUR NOTES ***\033[0m\n"
        for k, v in notesbook.data.items():
            result += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        return result

    def find_note(self, request: str, notesbook: NotesBook) -> str:
        """function to search for a note by title or content"""
        notesbook.read_file()
        find = ""
        for k, v in notesbook.data.items():
            if (request.lower() in k.lower()) or (request.lower() in v["note"].lower()):
                find += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        if find == "":
            return ('\033[33m*** No notes found for your request ***\033[0m')
        else:
            result = "\033[32m\n*** FIND NEXT NOTES ***\n\033[0m" + find
            return result

    def find_tag(self, tag: str, notesbook: NotesBook) -> str:
        """function to search for a note by tag"""
        notesbook.read_file()
        find = ""
        all_tags = []
        for k, v in notesbook.data.items():
            all_tags.extend(v["tags"])
            if (tag.lower() in v["tags"]) or (tag in v["tags"]):
                find += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        available = ', '.join(set(all_tags))
        if tag == "available":
            return("\nIn all your Notes are available next tags :\n" + available + "\n")
        elif find == "":
            return(f'\033[33m*** No notes found with tag \033[43m {tag} \033[0m\033[33m ***\033[0m')
        else:
            result = f"\033[32m\n*** Find next notes with tag \033[42m {tag} \033[0m\033[32m ***\n\033[0m" + find
            return result

    def sort_tag(self, notesbook: NotesBook) -> str:
        """function to display all notes sorted by tags alphabetically"""
        notesbook.read_file()
        result = ""
        all_tags = []
        for k, v in notesbook.data.items():
            all_tags.extend(v["tags"])
        for n in sorted(set(all_tags)):
            result += f"\033[4mNotes with tag {n}:\033[0m\n"
            for k, v in notesbook.data.items():
                if (n.lower() in v["tags"]) or (n in v["tags"]):
                    result += f'''  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        return result
