


while True:
    str = input('Enter a string: ')
    if str is None:
        print('Invalid input. Please enter a non-empty string.')
        continue
    if str == 'exit':
        exit()
    str_list = list(str)
    result = None
    for char in str_list:
        result = result + ord(char)
    print(f'Sum of ASCII values: {result}')