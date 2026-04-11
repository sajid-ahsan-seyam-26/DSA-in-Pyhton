def solve():
    nums=list(map(int,input().split()))
    result=[]
    i=len(nums)-1
    while i>=0:
        i=i-1
        result.append(nums[[i]])
        print(result)
solve()