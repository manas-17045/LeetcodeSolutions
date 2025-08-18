# Leetcode 679: 24 Game
# https://leetcode.com/problems/24-game/
# Solved on 18th of August, 2025
class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        """
        Given a list of four numbers, determine if it's possible to obtain 24 using
        addition, subtraction, multiplication, and division.
        :param cards: A list of four integers.
        :return: True if 24 can be obtained, False otherwise.
        """
        nums = [float(x) for x in cards]
        EPS = 1e-6

        def helper(arr: list[float]) -> bool:
            if len(arr) == 0:
                return False
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            # Try every unordered pair i < j
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = arr[i], arr[j]
                    # Build list of remaining numbers after removing i and j
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    # Possible results of combining a and b
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    # Try each candidate and recurse
                    for val in candidates:
                        rest.append(val)
                        if helper(rest):
                            return True
                        rest.pop()

            return False

        return helper(nums)