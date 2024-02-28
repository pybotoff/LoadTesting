def circular_array_path(n, m):
    try:
        array = list(range(1, n + 1))
        #print(array)
        path = []
        index = 0

        while len(path) < n:  # Продолжаем, пока не пройдем все элементы
            path.append(array[index])  # Добавляем начальный элемент интервала в путь
            if len(path) < n:  # Проверяем, не достигли ли мы конца пути
                index = (index + m - 1) % n  

        return ''.join(map(str, path))  
    except Exception as ex:
        print(f'Error: {ex}')






def enter_n():
    while True:
        try:
            n = int(input('Введите длину массива:\n'))
            return n
        except ValueError:
            print('Ошибка. Значение должно быть числовым.')

def enter_m():
    while True:
        try:
            m = int(input('Введите интервал хода:\n'))
            return m
        except ValueError:
            print('Ошибка. Значение должно быть числовым.')



def main():
    n = enter_n()
    m = enter_m()
    print(circular_array_path(n, m))
    main()

if __name__ == "__main__":
    main()
