my_dict={'Leon':75, 'Арина':7, 'Olya':62}
print(my_dict)
print(my_dict['Арина'])
my_dict['Piter']=29
print(my_dict['Piter'])
my_dict.update({'Anton':42, 'Vika':6})
del my_dict[('Olya')]
print(my_dict.get('Olya'))
print(my_dict)
my_set={38, (12, 41.2), 26.4, 38, 'seemen', (12, 41.2)}
print(my_set)
my_set.update([13, 6, 13])
my_set.discard(3)
print(my_set)