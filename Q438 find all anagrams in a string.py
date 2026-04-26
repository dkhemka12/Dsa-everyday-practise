# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
def findAnagrams(s, p):
    res = []
    count = [0] * 26

    for c in p:
            count[ord(c) - ord('a')] += 1

    l = 0

    for r in range(len(s)):
        count[ord(s[r]) - ord('a')] -= 1

        if r - l + 1 > len(p):
            count[ord(s[l]) - ord('a')] += 1
            l += 1

        if max(count) == 0:
            res.append(l)

    return res

s = input()
p = input()

result = findAnagrams(s, p)
print(result)
