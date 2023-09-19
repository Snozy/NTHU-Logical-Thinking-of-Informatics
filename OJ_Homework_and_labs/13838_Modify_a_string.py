def reverse(string):
    string = string[::-1]
    return string

x = input()
if len(x) % 2 != 0:
    i = 0
    while i < len(x):
        if x[i].isalpha():
            temp = x[i].upper()
            x = x[:i] + temp + x[i+1:]
            break
        i += 1
    else:
        exit()

    x = reverse(x)
    print(x)
else:
    middle = len(x) // 2
    x = x[:middle - 1] + "4" + x[middle:]
    x = x[:middle] + "2" + x[middle + 1:]
    print(x)
