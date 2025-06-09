# Leetcode 2376: Count Special Integers
# https://leetcode.com/problems/count-special-integers/
# Solved on 9th of June, 2025

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """
        Counts the number of positive integers less than or equal to n that have distinct digits.

        A number is considered "special" if all of its digits are distinct.

        The approach is to count special numbers by their length:
        1. Count all special numbers with length less than the length of n.
        2. Count special numbers with the same length as n by iterating through the digits of n
           and considering numbers with prefixes smaller than the prefix of n.

        Args:
            n: The upper bound (inclusive).

        Returns:
            The count of special numbers less than or equal to n.
        """
        s = str(n)
        L = len(s)

        # helper: P(a, b) = a * (a-1) * ... * (a-b+1), with P(a,0)=1
        def perm(a: int, b: int) -> int:
            if b > a or b < 0:
                return 0
            res = 1
            for x in range(a, a - b, -1):
                res *= x
            return res

        ans = 0

        # Count all special numbers with length < L
        for k in range(1, L):
            ans += 9 * perm(9, k - 1)

        # Count special numbers of the same length by scanning prefix
        used = set()
        for i, ch in enumerate(s):
            d = int(ch)
            # Try placing at position i any digit x < d that hasn't been used
            for x in range(0 if i > 0 else 1, d):
                if x in used:
                    continue
                # If we place x here, there are rem = L-i-1 positions left,
                # and we have 10 - (|used|+1) digits remaining to choose from
                rem = L - i - 1
                available = 10 - (len(used) + 1)
                ans += perm(available, rem)

            # If d itself is already used, we cannot match the prefix any further
            if d in used:
                break
            used.add(d)
        else:
            # If we never broke out, n itself has all distinct digits
            ans += 1

        return ans