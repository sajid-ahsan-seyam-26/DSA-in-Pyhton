def solve():
    text=input()
    vowels="aeiou"
    count=0
    for ch in text:
        if ch in vowels:
            count=count+1
            print(count)
solve()