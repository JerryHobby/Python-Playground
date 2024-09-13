

# - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.

# - Use a set if you need uniqueness for the elements. 

# - Use tuples when your data cannot/should not change.

# mutable, sortable
myList = ["one", 2, 3.0]

# immutable, sortable
myTuple = ("one", 2, 3.0)

# mutable, unsortable, no duplicates
mySet = {"one", 2, 3.0}

# mutable
myDict = {
  "brand": "Audi",
  "model": "Q5",
}


myList.insert(4,2)
mySet.add(4)

print("myList", myList)
print("myTuple", myTuple)
print("mySet", mySet)




# lambdas

def mult(n):
  return lambda a : a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5))



def tax_rate(rate):
  return lambda a: round(a + (a * rate), 2)

state_tax = tax_rate(0.085)
city_tax = tax_rate(0.025)

price = 100

print(state_tax(price))
print(city_tax(price))



#List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]

# Function to capitalize each name
def capitalize(name):
  return name.capitalize()

# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)




numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))

print(doubled)




products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)




#**kwargs is a dictionary
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)

display_info(name="Alice", age=30, city="New York")






def greet():
    return "Welcome!"

#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())




def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

# Using the decorated function
print(greet())




def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper

@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))