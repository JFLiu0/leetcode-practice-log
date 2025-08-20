# Problem ID: 03439
# Title: 3439. Reschedule Meetings for Maximum Free Time I

# Attempt: 1
# Initial Result: REF

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        freeList = [0] * (len(startTime) + 1)
        freeList[0] = startTime[0]
        for i in range(1, len(startTime)):
            freeList[i] = startTime[i] - endTime[i-1]
        freeList[len(startTime)] = eventTime - endTime[-1]

        ans = s = 0
        for i, ele in enumerate(freeList):
            s += ele

            if (i-(k+1)+1 < 0):
                continue
            
            ans = max(s,ans)

            s -= freeList[i-(k+1)+1]

        return ans
