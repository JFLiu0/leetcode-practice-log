# Problem ID: 01343
# Title: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Attempt: 1
# Initial Result: AC

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        s = 0
        for i,ele in enumerate (arr):
            s += arr[i]

            if (i < k-1):
                continue

            if (s >= threshold*k):
                ans+=1
            
            s -= arr[i-k+1]

        return ans 

