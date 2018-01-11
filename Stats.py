#full factorial
def fact(x):
    if x < 2:
        return 1
    else:
        return x*fact(x-1)

#factorial that stops at a certain number
def fact_break(x, y):
    if y > abs(x):
        raise Exception('incorrect arguments')
    elif x == y:
        return 1
    else:
        return x*fact_break(x-1, y)

#permutations
def nPr(n, r):
    return fact_break(n, n-r)

#combinations
def nCr(n, r):
    if r > n-r:
        r = n-r
    return nPr(n, r) / fact(r)


if __name__ == '__main__':
    print nCr(3, 1)