# Problem ID: 02841
# Title: 2841. Maximum Sum of Almost Unique Subarray

# Attempt: 1
# Initial Result: AC

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0
        sub_str = []
        for i,ele in enumerate(nums):
            sub_str.append(ele)
            
            if (i < k-1):
                continue    

            if (len(set(sub_str))>=m):
                ans = max(ans, sum(sub_str))
                
            del sub_str[0]

        return ans
