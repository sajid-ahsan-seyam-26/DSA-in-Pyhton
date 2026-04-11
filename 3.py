def solve():
    arr=list(map(int,input().split()))
    larget=arr[0]
    for num in arr:
        if num<larget:
            larget=num
            print(num)
solve()
    