# Problem ID: 01456
# Title: Maximum Number of Vowels in a Substring of Given Length
# Category: Sliding Window (Fixed Length)
# Attempt: 1
# Initial Result: AC (Accepted)
# Date: 2025-08-14

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        vow = 0
        for i,ele in enumerate(s):
            if s[i] in "aeiou":
                vow += 1
            if i < k-1:
                continue
            
            ans = max(ans,vow)

            if s[i-k+1] in "aeiou":
                vow -= 1
        
        return ans
