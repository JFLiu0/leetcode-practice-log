# Problem ID: 02090
# Title: 2090. K Radius Subarray Averages

# Attempt: 1
# Initial Result: AC

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        s = sum(nums[:2*k])

        for i,ele in enumerate(nums):
            if (i-k < 0 or i+k > len(nums)-1):
                ans.append(-1)
                continue
            
            s += nums[i+k]
            ans.append(math.floor(s/(2*k+1)))

            s -= nums[i-k]

        return ans
