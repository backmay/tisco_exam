def recursive_fucn(n):
    if n==1:
        return
    elif n%2==0:
        n=n/2
        print(n)
        recursive_fucn(n)
    elif n%2==1:
        n=n*3+1
        print(n)
        recursive_fucn(n)

recursive_fucn(5)