# Leetcode 165: Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# Solved on 23rd of September, 2025
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compares two version numbers.
        :param version1: The first version string.
        :param version2: The second version string.
        :return: -1 if version1 < version2, 1 if version1 > version2, 0 if version1 == version2.
        """
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')

        len1 = len(revisions1)
        len2 = len(revisions2)
        maxLength = max(len1, len2)

        for i in range(maxLength):
            val1 = 0
            if i < len1:
                val1 = int(revisions1[i])

            val2 = 0
            if i < len2:
                val2 = int(revisions2[i])

            if val1 < val2:
                return -1
            elif val1 > val2:
                return 1

        return 0