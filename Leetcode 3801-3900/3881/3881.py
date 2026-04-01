# Leetcode 3881: Direction Assignment with Exactly K Visible People
# https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/
# Solved on 1st of April, 2026
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        """
        Calculates the number of ways to assign directions such that exactly k people are visible.

        :param n: The total number of people.
        :param pos: The position of the observer.
        :param k: The exact number of visible people required.
        :return: The number of valid direction assignments modulo 10^9 + 7.
        """
        modVal = 1000000007

        k = min(k, n - 1 - k)
        numVal = 1
        denVal = 1
        for i in range(k):
            numVal = (numVal * (n - 1 - i)) % modVal
            denVal = (denVal * (i + 1)) % modVal

        return (2 * numVal * pow(denVal, modVal - 2, modVal)) % modVal