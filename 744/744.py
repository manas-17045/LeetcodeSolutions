# Leetcode 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Solved on 31st of January, 2026
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Finds the smallest character in the list that is lexicographically greater than the target.

        :param letters: A list of characters sorted in non-decreasing order.
        :param target: The target character to compare against.
        :return: The smallest character greater than target, or the first character if none exist.
        """
        left = 0
        lettersCount = len(letters)
        right = lettersCount

        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left % lettersCount]