def solve():
    text = input()

    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    answer = -1
    for ch in text:
        if freq[ch] == 1:
            answer = ch
            break

    print(answer)

if __name__ == "__main__":
    solve()
