"""
#------------ >СПИСКИ<------------
a = [1,2,3,4,5]
b=["apple", "banana", "cherry"]

print (a[0], a[1], a[-1])
print (b[0], b[2])

print(a[1:4], a[::])
print(b[::2])

print(a[::-1])
print(b[::-1])



#------------ > МЕТОДИ СПИСКІВ<------------

a.append(6)
b.append('tomato')
print(a, b)

a.insert(3,7.4)
b.insert(3,'bottle')
print(a, b)

a.remove(7.4)
b.remove('bottle')
print(a, b)

a.pop(0)
b.pop(0)
print(a, b)

print(a.index(3), b.index("banana"))

a.extend([5,5,5])
b.extend(["cherry", "banana", "banana"])
print(a.count(5), b.count("banana"))

a.sort(reverse = True)
b.sort()
print(a,b)
a.reverse()
b.reverse()
print(a,b)



#------------ > Кортеж <------------
a = (1,2,3,4,5)

print(a[0], a[1], a[2])
print(a[:2], a[-2:])



#------------ > Методи_кортежів<------------
a = (1,2,3,4,5, 5, 5, 4)

print(a.count(5), a.count(4))
print(a.index(4))



#------------ > СЛОВНИКИ<------------
my_dict = { 'user':'John', 'age':21, 'country':'USA'}
print(my_dict['user'], my_dict['age'], my_dict.get('country'))
print(my_dict.get('number', 'key not found'))
my_dict['age'] = 30
print(my_dict.get('age'))

my_dict['animal'] = 'cat'
print(my_dict)

animal = my_dict.pop('animal')
print(my_dict)
"""


#------------ > МЕТОДИ СЛОВНИКІВ<------------

my_dict = { 'user':'John', 'age':21, 'country':'USA'}
copy_my_dict = my_dict.copy()
print(my_dict.clear())
print(copy_my_dict)

#items = РОЗПАКОВУЄ
for key,value in copy_my_dict.items():
    print(f"kEY: {key}, Value: {value}")

wrong_key = copy_my_dict.pop("currency", "key not found")
print(wrong_key)

my_dict_update = {"new_role": "admin", "salary": 100000}
copy_my_dict.update(my_dict_update)
print(copy_my_dict)