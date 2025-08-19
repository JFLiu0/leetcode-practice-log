# Problem ID: 02461
# Title: 2461. Maximum Sum of Distinct Subarrays With Length K

# Attempt: 1
# Initial Result: TLE

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Method Exceed Time Limitation: Time Complexity of set() is O(k)
        # ans = 0
        # substr = []
        # for i, ele in enumerate(nums):
        #     substr.append(nums[i])

        #     if(i<k-1):
        #         continue
            
        #     if(len(set(substr)) == k):
        #         ans = max(ans,sum(substr))

        #     del substr[0]

        # return ans

        # Method with hashmap
        ans = 0
        s = 0
        cnt = defaultdict(int)

        for i,ele in enumerate(nums):
            s += ele
            cnt[ele] += 1

            if (i < k-1):
                continue

            if (len(cnt) == k):
                ans = max(ans, s)

            s -= nums[i-k+1]
            cnt[nums[i-k+1]] -= 1
            if (cnt[nums[i-k+1]] == 0):
                del cnt[nums[i-k+1]]
        
        return ans