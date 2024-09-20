items = ["apples", "bananas", "milk", "bread"]
print("Shopping list:", end=" ")

for i, item in enumerate(items):
    if i == len(items) - 1:
        print(item, end=".\n")
    else:
        print(item, end=", ")