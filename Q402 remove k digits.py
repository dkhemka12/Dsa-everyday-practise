# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

def removeKdigits(num, k):
    stack = []

    for c in num:
        while k>0 and stack and stack[-1]>c:
            stack.pop()
            k -= 1
        stack.append(c)
    while k>0:
        stack.pop()
        k -= 1
    result = "".join(stack).lstrip("0")

    return result if result else "0"

num = input()
k = int(input())
result = removeKdigits(num, k)
print(result)
