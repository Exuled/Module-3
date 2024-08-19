def print_params(a = 1, b = 'строка', c = True):
    print(f"a: {a}, b: {b}, c: {c}")

print_params()
print_params(10)
print_params(10, 'test')
print_params(10, 'test', False)


print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['строка', 10, True]
values_dict = {'a': 'строка', 'b': 10, 'c': True}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)