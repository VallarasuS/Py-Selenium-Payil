# data = {"fname": "John", "lname": "Smith"}

# print(data)
# print(type(data))

# # get vs set - update

# data.update({"fname": "Adam"})
# data.update({"age": 30})
# data.update({"employed": False})
# data.update({"address": ["12", "First Street", "Chennai", "TN"]})

# print(data)

# # Primary Use Case
# name = data.get("fname")
# print(name)

# name = "Adam"
# data.update({"fname": name})

# print(data)

# for i in data.keys():
#     print(i)

# for i in data.values():
#     print(i)

# for k, v in data.items():
#     print(k)
#     print(v)


# #
# city = data.get("City")
# print(city)

# # Membership check
# if "City" in data:
#     print("City key is present")
# else:
#     print("City key is NOT present")


# # List
# # process all data in order

# # Dictionary / Map / Hashmap
# # Search / Look up specific value/key

# # Short form
# data.update({"fname": "Dave"})
# data["fname"] = "Dave"

# name = data.get("fname")
# name = data["fname"]

# # del data["fname"]
# print(data)

# print(name)

# # Throws Error when key is not present
# # name = data["City"]

users = [
    ("John", "john@gmail.com", 123),
    ("Dave", "Dave@gmail.com", 123),
    ("Mike", "Mike@gmail.com", 123),
    ("John", "JohnA@gmail.com", 123),
]

email_dict = {}
for user in users:
    name, email, phone = user
    email_dict.update({email: user})
    # user_map[email] = name

print(email_dict)
name = email_dict.get("JohnA@gmail.com")
print(name)

phone_book = ("John", "09234", "email", "address")

expected = {"one": 1, "two": 2}
actual = {"one": 10, "two": 20}

if len(expected) != len(actual):
    print("Failed")

for key in expected.keys():  # one, two
    ex = expected.get(key)  # 1
    ac = actual.get(key)  # 10

    if ac == ex:
        print("success")
    else:
        print("Failure")

# 1 -> "Mondays"
# 7 -> "Sunday"

days = {1: "Monday", 7: "Sunday"}
reverse = {"Monday": 1, "Sunday": 7}

print(days.get(1))
print(reverse.get("Monday"))

# redis
# mongodb
# key - values
