def person_info(name, surname, birthday, city, email, phone):
    result = f'{name}, {surname}, дата рождения {birthday}, проживает в городе {city}, контактные данные {email}, {phone}'
    return result
print(person_info('Станислав', 'Россоленко', 11.07, 'Москва', 'rossolenkos@mail.ru', 89853034433))