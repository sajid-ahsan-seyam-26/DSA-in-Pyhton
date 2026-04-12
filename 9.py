def solve():
    nums=list(map(int,input().split()))
    first = -10**18
    second = -10**18
    for num in nums:
        if num>first:
            second=first
        elif num>second and num !=first:
            second=num
            print(second)
solve()

