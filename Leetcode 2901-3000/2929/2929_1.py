# Leetcode 2929: Distribute Candies among Children II
# https://leetcode.com/problems/distribute-candies-among-children-ii/
# Solved on 1st of June, 2025

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Calculates the number of ways to distribute n candies among 3 children
        such that each child receives at most limit candies.

        Args:
            n: The total number of candies.
            limit: The maximum number of candies each child can receive.
        """
        def countConfigs(candies: int) -> int:
            if candies < 0:
                return 0
            return (candies + 2)*(candies + 1) // 2

        ans = countConfigs(n)
        ans -= 3 * (countConfigs(n - (limit + 1)))
        ans += 3 * countConfigs(n - 2 * (limit + 1))
        ans -= countConfigs(n - 3 * (limit + 1))
        return ans