# 1. Прочитать файлик HW_Files.txt
# 2. Преобразовать его в json, где имя ключ, значение - фамилия
# 3. Записать в файлик json с сортировкой по ключам

import json

friends_list = (open('HW_Files.txt', 'r', encoding='utf-8')).read()
friends_dict = dict(name.split(',') for name in friends_list.split('\n'))
with open("griffindors.json", "w", encoding='utf-8') as file:
    json.dump(
        friends_dict,
        file,
        indent=4,
        ensure_ascii=False,
        sort_keys=True
    )
