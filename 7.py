def solve():
    nums=list(map(int,input().split()))
    result=[]
    i=0
    while i<len(nums):
        result.append(nums[i])
        i=i+2
        print(result)
solve()