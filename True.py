def in_even(n):
    return n % 2 == 0

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(numbers)

for i in numbers:
    print(in_even(i))


