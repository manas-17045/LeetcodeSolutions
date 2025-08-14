# Leetcode 2264: Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Solved on 14th of August, 2025
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Finds the largest good integer (a 3-digit number with all same digits) that is a substring of `num`.
        :param num: A string representing a large integer.
        :return: The largest good integer as a string, or an empty string if no good integer is found.
        """
        # Will hold the best single digit character seen
        best = None
        n = len(num)

        for i in range(n - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                # Update best if this digit is larger
                if best is None or num[i] > best:
                    best = num[i]

        return best * 3 if best is not None else ""