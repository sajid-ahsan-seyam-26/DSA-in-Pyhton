def solve():
    text=input()
    vowels="aeiouAEIOU"
    result=""
    for ch in text:
        if ch in vowels:
            result=result+"*"
        else:
            result=result+ch
            print(result)
solve()