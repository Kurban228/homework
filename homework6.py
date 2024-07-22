my_dict = {'Vladimir': 1983, 'Dmitry': 2000, 'Nadin': 1987}
print("Dict:", my_dict)
print("Existing value:", my_dict.get('Nadin'))
print("Not existing value:", my_dict.get('Ivan'))
my_dict.update({'Maxim': 2006, 'Artem': 1989})
deleted_value = my_dict.pop('Dmitry')
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)
my_set = {1, 'Яблоко', 42.314, (5, 6, 1.6)}
print("\nSet:", my_set)
my_set.update({13, (5, 6, 1.6)})
my_set.remove('Яблоко')
print("Modified set:", my_set)