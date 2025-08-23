# Problem ID: 03090
# Title: 3090. Maximum Length Substring With Two Occurrences

# Attempt: 1
# Initial Result: AC

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        cnt = defaultdict(int)
        for r, ele in enumerate(s):
            cnt[ele] += 1
            while (cnt[ele]>2):
                cnt[s[l]] -= 1
                l += 1
            ans = max (ans, r-l+1)
        
        return ans