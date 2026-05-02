# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    pcount,scount = {} ,{}
    for i in range(len(p)):
        pcount[p[i]] = 1 + pcount.get(p[i],0)
        scount[s[i]] = 1 + scount.get(s[i],0)
    res = [0] if pcount == scount else []
    l=0
    for r in range(len(p),len(s)):
        scount[s[r]] = 1 + scount.get(s[r],0)
        scount[s[l]] -= 1
        if scount[s[l]] == 0:
            del scount[s[l]]
        l+=1
        if pcount == scount:
            res.append(l)

    return res

s = input("Enter the string s: ")
p = input("Enter the string p: ")


result = findAnagrams(s, p)
print("Anagram start indices:", result)