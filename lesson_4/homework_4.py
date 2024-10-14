#------------ > СПИСКИ <------------
#1
list_numbers = [10,20]
list_numbers.remove(10)
print(list_numbers)
#2
sum_numbers = [1,2,3,4,5,6,7,8,9]
print(sum(sum_numbers))

numbers = [1,2,3,4,5,6,7,8,9]
duble_number = 0

#3
for i in numbers:
    duble_number = i*2
    print(duble_number)

#------------ > КОРТЕЖІ <------------
#1
fruits  = ('apple','banana','orange')
print(fruits[0],)
print(fruits[1])
print(fruits[2])

#2
numbers_1 = (1, 2, 3, 4, 5)
numbers_2 = (6, 7, 8, 9, 10)
new = numbers_1 + numbers_2
print(new)

#------------ > СЛОВНИКИ <------------
#1
personal_dict = {'name': 'Novak', 'age': 37, 'sport':'tennis'}

for k, v in personal_dict.items():
    print(f"Key: {k}, Value: {v}")

#2
books = {'The Hobbit': 1937, "The Little Prince": 1950}
new_books = {'The Vilagges': 2015}
books.update(new_books)
print(books)

#3
countries = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Poland':'Warsaw'}

name_c = input('Enter country : ')

if name_c in countries:
        print(f"The capital of {name_c} is {countries[name_c]}.")
else:
        print("Country not found. Try something else.")






