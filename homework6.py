my_dict = {'Иван': 2001, 'Юля': 1998, 'Егор': 2004}
print(my_dict)
print(my_dict.get('Иван'))
print(my_dict.get('Антон'))
my_dict.update({'Антон': 1987, 'Анна': 2005})
a = my_dict.pop('Антон')
print(a)
print(my_dict)
my_set = {1, 2, 3, 3, 3, 'Апельсин', 3.14, 4, 5, 1, 1, 1, 2}
print(my_set)
my_set.update([7, 'Apple'])
my_set.discard(1)
print(my_set)
