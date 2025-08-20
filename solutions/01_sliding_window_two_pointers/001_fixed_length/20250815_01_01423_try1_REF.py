# Problem ID: 01423
# Title: 1423. Maximum Points You Can Obtain from Cards

# Attempt: 1
# Initial Result: REF

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1,k+1):
            s = s + cardPoints[-i] - cardPoints[k-i]
            ans = max (ans, s)
        return ans