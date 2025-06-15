# Leetcode 2305: Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/
# Solved on 15th of June, 2025

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        """
        Distributes cookies among k children such that the unfairness (maximum number of cookies any child receives)
        is minimized.

        Args:
            cookies: A list of integers representing the number of cookies in each bag.
            k: The number of children.

        Returns:
            The minimum possible unfairness.
        """
        n = len(cookies)
        self.minUnfairness = float('inf')

        cookies.sort(reverse=True)

        distribution = [0] * k

        def solve(cookieIndex):
            if cookieIndex == n:
                self.minUnfairness = min(self.minUnfairness, max(distribution))
                return

            if self.minUnfairness <= max(distribution):
                return

            for childIndex in range(k):
                distribution[childIndex] += cookies[cookieIndex]

                if distribution[childIndex] < self.minUnfairness:
                    solve(cookieIndex + 1)

                distribution[childIndex] -= cookies[cookieIndex]

                if distribution[childIndex] == 0:
                    break

        solve(0)
        return int(self.minUnfairness)