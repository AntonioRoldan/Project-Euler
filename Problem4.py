def isPalindrome(S):
    S = list(S)
    limit = len(S)//2
    counter = 0
    x = 0
    y = len(S) - 1
    while counter < limit:
        if S[x] != S[y]:
            return False
        counter += 1
        S[x] = S[y]
        x += 1
        y -= 1

    return True

def main():
    lst = [n for n in range(1000) if len(str(n)) == 3]
    results = []
    factor = 0
    for n in lst:
        if n == 100:
            for i in range(len(lst)):
                results.append(n * (n + factor))
                factor += 1
        else:
            factor = 0
            t = n - 100
            for i in range(len(lst)):
                if t >= 0:
                    results.append(n * (n - t))
                    t -= 1
                else:
                    results.append(n * n + factor)
                    factor += 1

    print(max([n for n in results if isPalindrome(str(n))]))

main()
