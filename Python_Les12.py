import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

run_dir = os.path.join(current_dir, migrations)


def all_files():
    files_list = []
    for file in os.listdir(run_dir):
        if os.path.splitext(file)[1] == '.sql':
            files_list.append(file)
    return files_list


def search_files(files, search_term):
    for file in files:
        if file.lower().find(search_term) == -1:
            files.remove(file)
        else:
            continue
    if len(files) == 0:
        print('Такой поиск ничего не дал')
    print(files)
    print('Всего файлов:', len(files))


def search():
    files = all_files()
    while True:
        user_search = input('Введите строку (для выхода наберите exit): ').lower()
        if user_search == 'exit':
            break
        else:
            search_files(files, user_search)


search()
