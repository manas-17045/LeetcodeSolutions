# Leetcode 2305: Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/
# Solved on 15th of June, 2025

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        """
        Distributes cookies among k children such that the unfairness is minimized.
        Unfairness is defined as the maximum total number of cookies received by any single child.

        Args:
            cookies: A list of integers representing the number of cookies in each bag.
            k: The number of children.

        Returns:
            The minimum possible unfairness.
        """
        # Sort descending to place big cookies first (better pruning)
        cookies.sort(reverse=True)
        n = len(cookies)

        sums = [0] * k
        best = float('inf')
        current_max = 0

        def dfs(idx: int):
            nonlocal best, current_max
            # If all cookies distributed, update best
            if idx == n:
                best = current_max
                return

            c = cookies[idx]
            # Try to give cookie idx to each child
            for j in range(k):
                # Prune if this would not improve the best
                if sums[j] + c >= best:
                    continue

                prev_sum = sums[j]
                prev_max = current_max

                # Place cookie
                sums[j] += c
                # Update current maximum
                current_max = max(current_max, sums[j])

                # Recurse
                dfs(idx + 1)

                # Backtrack
                sums[j] = prev_sum
                current_max = prev_max

                # Symmetry break
                if prev_sum == 0:
                    break

        dfs(0)
        return int(best)