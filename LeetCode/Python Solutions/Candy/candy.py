from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n
        
        # Left-to-right scan
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
        # Right-to-left scan
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
                
        return sum(candies)
