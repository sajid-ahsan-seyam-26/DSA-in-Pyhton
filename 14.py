def solve():
    nums=list(map(int,input().split()))
    result=[]
    zero_count=0
    for num in nums:
        if num==0:
            zerro_count=zero_count+1
        else:
            result.appened(nums)
            for i in range(zero_count):
                result.append(0)
                print(result)
solve()