def solve():
    text=input()
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if  ch.isalpha() and ch not in vowels:
            count=count+1
            print(count)
solve()
        