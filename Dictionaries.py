# Each key in dictionary must be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])  # throws an error if key does not exist
print(customer.get("name"))
print(customer.get("birthdate"))  # returns None if key does not exist
print(customer.get("birthdate", "Default value"))  # returns None if key does not exist

customer["name"] = "Jack Smith"  # update value of key
customer["birthdate"] = "Jan 1 1980"  # add new key-value pair
print(customer.get("name"))
print(customer.get("birthdate"))

print(customer)
