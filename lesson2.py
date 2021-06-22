'''
print(bin(4))
#a + ib  i^2 = -1
k = complex(1,4)
print(k)
l = 2 +3l
print(l)
print(k + l)
print(k - l)
print(k ** l)
'''
'''
s1 = 'Hello world! How are you?'
s2 = ' world'
s3 = '*'
print(s1 + s2)
print(s3 * 30)
print(s1[1])    # элемент в строке
print(s1[0:5])   # лово + 1 элемент после
print(s1[0:5:2]) # шаг чере 2
print(s1[5:-2])  # c 5 до конца только наоборот
print(s1[::-1])  # в обратном порядке
print(len(s1))  # длина строки выводит

s1 = 'q a l     1'   # функция сплит разделяет строку
print(s1.split())
print(s1.split(' '))  # включаются пробелы или звездочки '*' вместо пробела
print(' '.join([s1, '4567', 'sdf']))  #через что соединить
s3 = 'Hello'
print(s3.title())  # делает первую букву заглавной
# upper в верхнем регистре
# lower в нижнем регистре
# is перед ними TRUE or FALSE для проверки
s4 = 'sdggfshsh 466 ghfg'
print(s4.count('dg')) # сколько раз повторяется dg
print(s4.replace('46', '523'))  # аменить значение в строке
print(s4.index('h'))  # индекс вхождения в строку
print(s4.index('h', 4))  # с какой строки начинать
print(s4.find('h', 4, 9))  # что ищу и с какого элемента

print(chr(65))  # найти по номеру кода
print(ord(A))   # наоборот
'''
'''
# СПИСКИ
s3 = 'dgsg'
l = [3, 6, 'dfggh', [3, 6]]
print(list(s3))   # разбить строку на элементы
print(l[0])   # посмотреть на 1 элемент
l[0] = 78    # (список изменяемый)
print(l[0])
print(l[1:4])   # срез списка
print(l[3][0])  # номер элемента (двумерный спеисок) и номер в другом списке
print(l + [4, 7] + [325])  # сложение списков
print(l * 3)

l.append('haha')   # добавляет только 1 элемент и только в самый конец
print(l)
l.extend([4, 8, '34234'])  #добавялет нескольк списков в конец
print(l)
l.insert(3, 'zzz')   # на какое место и что поставить
print(l)
l.index(6)  # индекс вхождения(на каком месте элемент и только первое вхождение)
print(l)
l.append('3')
print(l.count(4)) # количество элементов в строке
print(l)
l.remove('zzz')  # удаление элемента(по названию)
print(l)
l.pop(2)  # удаление по индексу, если не задавать то удаление последнего элемента
print(l)
   #   l.sort()   # отсортировать список (только одинаковые данные сравенение между собой число с числом и тд
l2 = [3, 7, 12, 5]
l2.sort()
print(l2)
l2.sort(reverse = True)  # в обратном порядке
l2.clear()   #очистка списка
l5 = l2.copy()  #копирование
# if '3' in l:  # есть ли элемент в списке
print(78 or 4 in l)  # тоже поиск элементов
'''
'''
# Кортеж
s = tuple('yuy')   # кортеж
print(s)
s2 = (2, 'f343')
print(s2)
print(s2[1])   # индекс
s3 = (2, 'f343', [1, 5, 7])
s3[2].remove(1)
print(s3)  #замена элемента в кортеже
print(s3.count(2))  # найти количесво элементов
'''
'''
# Множества
s = 'hello world'
print(set(s))    # множество(удаляет повторяющиеся элементы)

d = {2, 4, 5, 'dgsdg', (3, 5)}
print(d)
d.add(67)  #добавление элемента
print(d)
d.add(2)  # nfrjq ;t 'ktvtyn yt lj,fdbn
print(d)
d.remove(2)  #удаление элемента
print(d)
d.pop()   # удаление 1-го элемента (в списках последний)
print(d)
d.discard(4)  # удаление по значению (не выдает ошибки если нет элемента,в отличии от remove)
print(d)
d2 = d.copy()  #копирование
d.clear()   # очистить
print(d)
print(frozenset(s))  # неизменяемый тип данных (со множествами можно делать арифметические операции)
'''
# Cловарь
'''
d = dict(kate = 89853034433, bob = 563234)  #создание
print(d)
m = {"Kate" : 2411, "Bob" : 2141}  #тоже создание
print(m)
print(m['Kate'])   #поиск ключа
m['Kate'] = 1111   # заменить значение
print(m)
m['Nick'] = 3235  #добавить элемент
print(m)
print(m.keys())  # все ключи
print(m.values())   # все значения
print(m.items())  # список из кортеж(ключ и значение)
print(m.pop('Bob'))  # удаляется значение, но значение к ключу принадлежит(только значение возвращает
print(m)
print(m.popitem())  #удаояется последний элемент , целиком кортеж и возвращает его(целиком возвращает
d = dict(kate = 89853034433, bob = 563234)
n = dict(Ane = 89853033, Koko = 56323434)
n.update(d)  # соединение двух словаерей
print(n)
'''
'''
# Цикл for
l = [2, 4, 6, 8]
print(l)
for i in l:  #первый раз переменная не ошибка i = 2 возврат цикла по списку
    print(i)
d = dict(kate = 89853034433, bob = 563234)
n = dict(Ane = 89853033, Koko = 56323434)
n.update(d)  # соединение двух словаерей
for key, value in n.items():
    print(key, value)
for i, j in enumerate(l, 100):  # отдельно идексы,отдельно значения
    print(i, j)

l2 = l * 10
print(l2)
for i in range(0, 12):
    print(i)
'''
# Тернарный оператор

#num = input()
#print(True if num.isdigit() else False)  #проверка числа

#l1 = [3, 5]
#l2 = [3, 5]
#if l1 == l2:
   # print('ok')
  # print(l1 is l2)
#num = input()
#print(True if num.isdigit() and int(num) > 10 else False)

l1 = [3, 5]
l2 = [3, 5]
print(l1 is l2)

l3 = l1
print(l1 is l3)  # ссылаются на один и тотже объект

if l1 == l2:
    print('ok')