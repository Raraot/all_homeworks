## PythonCore7 final project. Team-2
### СLI helper
This is concole line helper. It was created as final project in **GoIT PythonCore7** studying course.
It is separated ot two main parts. First part is **phonebook** and second is **notebook**.
Commands which are able for each will be presented in a while. If command is wrong helper will try to predict
desired command
### Please mention that to correct operation you need to use spaces as separator between entered data.
<br>

<h3>To install package <p>pip install -i https://test.pypi.org/simple/ CLI-helper</p> </h3>

#### Phonebook commands:
* new contact <**name**> <**phone(s)**> <**email(s)**> <**birthday**> - command for adding new contact in phonebook.
Contact name is the only _*obligatory*_ data, phone(s), email(s) and birhday can be added afterwars if needed.
* add phone <**name**> <**phone**> - adding new phone number to your existing contact in phonebook. Format - __10 digits__.
* birthdays in <**days**> - to find users who have birthday in given gap. Days is not obligatory parameter.
* change phonebook <**book name**> - changing user phonebook to given. If it exists it will restore saved data.
Otherwise new phonebook file will be created. By default name is **phonebook**.
* edit birthday <**name**> <**new data**> - change birthday in existing contact. Format is __dd-mm-yyyy__
* edit email <**name**> <**old data**> <**new data**> - change email in existing contact.
* edit phone <**name**> <**old data**> <**new data**> - change existing phone in given contact, format - 10 __digits__
* delete birthday <**name**> - delete birthday in phonebook contact
* delete email <**name**> <**email to delete**> - delete existing email in given contact record. 
* delete phone <**name**> <**deleted_data**>  - delete existing phone number from contact record.
* find phonebook <**any data**> - searching any similar data in phonebook
* show contacts - show all contacts in current phonebook
* show contact <**name**> - show given contact in current phonebook

#### NOTES COMMANDS:
_*all commands without parameters*_
* add note    - add a new note 
* delete note - delete a note
* edit note   - note editing
* edit tag    - editing note tags
* find note   - search for a note by name or text
* find tag    - search for a note by tag
* show notes  - display all notes
* show note   - display an exact note
* sort tag    - a command that displays notes sorted by tags\n

#### OTHER COMMANDS:

* sort folder <**path in OS**> - sorted all your files in given folder according to follwing criterias: \
**images** JPEG, PNG, JPG, SVG \
**video** AVI, MP4, MOV, MKV \
**documents** DOC, DOCX, TXT, PDF, XLSX, PPTX \
**audio** MP3, OGG, WAV, AMR \
**archives** ZIP, GZ, TAR \
_Archives_ will be unpacked in same folder as its name. \
Files with unknown extensions will be replaced to unknown folder \
Empty folders will be deleted. \
Only latin symbols and "_" sign are allowed, otherwise files and in case of archives folders will be renamed\n"""
* show help - show information for all commands

### Data will be saved after program completion
