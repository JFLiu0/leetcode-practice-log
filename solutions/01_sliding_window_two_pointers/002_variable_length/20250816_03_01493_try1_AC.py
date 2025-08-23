# Problem ID: 01493
# Title: 1493. Longest Subarray of 1's After Deleting One Element

# Attempt: 1
# Initial Result: AC

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        s = 0
        zeroCnt = 0
        for r, ele in enumerate(nums):
            s += ele
            if (ele == 0):
                zeroCnt += 1
            
            while (zeroCnt > 1):
                if(nums[l] == 0):
                    zeroCnt -= 1
                s -= nums[l]
                l += 1
            ans = max(ans,s) 
        return ans if zeroCnt == 1 else ans-1