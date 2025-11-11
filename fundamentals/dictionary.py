dictVar = {
    "id": 111,
    "name": "Adebayo",
    "age": 34,
    "height": "2m",
    "scores": [65,75,70,84]
}

secondDictVar = {#this is also possible. Using immutable values as keys
    123: 111,
    "name": "Adebayo",
    True: 34,
}

thirdDict = dict(name = "Robinson") #another way of creating dictionaries. This returns {"name":"Robinson"}

#GETTING VALUE 
print(dictVar["name"]) #returns the value of the key.
print(dictVar.get("name")) #same function as the above but safer. returns the value with the key. If the key doesn't exist, it just returns None
print(dictVar.get("brother", "Jubril")) #same function as the above but if the key doesn't exist, it will return the given value in the second param
print(dictVar.items()) #returns a list of the items of the dict and the key value pairs are stored as elements of tuples

print("name" in dictVar) #returns TRUE because the key exist in the dict
print("name" in dictVar.keys()) #same as above
print("Adebayo" in dictVar.values()) #returns TRUE because the value exist in the dict

# #SETTING OR REPLACING VALUE 
dictVar["id"] = 344
print(dictVar["id"])
dictVar.update({"age" : 29, "car": "ROver"})#extends the new dictionary into the existing dictionary, if a key already exists in the old dict, then it just replaces its value
print(dictVar)

#REMOVING ITEM
item = dictVar.pop("ages") #deletes an item with the key and return the value
item = dictVar.popitem() #deletes any item and return the key-value pair in a tuple (NB!! this doesn't delete in an order, meaning it can delete any item)
dictVar.clear() #clears the whole dict and makes it empty {}

#OTHER METHODS
fourthDict = secondDictVar.copy() #copies the items of a dict into another
