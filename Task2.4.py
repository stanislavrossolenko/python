a = input('Введите слова через пробел:')
b = []
num = 1
for i in range(a.count(' ') + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {num} {b[i]}")
        num += 1
    else:
        print(f" {num} {b[i][0:10]}")
        num += 1
    print(a[0])
