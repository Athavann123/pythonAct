customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer.get("birth", "Jan 1 1980"))
print(customer["name"])