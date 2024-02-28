import sys

def min_moves(filename):
    with open(filename, 'r') as f:
        nums = list(map(int, f.read().split()))

    nums.sort()
    median = nums[len(nums) // 2]

    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Использовать:\n"
              ">> cd C:\YourWay\\task4\n"
              ">> python task4.py nums.txt")
        return

    print(min_moves(sys.argv[1]))

if __name__ == "__main__":
    main()