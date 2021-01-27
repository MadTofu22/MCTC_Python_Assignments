def fib(n):
    initialTerms = [1,1,2,3,5]
    nextTerm = initialTerms[-1] + initialTerms[-2]

    if n == len(initialTerms):
        return initialTerms[n-1]
    else:
        initialTerms.append(nextTerm)
        fib(n)
