# Задание
    Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. Смысл - такой же, как на семинаре: сначала продумать архитектуру приложения, разбить задачу на отдельные модули и каждый модуль пишет отдельный человек (можно взять на себя и два, если количество модулей превышает количество человек).

    Под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*

    *Фамилия_1*

    *Имя_1*

    *Телефон_1*

    *Описание_1*

    *Фамилия_2*

    *Имя_2*

    *Телефон_2*

    *Описание_2*

    *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***

    *Фамилия_1,Имя_1,Телефон_1,Описание_1*

    *Фамилия_2,Имя_2,Телефон_2,Описание_2*

    *и т.д.*


## Бэклог
1. [parsing_format.py](https://github.com/GeekDevTeam/Calc-Console-App/tree/master/src/parsing_format.py) - модуль для парсинга данных заданных в разных форматах
    - [ ] Добавить словарь 
    ```
    FORMATS = [
        { # по-хорошему задать массив через точное определние структуры с помощью классов, но пока я не пробовал классы в питоне
            'formatDataDelimeter': '\n', # разделитель между форматами хранения
            'userDataDelimeter': ';', # разделитель данных пользователей
            'userPropertiesDelimeter': ',',  # разделитель свойств пользователя

            # Пример входного файла с данными: 
            # "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n"
        },
        {
            'formatDataDelimeter': '\t',
            'userDataDelimeter': ';',
            'userPropertiesDelimeter': ',',

            # пример входного файла с данными: 
            # "   ;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;    "
        },
        {
            'formatDataDelimeter': '%',
            'userDataDelimeter': ';',
            'userPropertiesDelimeter': ',',

            # пример входного файла с данными: 
            # "%;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;%"
        }

        пример входного файла с данными:
        "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n   ;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;    %;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;%"
    ]
    ```
    - [ ] Добавить метод `parse_userProperties_by_delimeter(properties: string, userPropertiesDelimeter: string)`. Метод должен возвращать массив, из данных `properties`, разделенных с помощью `userPropertiesDelimeter`
    - [ ] Добавить метод `parse_userData_by_delimeter(usersData: string, userDataDelimeter: string)`. 
        * Метод должен возвращать массив данных по каждому пользователю
        * Алгоритм: 
            1. Разбиваем строку `userData` с помощью разделителя `userDataDelimeter` -> получаем массив строк свойств пользователя
            2. Для каждого элемента массива 
                1. вызываем метод `parse_userProperties_by_delimeter`
                2. Полученный результат добавляем в массив `parsed_usersData`
            3. Возвращаем сформировавшийся массив `parsed_usersData`
    - [ ] Добавить метод `parse_formatData_by_delimeter(formatData: string, formatDataDelimeter: string)`
        * Метод должен возвращать массив, из данных `formatData`, разделенных с помощью `formatDataDelimeter`
        * Алгоритм: 
            1. Разбиваем строку `formatData` с помощью разделителя `formatDataDelimeter` -> получаем массив строк одного формата хранения
            2. Для каждого элемента массива 
                1. вызываем метод `parse_userData_by_delimeter`
                2. Полученный результат добавляем в массив `parsed_formatData`
            3. Возвращаем сформировавшийся массив `parsed_formatData`