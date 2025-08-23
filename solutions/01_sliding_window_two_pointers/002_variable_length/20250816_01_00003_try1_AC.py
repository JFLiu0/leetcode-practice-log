# Problem ID: 00003
# Title: 3. Longest Substring Without Repeating Characters

# Attempt: 1
# Initial Result: AC

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0  #left index
        cnt = defaultdict(int)
        for r, ele in enumerate (s):
            cnt[ele] += 1
            while (cnt[ele]>1):
                cnt[s[l]] -= 1
                l += 1
            ans = max (ans,r-l+1)
        return ans