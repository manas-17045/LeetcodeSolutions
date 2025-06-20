# Leetcode 2358: Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
# Solved on 20th of June, 2025

class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        """
        Given a list of grades, form the maximum number of groups such that
        for any two consecutive groups, the later group has strictly more
        students and a strictly greater sum of grades than the earlier group.

        The students within each group can be chosen arbitrarily from the
        remaining students.

        Args:
            grades: A list of integers representing the grades of students.

        Returns:
            The maximum number of groups that can be formed.
        """
        # Sort grades to assign the smallest ones to earlier (smaller) groups
        grades.sort()
        n = len(grades)

        # Build prefix sums so segment sums can be queries in O(1) time
        prefix = [0] * (n + 1)
        for i, g in enumerate(grades, start=1):
            prefix[i] = prefix[i - 1] + g

        ans = 0
        prevSize = 0
        prevSum = 0
        start = 0

        # We'll move 'j' forward only, across all groups, at most n steps total.
        j = 0

        while True:
            # Next group must have strictly more members than prev_size
            j = max(j, (start + prevSize + 1))
            # Advance j until we either run out of students or the group-sum > prev_sum
            while j <= n and prefix[j] - prefix[start] <= prevSum:
                j += 1

            # if we ran out of students, can't form another valid group
            if j > n:
                break

            # Form the group
            currSize = j - start
            currSum = prefix[j] - prefix[start]

            # Update state for next iteration
            ans += 1
            prevSize = currSize
            prevSum = currSum
            start = j

        return ans