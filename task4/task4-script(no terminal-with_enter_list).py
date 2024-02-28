def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)

def enter_len_list():
    try:
        len_list = int(input('Введите количество элементов в списке:\n'))
        return len_list
    except ValueError:
        print('Нужно числовое значение!')
        enter_len_list()

def add_items_in_list(len_list):
    nums = []
    for i in range(len_list):
        try:
            item = int(input(f'Введите значение #{i + 1}/{len_list}\n'))
            nums.append(item)
        except ValueError:
            print('Нужно числовое значение!')
    return nums

def main():
    len_list = enter_len_list()
    nums = add_items_in_list(len_list)
    print('Итог:', min_moves(nums))

if __name__ == "__main__":
    main()