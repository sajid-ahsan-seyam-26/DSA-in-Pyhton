def solve():
    nums=list(map(int,input().split()))
    target=int(input())
    count=0
    for num in nums:
        if num==target:
            count=count+1
        print(count)
solve()