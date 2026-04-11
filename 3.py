def solve():
    num=list(map(int,input().split()))
    larget=num[0]
    for num in larget:
        if num<larget:
            larget=num
            print(num)
solve()
    
