import math

def calculate_point_position(circle_file, points_file):
    try: 
        with open(circle_file, 'r') as f:
            x_center, y_center = map(float, f.readline().split())
            if not (abs(x_center) <= 10**38 and abs(y_center) <= 10**38): #Проверка на 10^-38 излишняя
                print("Координаты центра окружности должны быть в диапазоне от -10^38 до 10^38.")
                return
            radius = float(f.readline())

        with open(points_file, 'r') as f:
            points = []
            for i, line in enumerate(f):
                if i >= 100:  # Остановить чтение после 100 строк
                    break
                x, y = map(float, line.split())
                if not (abs(x) <= 10**38 and abs(y) <= 10**38): #Проверка на 10^-38 излишняя
                    print(f"Координаты точки {i+1} должны быть в диапазоне от -10^38 до 10^38.")
                    return
                points.append([x, y])
            
        """
        Тут самое "веселое".
        Для вычисления расстояния между двумя точками на плоскости нужно использовать формулу расстояния 
        между двумя точками в двумерном пространстве: √((x2-x1)^2 + (y2-y1)^2), где (x1, y1) и (x2, y2) — координаты двух точек
        Источник: https://uchet-jkh.ru/i/kak-naiti-rasstoyanie-mezdu-2-tockami

        Я в геометрии не силён, и  чтобы понять что именно эта формула мне нужна потратил больше времени, 
        чем на всё написание обоих тасков и обеих вариациях вместе взятых. Но это было интересное приключение.
        """
        for point in points:
            distance = math.sqrt((point[0] - x_center)**2 + (point[1] - y_center)**2)
            if distance < radius:
                print(1)
            elif distance == radius:
                print(0)
            else:
                print(2)
    except Exception as ex:
        print(f'Error {ex}')
        main()

def enter_the_path_circle():
    circle_file = input('Введите полный путь до файла с координатами и радиусом окружности, включая сам файл и его расширение.\n'
          'Пример: C:\GitHubRepo\LoadTesting\\task2\circle.txt\n\n')
    return circle_file

def enter_the_path_points():
    points_file = input('Введите полный путь до файла с координатами точек, включая сам файл и его расширение.\n'
          'Пример: C:\GitHubRepo\LoadTesting\\task2\points.txt\n\n')
    return points_file

def main():
    circle_file = enter_the_path_circle()
    points_file = enter_the_path_points()
    calculate_point_position(circle_file, points_file)

if __name__ == "__main__":
    main()