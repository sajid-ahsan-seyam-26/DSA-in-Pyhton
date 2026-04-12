def solve():
    nums=list(map(int,input().split()))
    largest=nums[0]
    smallest=nums[0]

    for num in nums:
        if num>largest:
            largest=num
        elif num<smallest:
            smallest=num
            print(largest-smallest)
solve()

    