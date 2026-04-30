def f_bk(a, b, c, k, f1):
    # f1 means f(1)
    if a == 1:
        return f1 + c * k
    else:
        return (a ** k) * f1 + c * ((a ** k - 1) // (a - 1))


''' Given a recurrence relation of the form f (n) = af (n/b) + c, 
where a is a real number, b is a positive integer, and c is a real number, 
and a positive integer k, find f (bk ) using iteration. '''


a = float(input("a: "))
b = int(input("Enter value for b: "))
c = float(input("Enter value for c: "))
k = int(input("Enter value for k: "))
f1 = int(input("Enter value for f1: "))

result = f_bk(a, b, c, k, f1)
print(result)
