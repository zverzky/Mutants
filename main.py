def read_mutants_file():
    mutabts_day = ["day", "night", "evening", "morning"]

    with open('all_mutant.txt', 'r', encoding='utf-8') as file:
        for item in file.readlines():
            s = item.split(">")
            cords = s[0][s[0].find("<") + 1:].replace(",", "").split(" ")
            cords[1] = "0"
            cords = " ".join(cords)
            classname = item.split(">")
            classname = classname[1][1:-2]

            for file_name in mutabts_day:
                with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
                    f.write(f'\n{classname}|{cords}|1|3600')
                    print(f'Животое {classname} добавлено в файл {file_name}!')


read_mutants_file()