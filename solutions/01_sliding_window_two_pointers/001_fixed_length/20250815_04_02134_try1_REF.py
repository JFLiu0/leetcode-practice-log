# Problem ID: 02134
# Title: 2134. Minimum Swaps to Group All 1's Together II

# Attempt: 1
# Initial Result: REF

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        if (k == 0):
            return 0
        
        max1 = cnt1 = 0
        for i in range(0,n+k-1):
            cnt1 += nums[i%n]

            if (i < k-1):
                continue

            max1 = max(cnt1,max1)

            cnt1 -= nums[(i-k+1)%n]

        return k-max1 