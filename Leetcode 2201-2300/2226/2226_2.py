# Leetcode 2226: Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# Solved on 3rd of August, 2025
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        """
        Finds the maximum number of candies that can be given to each of k children.
        Args:
            candies (list[int]): A list of integers representing the number of candies in each pile.
            k (int): The number of children.
        Returns:
            int: The maximum number of candies each child can receive.
        """
        def can_make(x: int) -> bool:
            count = 0
            for c in candies:
                count += c // x
                if count >= k:
                    return True
            return False

        # If even piles of size 1 are insufficient, answer is 0 right away.
        total_candies = sum(candies)
        if total_candies < k:
            return 0
        
        lo, hi = 1, max(candies)
        best = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                best = mid
                lo = mid + 1    # mid is feasible, try for a larger size
            else:
                hi = mid - 1    # too large, reduce
        
        return best