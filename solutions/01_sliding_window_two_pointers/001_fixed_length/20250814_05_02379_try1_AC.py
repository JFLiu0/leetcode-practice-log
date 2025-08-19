# Problem ID: 02379
# Title: 2379. inimum Recolors to Get K Consecutive Black Blocks

# Attempt: 1
# Initial Result: AC

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        w_n = 0

        for i,ele in enumerate(blocks):
            if blocks[i] == 'W':
               w_n += 1

            if (i<k-1):
                continue

            ans = min(ans,w_n)

            if blocks[i-k+1] == 'W':
                w_n -= 1

        return ans