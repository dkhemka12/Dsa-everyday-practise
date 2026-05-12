# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

def successfulPairs(spells, potions, success):
        potions.sort()
        pairs = []

        for spell in spells:
            need = (success + spell - 1) // spell

            left, right = 0, len(potions)

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= need:
                    right = mid
                else:
                    left = mid + 1

            pairs.append(len(potions) - left)

        return pairs

n=int(input())
spells=list(map(int,input().split()))
m=int(input())
potions=list(map(int,input().split()))
success=int(input())
print(successfulPairs(spells, potions, success))

