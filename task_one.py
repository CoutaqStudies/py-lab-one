def convert_into_currency(num):
    if num < 0:
        raise ValueError('Некорректный формат!')
    dec = num % 1
    number = int((num - dec))
    dec = int(dec * 100)
    print(f'{number} руб. {dec} коп.')


convert_into_currency(12.5)
