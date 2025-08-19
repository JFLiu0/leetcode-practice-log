# Problem ID: 00643
# Title: 643. Maximum Average Subarray I

# Attempt: 1
# Initial Result: AC

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = -inf
        s = 0
        for i,ele in enumerate (nums):
            s += nums[i]  # 1. into the windows

            if i<k-1:
                continue
            
            max_s = max(max_s,s)  # 2. update the max

            s -= nums[i-k+1]  #3. get of the window
        
        return max_s/k
