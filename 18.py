def solve():
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))

    result=[]
    for nums in num1:
        result.append(nums)
    for nums in num2:
        result.append(nums)
        print(result)
solve()