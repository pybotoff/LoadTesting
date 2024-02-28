import sys

def circular_array_path(n, m):
    try:
        array = list(range(1, n + 1))
        path = []
        index = 0

        while len(path) < n:  
            path.append(array[index])  
            if len(path) < n:  
                index = (index + m - 1) % n  

        return ''.join(map(str, path))  
    except Exception as ex:
        print(f'Error: {ex}')

def main():
    if len(sys.argv) != 3:
        print("Использовать:\n"
              ">> cd C:\YourWay\\task1\n"
              ">> python task1.py n m")
        return

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print(circular_array_path(n, m))

if __name__ == "__main__":
    main()
