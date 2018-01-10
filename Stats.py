def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*fact(x-1)

def nPr(n, r):
    return fact(n) / fact(n-r)

def nCr(n, r):
    return nPr(n, r) / fact(r)

if __name__ == '__main__':
    print nCr(3, 2)