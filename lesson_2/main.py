#1
String = 'name'
Integer = 19
Float = 12.56
List = [1, 2, 3, 4, 5, 6, 7, 8, 19]
Dict = {'name':'Nadia', 'age': 19}
Tuple = (1,2,3,5)
n = None

#2
a = String == 'name'
b = Integer != 19
c = Integer > Float and Integer in List
d= String in Dict
print(a,b,c,d)

m = 27
s = 14
o= m//s
print(o)
o = m%s
print(o)

#3
#3.1
num_str = 125
num_str = str(num_str)
print(type(num_str))

#3.2
message = 'Hi, my name is Python!'
message = message.replace('y', '0')
print(message)
message = message.replace('i','1')
print(message)

#3.3
split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)
string_join = " ".join(split_test)
print(string_join)

#3.4
print(len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
listt = (7, 8, 9)
list_extend.extend(listt)
print(list_extend)

print(list_extend.index(6))
print(len(list_append))

#dictionary
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
print(dict_test['car'])
print(dict_test['where'])

print(dict_test.keys())
print(dict_test.values())

print(dict_test.items())
