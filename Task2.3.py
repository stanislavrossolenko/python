a = ['Winter', 'Summer', 'Spring', 'Fall']
c = {1 : 'Winter', 2 : 'Summer', 3 : 'Spring', 4 : 'Fall'}
b = int(input('Введите номер месяца: '))
if b == 12 or b <= 2:
    print(c.get(1))
    print(a[0])
elif b <= 5 and b > 2:
    print(c.get(3))
    print(a[2])
elif b <= 8 and b > 5:
    print(c.get(2))
    print(a[1])
elif b <= 11 and b > 7:
    print(c.get(4))
    print(a[3])
else:
    print('Такого месяца нет')