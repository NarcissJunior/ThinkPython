def printplus():
    print("+", end=' ')

def printdash():
    print("-", end=' ')

def printl():
    print("|", end=' ')

def printspace():
    print(" ", end=' ')

def printline():
    printmultiplier(printdash, 4)

def printheader():
    for x in range(5):
        if (x % 2):
            printline()
        else:
            printplus()
    print("")

def printmiddle():
    for x in range(5):
        if (x % 2):
            printmultiplier(printspace, 4)
        else:
            printl()
    print("")

def printmultiplier(func, times):
    for x in range(times):
        func()

def printalternator(func_one, func_two, times):
    for x in range(times):
        if (x % 2):
            func_one()
        else:
            func_two()

def print_square():
    for x in range(5):
        if (x % 2):
            printmultiplier(printmiddle, 4)
        else:
            printheader()

print_square()