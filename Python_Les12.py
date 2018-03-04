import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

run_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), migrations)


def all_files():
    files_list = []
    for file in os.listdir(run_dir):
        if (file.split('.')[-1]) == 'sql':
            files_list.append(file)
    return files_list


def search_files(files, search_term):
    file_list = []
    for file in files:
        for term in search_term:
            if file.lower().find(term) == -1:
                continue
            else:
                file_list.append(file)
    if len(file_list) == 0:
        return 'Такой поиск ничего не дал'
    print(file_list)
    print('Всего файлов:', len(file_list))
    return True


while True:
    files = all_files()
    search_term = []
    user_search = input('Введите строку (для выхода наберите exit): ').lower()
    if user_search == 'exit':
        break
    else:
        search_term.append(user_search)
        search_files(files, search_term)
