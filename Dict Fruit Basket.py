

fruitBasket = {
    "apple": 5,
    "banana": 3,
    "orange": 2,
    "kiwi": 4,
    "grape": 10
}

print(fruitBasket)

fruitBasket["apple"] = 10
print(fruitBasket)

fruitBasket["pear"] = 7
print(fruitBasket)

del fruitBasket["banana"]
print(fruitBasket)


print(fruitBasket["kiwi"])  # Output: 4
print(fruitBasket.get("kiwi"))  # Output: 4
print(fruitBasket.get("banana"))  # Output: None
print(fruitBasket.get("banana", 0))  # Output: 0