'''18.Which values of Ackermann’s function are small enough 
that you are able to compute them?'''

m=int(input("Enter value for m: "))
n=int(input("Enter value for n: "))
def f(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return f(m - 1, 1)
    else:
        return f(m - 1, f(m, n - 1))

result = f(m, n)
print(result)
