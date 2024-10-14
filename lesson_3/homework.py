#Task_1
user_1= {
    "password": "password123"
}

u_login = input("Please enter your login:")
u_password = input("Please enter your password:")

if u_password == user_1["password"]:
    print("Success!")
else:
        print('Incorect password')


#Task_2
 
days = {
       "1":"Monday",
       "2":"Tuesday",
       "3":"Wednesday",
       "4":"Thursday",
       "5":"Friday",
       "6":"Saturday",
       "7":"Sunday"
    }
u=input("Enter number from 1 to 7:  ")

if u in days :
      print(days[u])
else:
      print ("There is no such day of the week!")


#Task_3
user_number = int(input("Введіть число: "))

for i in range(1, 11):
    result = user_number * i
    print(f"{user_number} x {i} = {result}")


#task_4

list_number = [1, 2, 3, 4, 5, 6, 7, 8]
total_sum = 0
for i in list_number:
    total_sum += i
print(total_sum)


#Task_5

print ("Input a number")
factorialIP = int (input ())
ffactor23 = 1
for j in range (1, factorialIP+1):
   ffactor23 = ffactor23 * j
print ( ffactor23)


#Task_6

for i in range(1,51):
   if i%2 == 0:
    print( i )


#Task_7
for i in range(1,51):
   if i%2 != 0:
    print( i )
