# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    mapst,mapts = {}, {}
    for i in range(len(s)):
        c1,c2 = s[i], t[i]
        if (c1 in mapst and mapst[c1]!=c2) or (c2 in mapts and mapts[c2]!=c1):
            return False
        mapst[c1] = c2
        mapts[c2] = c1
    return True

s=input()
t=input()
print(isIsomorphic(s,t))