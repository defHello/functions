def all_even(*nums):
    for i in nums:
        if i % 2 != 0:
            return False
    return True
print(f'Введите значения для проверки: Четности')
a, b, c = int(input()), int(input()), int(input())
print(all_even(a, b, c))