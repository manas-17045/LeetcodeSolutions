# Leetcode 165: Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# Solved on 23rd of September, 2025
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compares two version numbers.
        :param version1: The first version string.
        :param version2: The second version string.
        :return: 1 if version1 > version2, -1 if version1 < version2, and 0 otherwise.
        """
        i, j = 0, 0
        n1, n2 = len(version1), len(version2)

        while i < n1 or j < n2:
            num1 = 0
            while i < n1 and version1[i] != '.':
                # Build integer digit-by-digit
                num1 = num1 * 10 + (ord(version1[i]) - 48)
                i += 1

            # Skip the dot if present
            if i < n1 and version1[i] == '.':
                i += 1

            num2 = 0
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + (ord(version2[j]) - 48)
                j += 1

            if j < n2 and version2[j] == '.':
                j += 1

            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

        return 0