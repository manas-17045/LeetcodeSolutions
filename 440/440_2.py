# Leetcode 440: K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Solved on 9th of June, 2025

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Finds the k-th smallest number in the lexicographical order of numbers from 1 to n.

        Args:
            n: The upper limit of the numbers to consider.
            k: The k-th number to find.

        Returns:
            The k-th smallest number in lexicographical order.
        """
        curr = 1
        k -= 1

        def countSteps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        while k > 0:
            steps = countSteps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr