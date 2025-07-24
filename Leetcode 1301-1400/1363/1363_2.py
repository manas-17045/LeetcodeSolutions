# Leetcode 1363: Largest Multiple of Three
# https://leetcode.com/problems/largest-multiple-of-three/
# Solved on 24th of July, 2025
class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        """
        Given a list of digits, return the largest multiple of three that can be formed by concatenating some of the
        given digits in any order.

        Args:
            digits (list[int]): A list of digits.
        Returns:
            str: The largest multiple of three that can be formed, or an empty string if no such number can be formed.
        """
        freq = [0] * 10
        total = 0
        for d in digits:
            freq[d] += 1
            total += d

        # Helper function to remove k digits of given mod-class in ascending order
        def remove_digits(target_mod: int, k: int) -> bool:
            if target_mod == 1:
                choices = [1, 4, 7]
            else:
                choices = [2, 5, 8]

            for _ in range(k):
                for d in choices:
                    if freq[d] > 0:
                        freq[d] -= 1
                        break
                else:
                    return False

            return True

        rem = total % 3
        if rem == 1:
            if not remove_digits(1, 1) and not remove_digits(2, 2):
                return ""

        elif rem == 2:
            if not remove_digits(2, 1) and not remove_digits(1, 2):
                return ""

        # Build the result in descending order
        res = []
        for d in range(9, -1, -1):
            if freq[d]:
                res.append(str(d) * freq[d])

        if not res:
            return ""

        if res[0][0] == '0':
            return "0"

        return "".join(res)