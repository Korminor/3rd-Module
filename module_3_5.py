def get_multiplied_digits(number):
    number = int(number) # убираем нули в начале
    str_number = str(number) # '40203'
    str_number = str_number.replace('0','')
    first = int(str_number[0])  # 4
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(40203)

print(result)