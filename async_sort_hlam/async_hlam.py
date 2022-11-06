import asyncio
import re
from aiopath import AsyncPath
from aioshutil import copyfile

DICT_REPORT = {}

async def collect_folders(path):
    async for i in path.iterdir():
        if await i.is_dir():
            await collect_folders(i)
        else:
            await copy_file(i)

async def copy_file(file):
    ext = file.suffix.replace('.', 'files_')
    new_path = output_path / ext
    try:
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(file, new_path / transliteration(file.name))
        DICT_REPORT[ext] = DICT_REPORT.get(ext, 0) + 1
    except OSError as err:
        print('OSError when copy {file} file')


def reporting():
    printing = f"\nПід час роботи сортувальника розібрано папку {source_path.name}\nта переміщено в папку {output_path.name} наступні файли:\n"
    for key, value in DICT_REPORT.items():
        printing += f" - підпапка {key}, кількість файлів - {value} з розширенням {key.replace('files_','.')}\n"
    print(printing+'--- Дякуємо за використання нашого сортувальнка файлів ---\n')

def transliteration(text):
    trans_map = {
    ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B', ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G',
    ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E', ord('ё'): 'e', ord('Ë'): 'E', ord('ж'): 'j', ord('Ж'): 'J',
    ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I',  ord('й'): 'j', ord('Й'): 'J', ord('к'): 'k', ord('К'): 'K',
    ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M', ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O',
    ord('п'): 'p', ord('П'): 'P', ord('р'): 'r', ord('Р'): 'R', ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T',
    ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F', ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'TS',
    ord('ч'): 'ch', ord('Ч'): 'CH', ord('ш'): 'sh', ord('Ш'): 'SH', ord('щ'): 'sch', ord('Щ'): 'SCH', ord('ъ'): '', ord('Ъ'): '',
    ord('ы'): 'y', ord('Ы'): 'Y', ord('ь'): '', ord('Ь'): '', ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'yu', ord('Ю'): 'YU',
    ord('я'): 'ja', ord('Я'): 'JA', ord('є'): 'ye', ord('Є'): 'YE', ord('ї'): 'ji', ord('Ї'): 'JI', ord('ї'): 'і', ord('І'): 'I',
    ord('ґ'): 'g', ord('Ґ'): 'G', ord('.'): '.'
    }
    trans_text = text.translate(trans_map)
    trans_text = re.sub(r'[\.]\W', '_', trans_text)
    return trans_text



if __name__ == '__main__':
    
    inp_source = input("\nВведіть назву папки яку потрібно розібрати (сортувати): ")
    inp_output = input("\nВведіть назву папки в яку потрібно зложити файли: ")
    source_path = AsyncPath(inp_source)
    output_path = AsyncPath(inp_output)

    asyncio.run(collect_folders(source_path))
    reporting()



# python3 async_hlam.py

