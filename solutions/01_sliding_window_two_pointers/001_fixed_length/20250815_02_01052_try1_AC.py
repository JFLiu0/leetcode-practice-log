# Problem ID: 01052
# Title: 1052. Grumpy Bookstore Owner

# Attempt: 1
# Initial Result: AC

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        flipped = [1 - x for x in grumpy]
        for i,ele in enumerate (customers):
            ans += customers[i]*flipped[i]  # calculate the total number
        
        s = ans
        for i,ele in enumerate (customers):
            if (grumpy[i] == 1):
                s += customers[i]
            
            if (i-minutes+1 < 0):
                continue
            
            ans = max (ans,s)

            if (grumpy[i-minutes+1] == 1):
                s -= customers[i-minutes+1]
        
        return ans