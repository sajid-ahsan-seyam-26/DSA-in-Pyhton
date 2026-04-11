def solve():
    nums=list(map(int,input().split()))
    count=0
    for num in nums:
        if nums%2==0:
            count=count+1
            print(count)
solve()