from threading import Thread
from pathlib import Path
from shutil import copyfile

LIST_ZVIT = {}

def collect_folders(path: Path):
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i)
            collect_folders(i)

def reporting():
    printing = f"\nПід час роботи сортувальника розібрано папку {inp_source}\nта переміщено в папку {inp_output} наступні файли:\n"
    for key, value in LIST_ZVIT.items():
        printing += f" - підпапка {key}, кількість файлів - {value} з розширенням {key.replace('files_','.')}\n"
    print(printing+'--- Дякуємо за використання нашого сортувальнка файлів ---\n')

class CopyFilesThread(Thread):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        for n in self.path.iterdir():
            if n.is_file():
                ext = n.suffix.replace('.', 'files_')
                new_path = output_path / ext

                try:
                    new_path.mkdir(exist_ok=True, parents=True)
                    copyfile(n, new_path / n.name)
                    LIST_ZVIT[ext] = LIST_ZVIT.get(ext, 0) + 1
                except OSError as err:
                    print('OSError when copy {n} file')


if __name__ == '__main__':
    
    inp_source = input("\nВведіть назву папки яку потрібно розібрати (сортувати): ")
    inp_output = input("\nВведіть назву папки в яку потрібно зложити файли: ")
    source_path = Path(inp_source)
    output_path = Path(inp_output)
    folders = []
    folders.append(source_path)
    collect_folders(source_path)

    threads = []
    for folder in folders:
        th = CopyFilesThread(folder)
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

    reporting()



# python3 hlam.py