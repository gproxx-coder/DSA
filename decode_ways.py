
# https://leetcode.com/problems/decode-ways/

def decode(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    counter = [0] * (n + 1)
    counter[0] = counter[1] = 1
    for i in range(1, n):
        if s[i] != '0':
            counter[i + 1] += counter[i]
        if s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
            counter[i + 1] += counter[i - 1]
    return counter[n]


print(decode("10"))