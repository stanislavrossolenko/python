numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)
print((sum(numbers)) - min(numbers))
