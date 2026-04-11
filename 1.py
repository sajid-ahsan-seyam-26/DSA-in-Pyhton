def solve():
    arr = list(map(int, input().split()))
    total = 0
    for num in arr:
        total += num
    print(total)

if __name__ == "__main__":
    solve()
