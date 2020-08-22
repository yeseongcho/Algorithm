def f(n, memo={}) :
    if n == 1 :
        a = 1; b =1
        return a, b
    if n in memo : return memo[n]

    if (n%2) == 0 :
        a = f(n-1)[0]
        b = f(n-1)[0] + f(n-1)[1]
    else  :
        a = f(n-1)[0] + f(n-1)[1]
        b = f(n-1)[1]    
    memo[n] = a, b
    return a, b

n = int(input())
a, b = f(n)
print(2*(a+b))

