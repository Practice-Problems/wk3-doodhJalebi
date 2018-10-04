def extraLongFactorials(n):
    result = n
    while(n>1):
        result = result * (n-1)
        n = n - 1
    print(result)
extraLongFactorials(int(input()))