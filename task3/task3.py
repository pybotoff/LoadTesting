import json
import sys

def fill_values(tests, values_dict):
    for test in tests:
        if 'id' in test and test['id'] in values_dict:
            test['value'] = values_dict[test['id']]
        if 'values' in test:
            fill_values(test['values'], values_dict)

def main():
    if len(sys.argv) != 4:
        print("Использовать:\n"
              ">> cd C:\YourWay\\task3\n"
              ">> python task1.py tests.json values.json report.json")
        return

    tests_file, values_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(tests_file, 'r') as f:
        tests = json.load(f)['tests']

    with open(values_file, 'r') as f:
        values = {item['id']: item['value'] for item in json.load(f)['values']}

    fill_values(tests, values)

    with open(report_file, 'w') as f:
        json.dump({'tests': tests}, f, indent=2)
        print('Enjoy')
if __name__ == "__main__":
    main()
