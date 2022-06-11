import convert_format
import parsing_format

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

    #     пример входного файла с данными:
    #     "\n;Фамилия_1,Имя_1,Телефон_1,Описание_1;;Фамилия_2,Имя_2,Телефон_2,Описание_2;\n   ;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;    %;фамилия_1,имя_1,телефон_1,описание_1;;фамилия_2,имя_2,телефон_2,описание_2;%"
]