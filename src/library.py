def Fibonachi(n):
    n:int
    a = [1,1]
    for i in range(2, n):
        a.append(a[i-2]+a[i-1])
    return a

def Puzirek(a):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if (a[j] > a[i]):
                b = a[j]
                a[j] = a[i]
                a[i] = b
    return a

def Deistvie(a, symb, b):
    if (symb == "+"):
        return a + b
    elif (symb == "-"):
        return a - b
    elif (symb == "*"):
        return a * b
    elif (symb == "/"):
        return a / b
    else:
        return 0