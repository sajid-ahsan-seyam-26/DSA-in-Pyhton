def solve():
    nums=list(map(int,input().split()))
    target=int(input())
    answer=-1
    for i in range(len(nums)):
        if nums[i]==target:
            answer=i
            break
        print(answer)
solve()