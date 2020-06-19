import argparse
from collections import defaultdict
import bs4
import pandas as pd
import requests
values_to_find = [
    'дата рождения',
    'место рождения',
    'место проживания',
    'лагерное управление',
    'национальность',
    'дата ареста',
    'кем приговорен',
    'приговор',
    'книга памяти',
]


def main():
    # Сбор информации из аргументов командной строки
    parser = argparse.ArgumentParser(description='Сбор информации о '
                                     'репрессированных')
    parser.add_argument('link', help='ссылка на человека')
    parser.add_argument(
        '--output',
        help='файл для сохранения результата(файл перезапишется!)'
        '(по умолчанию result.xlsx)',
        type=argparse.FileType('wb+'),
        default='result.xlsx'
    )
    args = parser.parse_args()

    # Скачивание страницы
    req = requests.get(args.link)
    # Если ссылка не найдена или возникла другая ошибка
    if req.status_code != 200:
        print('От сервера получена ошибка:', req.status_code)
        exit(1)

    text = req.text

    # конструирование BeautifulSoup
    soup = bs4.BeautifulSoup(text, 'html.parser')
    result = defaultdict(list)
    # поиск элемента карточки
    card = soup.find('div', {'class': 'event'})
    # поиск пар классов (nameEvent, dataEvent) и итерация по каждой паре
    for k, v in zip(card.find_all(None, {'class': 'nameEvent'}), 
                    card.find_all(None, {'class': 'dataEvent'})):
        # поиск всех строк данного элемента
        keys = list(k.strings)
        values = list(v.strings)
        # если ключ пустой
        if not keys:
            continue
        # если значение пустое
        if not values:
            value = 'NA'
        else:
            # соединям все строки
            value = ''.join(values).strip()

        # приводим ключ к удобному формату
        key = keys[0].strip().replace(':', '')

        # проверка, есть ли ключ в списке необходимых
        if key.lower() not in values_to_find:
            continue
        result[key].append(value)

    # заполняем пропущенные значения
    for key in values_to_find:
        if key not in result:
            result[key] = ['NA']

    # форматирование результата
    formatted_result = {}
    for key, value in result.items():
        # если значение пропущенно, ставим null(None в Python)
        if not value:
            formatted_result[key] = 'NA'
        else:
            # разделяем ; все значения
            formatted_result[key] = ';'.join(value)

    df_existing = pd.DataFrame(columns=values_to_find)
    .append([formatted_result], sort=True)

    # запись в файл
    df_existing.to_excel(args.output, index=False)


if __name__ == '__main__':
    main()
