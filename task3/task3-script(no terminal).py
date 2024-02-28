import json

def fill_values(tests, values_dict):
    for test in tests: #тут схож принцип работы с SQL, с оператором WHERE
        if 'id' in test and test['id'] in values_dict:
            test['value'] = values_dict[test['id']]
        if 'values' in test:
            fill_values(test['values'], values_dict)

def path_to_tests():
    tests_file = input('Введите полный путь до файла со структурой для построения отчетов, включая сам файл и его расширение.\n'
          'Пример: C:\GitHubRepo\LoadTesting\\task3\\tests.json\n\n')
    return tests_file

def path_to_values():
    values_file = input('Введите полный путь до файла с результатами тестов, включая сам файл и его расширение.\n'
          'Пример: C:\GitHubRepo\LoadTesting\\task3\\values.json\n\n')
    return values_file

def name_for_output_file():
    name_for_output_file = input('Введите название файла для вывода.\n')
    return name_for_output_file

def main():
    tests_file = path_to_tests()
    values_file = path_to_values()
    report_file = name_for_output_file()
    try:
        with open(tests_file, 'r') as f:
            tests = json.load(f)['tests']

        with open(values_file, 'r') as f:
            values = {item['id']: item['value'] for item in json.load(f)['values']}

        fill_values(tests, values)

        with open(f'{report_file}.json', 'w') as f:
            json.dump({'tests': tests}, f, indent=2)
            print('Enjoy')

    except Exception as ex:
        print(f'Error: {ex}')
        main()
if __name__ == "__main__":
    main()
