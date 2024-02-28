def min_moves(filename):
    with open(filename, 'r') as f:
        nums = list(map(int, f.read().split()))

    nums.sort()
    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)

def path_to_file():
    filename = input('Введите полный путь до файла, включая сам файл и его расширение.\n'
          'Пример: C:\YourWay\\task4\\nums.txt\n\n')
    return filename

def main():
    filename = path_to_file()
    print(min_moves(filename))

if __name__ == "__main__":
    main()