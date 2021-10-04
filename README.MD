Это консольное приложение.
Результат сохраняется в файл таблицу под названием flats.csv в корневую папку приложения

1.
Чтобы авито не забанил в переменной HEADERS указываем свои Accept и User-Agent

Пример:
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36'
}

2.
В функции "save_doc" меняет нужно кол-во минут, которое уже висит объявление

Пример для 15 минут:
                    if time_number < 15:

3.
Если нет желания каждый раз вводить кол-во страниц для парсинга, тогда в функции "parser" присваиваем переменной PAGENNATION нужное кол-во страниц
Строку с input для ввода закоментируем(в примере) или удаляем.

Пример для 3 страниц: 
    PAGENATION = 3
    # PAGENATION = input('Введите кол-во страниц для парсинга: ')
    # PAGENATION = int(PAGENATION.strip())

4.
Устанавливает вилку цен от и до в функции "parser" 

Пример максимальная цена 45000 руб. минимальная 27000 руб.:
                'pmax': 45000,
                'pmin': 27000,

5. Тип объявления в функции "parser" можно сменить тип объявлений от частных до агенств.

0 - Все
1 - Частные
2 - Агенства

Пример для всех объявлений:
                 'user': 0

6. Чтобы сменить кол-во комнат в квартире нужно заменить актуальную ссылку с 1 лишь параметром кол-во комнат, присвоив значение переменной URL

Пример для однокомнатной:
URL = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok/1-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUjlk'

Пример для двухкомнатной
URL = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok/2-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUkFk'

7. По тому же принципу меняется город поиска объявлений.

Приложение писалось для личных нужд, GUI и допиливание не предвидется.
Old версия осталось под старую верстку avito. При краше рекомендую проверить не изменилась ли верстка у авито и заменить в функции get_content актуальные теги и классы.