"""user_1 = {
    "name": "Tom",
    "age": 32,
    "balance":50000,
    "currency": "USD",
    "status": True
}

user_2 = {
    "name": "Frenk",
    "age": 56,
    "balance":2000,
    "currency": "EUR",
    "status": False
}
user_3 = {
    
    "age": 16,
    "balance":110000,
    "currency": "UAH",
    "status": True
}

list_of_currency = ["USD", "GBR", "UAH", "EUR"]

if user_1["name"] and user_1["age"] >= 18 and user_1["status"]:
    if user_1["balance"] >=10000 and user_1["currency"] in list_of_currency:
        print(f"Hello! You can create your binance account, welcome {user_1['name']}!")
    elif user_1["balance"] >=1000 and user_1["currency"] in list_of_currency:
        print("You need more money!")
    else:
        print("Sorry, money is not enough")
elif not user_1["name"]:
    print("Please, enter your name")
elif user_1["age"]<18 :
    print("You need 18 years old for registration")
else:
    print("Something went wrong")


if user_2["name"] and user_2["age"] >= 18 and user_2["status"]:
    if user_2["balance"] >=10000 and user_2["currency"] in list_of_currency:
        print(f"Hello! You can create your binance account, welcome {user_2['name']}!")
    elif user_2["balance"] >=1000 and user_2["currency"] in list_of_currency:
        print("You need more money!")
    else:
        print("Sorry, money is not enough")
elif not user_2["name"]:
    print("Please, enter your name")
elif user_2["age"]<18 :
    print("You need 18 years old for registration")
else:
    print("Something went wrong")


if user_3.get("name", None) and user_3["age"] >= 18 and user_3["status"]:
    if user_3["balance"] >=10000 and user_3["currency"] in list_of_currency:
        print(f"Hello! You can create your binance account, welcome {user_3['name']}!")
    elif user_3["balance"] >=1000 and user_3["currency"] in list_of_currency:
        print("You need more money!")
    else:
        print("Sorry, money is not enough")
elif not user_3.get("name", None ):
    print("Please, enter your name")
elif user_3["age"]<18 :
    print("You  need 18 years old for registration")
else:
    print("Something went wrong")
"""
                  

"""
test_list = ["test","python","code"]
for s in test_list:
    if s =="test":
        print(s)
    elif s =="python":  
        print(s)
    else:
        print(s)
"""
"""
a=0
add_list = []

while len(add_list)<100:
    print(f"len of list , {len(add_list)}")
    add_list.append(a)
    a +=1
    if len(add_list) == 50:
        print('You are at middle of list')
"""



user_1 = {
    "user_name": "tester",
    "role": "admin",
    "account_connection": True
}
user_2 = {
    "user_name": "junior",
    "role": "user",
    "account_connection": False
}
user_3 = {
    "user_name": "middle",
    "role": "pro_user",
    "account_connection": True
}

list_of_users =[user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with {user['user_name']} account -------<<<<")
    if not user['account_connection']:
        count_of_tries = 10
        while count_of_tries != 0:
            print ("Try to connect to user account")
            count_of_tries -= 1
            if count_of_tries == 5:
                print("Middle of tries")
                continue
            print("Count of tries left: ", count_of_tries)
    elif user['role'] == 'admin':
        print(f"Hello in system {user['user_name']}")
    else:
        print("Welcome on the board")

print("all users were checked")













