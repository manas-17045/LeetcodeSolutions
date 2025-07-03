# Leetcode 1494: Parallel Courses II
# https://leetcode.com/problems/parallel-courses-ii/
# Solved on 3rd of July, 2025
class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        """
        Calculates the minimum number of semesters required to take all 'n' courses.

        Args:
            n (int): The total number of courses.
            relations (list[list[int]]): A list of prerequisite relations, where
                                         relations[i] = [u, v] means course u must be
                                         taken before course v.
            k (int): The maximum number of courses that can be taken in one semester.

        Returns:
            int: The minimum number of semesters needed to complete all courses.
                 Returns -1 if it's impossible to complete all courses (though problem constraints usually guarantee possibility).
        """
        prereq_mask = [0] * n
        for u, v in relations:
            prereq_mask[v - 1] |= 1 << (u - 1)

        FULL = (1 << n) - 1
        INF = n + 1
        dp = [INF] * (1 << n)
        dp[0] = 0

        # Iterate over all subsets of courses already taken
        for mask in range(1 << n):
            if dp[mask] == INF:
                continue

            # Compute which courses we can take next
            avail = 0
            for i in range(n):
                if not (mask & (1 << i)) and (mask & prereq_mask[i]) == prereq_mask[i]:
                    avail |= (1 << i)

            # If we can take all available courses within k, do so
            cnt_avail = avail.bit_count()
            if cnt_avail <= k:
                nxt = mask | avail
                if dp[nxt] > dp[mask] + 1:
                    dp[nxt] = dp[mask] + 1
            else:
                # Otherwise, try every subset of avail with exactly k bits
                # Iterate submasks of avail
                sub = avail
                while sub:
                    if sub.bit_count() == k:
                        nxt = mask | sub
                        if dp[nxt] > dp[mask] + 1:
                            dp[nxt] = dp[mask] + 1
                    sub = (sub - 1) & avail

        return dp[FULL]