def solve():
    nums=list(int,input().split())
    count=0
    for num in nums:
        if num <0:
            count=count+1
            print(count)
solve()