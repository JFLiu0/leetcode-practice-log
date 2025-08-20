# Problem ID: 01652
# Title: 1652. Defuse the Bomb

# Attempt: 1
# Initial Result: REF

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0]*n
        r = k+1 if k>0 else n # right index (not included)
        k = abs(k)
        s = sum(code[r-k:r])
        for i in range (n):
            ans[i] = s
            s = s + code[r%n] - code[(r-k)%n]
            r += 1
        return ans