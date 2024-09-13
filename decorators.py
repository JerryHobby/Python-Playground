def decor(func):
    def wrapper(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrapper

@decor
def invoice(num):
    print("INVOICE #" + num)

invoice(input());