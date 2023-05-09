str = '1' + '9' * 100

while '19' in str or '299' in str or '3999' in str:
    # replace(<что ищем>, <чем заменяем>, <сколько раз>)
    # функция не изменяет строку, но возвращает изменённую
    str = str.replace('19', '2', 1)
    str = str.replace('299', '3', 1)
    str = str.replace('3999', '1', 1)
print(str)