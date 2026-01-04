# Leetcode 3006: Find Beautiful Indices in the Given Array I
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/
# Solved on 4th of January, 2026
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        """
        Finds all "beautiful" indices in a string `s`.
        An index `i` is beautiful if `s[i:i+len(a)] == a` and there exists an index `j`
        such that `s[j:j+len(b)] == b` and `abs(i - j) <= k`.

        :param s: The main string to search within.
        :param a: The first substring to find.
        :param b: The second substring to find.
        :param k: The maximum allowed absolute difference between indices `i` and `j`.
        :return: A list of all beautiful indices `i`.
        """
        sLen = len(s)
        aLen = len(a)
        bLen = len(b)

        indicesA = []
        for i in range(sLen - aLen + 1):
            if s[i:i + aLen] == a:
                indicesA.append(i)

        indicesB = []
        for j in range(sLen - bLen + 1):
            if s[j:j + bLen] == b:
                indicesB.append(j)

        result = []
        bIndex = 0
        bCount = len(indicesB)

        for i in indicesA:
            while bIndex < bCount and indicesB[bIndex] < i - k:
                bIndex += 1

            if bIndex < bCount and abs(indicesB[bIndex] - i) <= k:
                result.append(i)

        return result