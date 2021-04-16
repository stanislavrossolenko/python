time = int(input('Введите любое число:'))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f'Время в формате чч:мм:сс {hours} : {minutes} : {seconds}')

