#this is similar to the way you do list comprehension

#its a method of quickly creating a dict through another dict and it gives you the flexibility of transforming and filtering the values before mapping
peoplesAges = {
    "Taiwo": 32,
    "Glory": 20,
    "John": 65,
    "Jamie": 15,
    "Hanah": 18,
}

usersAgeX2 = {user:age*2 for user,age in peoplesAges.items()}

olderUsers = {user:age for user,age in peoplesAges.items() if age > 21} #with condition to filter

print(f"Users: {peoplesAges}")
print(f"ages x2: {usersAgeX2}")
print(f"Older users: {olderUsers}")