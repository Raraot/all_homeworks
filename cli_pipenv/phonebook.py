from collections import UserDict
from datetime import date, datetime, timedelta
import re
from pathlib import Path
import pickle
from typing import Optional, List, Generator
from abc import ABC, abstractmethod
import errors


class Field:

    def __init__(self, value) -> None:
        self._value = None  # Private not Hidden!!!
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value) -> None:
        self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, value: str = None) -> None:  # dd-mm-yyyy -> %d-%m-%Y

        try:
            self._value = datetime.strptime(value, '%d-%m-%Y').date()  # raise ValueError if wrong
        except ValueError:
            raise errors.WrongBirthday('Data should be in format dd-mm-yyyy')

    def __repr__(self) -> str:
        return self.value.strftime('%d-%m-%Y')

    def __str__(self) -> str:
        return self.value.strftime('%d-%m-%Y')


class Email(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        __pattern = r"^[a-zA-Z][\w.]+@([a-zA-Z]{2,}[.][a-zA-Z]{2,}|[a-zA-Z]{2,}[.][a-zA-Z]{2,}[.][a-zA-Z]{2,})$"
        if re.match(__pattern, value):
            self._value = value

        else:
            raise errors.WrongEmail(f"Looks like {value} is a wrong email")

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


class Name(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        if len(value) <= 100:
            self._value = value
        else:
            raise errors.LongName('Entered contacts name is too long')

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


class Phone(Field):

    @Field.value.setter
    def value(self, value: str) -> None:

        if len(value) == 10 and value.isdigit():
            self._value = value

        else:
            raise errors.WrongPhone(f"Looks like {value} is a wrong number. It must be 10 digits")

    def __repr__(self) -> str:
        return f"+38({self.value[:3]}){self.value[3:6]}-{self.value[6:8]}-{self.value[8:]}"  # +38(012)34-567-89

    def __str__(self) -> str:
        return f"+38({self.value[:3]}){self.value[3:6]}-{self.value[6:8]}-{self.value[8:]}"  # +38(012)34-567-89


class Record:
    """
    Contact record
    Attributes: name, phones, birthday, emails
    """
    def __init__(self, name: Name, phones: Optional[List[Phone]] = None,
                 birthday: Optional[Birthday] = None, emails: Optional[List[Email]] = None) -> None:

        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.emails = emails

    def add_birthday(self, birthday: Birthday) -> str:
        """
        Adding new birthday to current record

        :param birthday: instance of Birthday
        :return: string with result
        """
        if self.birthday is None:
            self.birthday = birthday
        else:
            return "Birthday exists"
        return "Birthday added"

    def add_email(self, email: Email) -> str:
        """
        Adds new email to current record

        :param email: instance of Email
        :return: string with result
        """
        if self.emails is None:
            self.emails = [email]
        else:
            self.emails.append(email)
        return "Email added"

    def add_phone(self, phone: Phone) -> str:
        """
        Adding new phone to current record

        :param phone: instance of Phone
        :return: string with result
        """
        if self.phones is None:
            self.phones = [phone]
        else:
            self.phones.append(phone)
        return "Phone number added"

    def change_birthday(self, new_birthday: Birthday) -> str:
        """
        Changing user birthday

        :param new_birthday: instance of Birthday
        :return: string with result
        """
        if self.birthday is not None:
            self.birthday = new_birthday
            return "Birthday changed"

        return "Birthday does not exist"

    def change_email(self, old_email: str, new_email: Email) -> str:
        """
        Changing user email

        :param old_email: email to be changed
        :param new_email: instance of Email
        :return: string with result
        """
        for email in self.emails:
            if email.value == old_email:
                self.emails.remove(email)
                self.emails.append(new_email)
                return "Email changed"

        return f"{old_email} does not exist"

    def change_phone(self, old_phone: str, new_phone: Phone) -> str:
        """
        Changing user phone

        :param old_phone: phone to be changed
        :param new_phone: instance of Phone
        :return: string with result
        """
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.append(new_phone)
                return "Phone number changed"

        return f"{old_phone} does not exist"

    def delete_birthday(self) -> str:
        """
        Deleting birthday

        :param: None
        :return: string with result
        """
        if self.birthday:
            self.birthday = None
            return "Birthday deleted"

        return "Birthday does not exist"

    def delete_email(self, email_to_delete: str) -> str:
        """
        Deleting email

        :param email_to_delete: email to be deleted
        :return: string with result
        """
        for email in self.emails:
            if email.value == email_to_delete:
                self.emails.remove(email)
                return "Email deleted"

        return f"{email_to_delete} does not exist"

    def delete_phone(self, phone_to_delete: str) -> str:
        """
        Deleting phone

        :param phone_to_delete: phone to be deleted
        :return: string with result
        """
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone)
                return "Phone number deleted"

        return f"{phone_to_delete} does not exist"


class AddressBook(UserDict):

    __fields = ('name', 'phones', 'emails', 'birthday')
    __records_per_page = 2

    def __init__(self):
        super().__init__(self)
        self.__book_name = 'phonebook'
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
        path = path.joinpath(f'{self.__book_name}.phone')
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
                    if not isinstance(book, AddressBook):  # If data not AddressBook object
                        print(f'Wrong data in {self.__book_name}\nBook has not been restored')
                        return {}
                except EOFError:  # If file is empty
                    return {}
            print(f'{self.__book_name} data has been restored')
            return book.data
        else:  # If file does not exist
            return {}

    def __save(self) -> None:
        """
        Saving data in given path
        :return: None
        """
        with open(self.__path, 'wb') as file:
            pickle.dump(self, file)

        print(f"Phonebook has been saved to {self.__book_name}")

    def add_contact(self, record: Record) -> None:
        """
        Create new contact in phonebook

        :param record: Record instance with contact information
        :raise ContactExists: if contact is phonebook
        :return: None
        """
        contact = record.name.value
        if contact in self.data:
            raise errors.ContactExists(f"{contact} is already in your contacts")

        self.data[contact] = record
        self.__save()

    def changed_contact_data(self, record: Record) -> str:
        """
        Is used change contact data
        :param record: record to be changed
        :return:
        """
        self.data[record.name.value] = record
        self.__save()

        return f"Data has been changed"

    def change_book(self, book_name: str):

        self.__book_name = book_name
        self.__path = self.__path_file()
        self.data = self.__restore()

    def delete_contact(self, contact: str) -> str:
        """
        Delete contact from phonebook

        :param contact: contact name to be deleted
        :return: Message if contact was deleted
        :raise: KeyError if no given contact in phonebook
        """
        if contact not in self.data:
            raise KeyError(f"{contact} is not in your phonebook")

        self.data.pop(contact)
        self.__save()

        return f"{contact} has been deleted"

    def find_record(self, search: str) -> str | dict[list]:
        """
        Show records with similar or exact data

        :param search: information to search
        :return: dictionary with key is a username and value it's matched data
        :raise EmptySearchString if search string is empty
        """
        if not search:
            raise errors.EmptySearchString

        matched_information = {}
        for record in self.data.values():  # type: Record
            information = []
            for field in self.__fields:

                record_field = getattr(record, field)
                if record_field is None:
                    continue

                if isinstance(record_field, list):  # type: List[Phone] | List[Email]
                    data_in_field = [data for data in record_field if search in data.value]
                    if data_in_field and None not in data_in_field:
                        information.append([field, *data_in_field])

                elif isinstance(record_field, Birthday):  # type: Birthday
                    if search in record_field.value.strftime('%d-%m-%Y'):
                        information.append([field, record_field])

                elif isinstance(record_field, Name):
                    if search in record_field.value:  # type: Name
                        information = [record_field.value]

            if information:
                matched_information[record.name.value] = information.copy()
                information.clear()

        return matched_information

    def show_near_birthdays(self, days: int = 30) -> list:
        """
          Show users and their birthdays in given days

        :param days: days interval
        :return: list of birthday persons in the nearest days
        """
        current_date = datetime.now().date()
        birthdays = []
        time_gap: date = current_date + timedelta(days)
        for record in self.data.values():  # type: Record

            if record.birthday:
                birthday = record.birthday.value.replace(year=current_date.year)

                if current_date <= birthday <= time_gap:

                    birthdays.append(
                        f"{record.name.value} has birthday {record.birthday.value.strftime('%d %B')}"
                        f" in {(birthday - current_date).days} days"
                    )

        return birthdays

    def show_contacts(self, records_per_page: int = None) -> Generator:
        """
        Show fields from records on page.

        :param records_per_page: number of fields shown on one page
        :Generator: yield fields per one page
        """
        if not self.data:
            raise KeyError('No contacts in your phonebook')
        if records_per_page:
            self.__records_per_page = records_per_page

        total_pages = len(self.data) / self.__records_per_page if len(self.data) % self.__records_per_page == 0 else \
            (len(self.data) // self.__records_per_page) + 1
        total_pages = int(total_pages)
        current_page = 1
        page_info = []
        on_page = 0

        for record in self.data.values():
            for field in self.__fields:
                record_field = getattr(record, field)

                if record_field is None:
                    page_info.append([f"{field}:", 'No data'])  # type: None

                elif isinstance(record_field, list):
                    page_info.append([f"{field}:", *record_field])  # type: List[Phone] | List[Email]

                else:
                    page_info.append([f"{field}:", record_field])  # type: Birthday | Name

            on_page += 1

            if on_page == self.__records_per_page:

                page_info.append([f"{current_page} page of {total_pages} pages\n"])
                yield page_info
                page_info.clear()
                current_page += 1
                on_page = 0

        else:
            if current_page == total_pages:
                page_info.append([f"{current_page} page of {total_pages} pages\n"])
                yield page_info

    def show_record_data(self, contact: str) -> list:

        record: Record = self.data.get(contact)
        if record is None:
            raise KeyError(f"No {contact} in your {self.__book_name} phonebook")
        data = []
        for field in self.__fields:
            record_field = getattr(record, field)

            if record_field is None:
                data.append([f"{field}:", 'No data'])  # type: None

            elif isinstance(record_field, list):
                data.append([f"{field}:", *record_field])  # type: List[Phone] | List[Email]

            else:
                data.append([f"{field}:", record_field])  # type: Birthday | Name

        return data

class IConsoleAdressbook(ABC):

    @abstractmethod
    def print_data(self, adressbook, data):
        pass


class ShowSomeContact(IConsoleAdressbook):

    def print_data(self, adressbook, name):
        result = adressbook.show_record_data(name)
        for field in result:
            print(*field)


class ShowAllContacts(IConsoleAdressbook):

    def print_data(self, adressbook, records_per_page):
        pages = adressbook.show_contacts(records_per_page) if records_per_page else adressbook.show_contacts()
        for page in pages:
            for data in page:
                print(*data)