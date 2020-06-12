# Сбор информации о репрессированных с сайта https://bessmertnybarak.ru
Напишите программу для сбора информации о репрессированных с сайта https://bessmertnybarak.ru. Используйте эту программу для сбора информации о 100 любых репрессированных. Выложите на github код и ссылку на google drive с датасетом. 

Входные данные: 
ссылка на страницу репрессированного (пример: https://bessmertnybarak.ru/adelgeym_evgeniy_vladimirovich/)

Выходные данные:
Excel-файл со следующими колонками:
1. Дата рождения;
2. Место рождения;
3. Место проживания;
4. Лагерное управление;
5. Национальность;
6. Дата ареста;
7. Кем приговорен;
8. Приговор;
9. Книга Памяти.

Если на странице списка отсутствует какая-то информация из требуемых, в таблицу следует записать NA. На странице некоторые пункты могут быть продублированы. Следует сохранить всё, что указано, в записи, разделив точкой с запятой.

Используйте библиотеку BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) для сбора информации с сайта и pandas (https://pandas.pydata.org/) для сохранения информации в excel-файл.
