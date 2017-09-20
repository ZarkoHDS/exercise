def fibonaccil(n):
    if n == 1 or n == 2:
        return 1
    return fibonaccil(n-1) + fibonaccil(n-2)
for i in range(1,10):
    print(fibonaccil(i))
