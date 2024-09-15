def convert(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return convert(num // 2) + str(num % 2)

print(convert(int(input())))