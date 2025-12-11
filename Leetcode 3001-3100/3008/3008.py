# Leetcode 3008: Find Beautiful Indices in the Given Array II
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/
# Solved on 11th of December, 2025
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        """
        Finds "beautiful" indices in a string `s`. An index `i` is beautiful if `s[i:i+len(a)] == a`
        and there exists an index `j` such that `s[j:j+len(b)] == b` and `|i - j| <= k`.
        :param s: The main string to search within.
        :param a: The first pattern string.
        :param b: The second pattern string.
        :param k: The maximum allowed absolute difference between indices `i` and `j`.
        :return: A list of beautiful indices in ascending order.
        """
        def computeLPS(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def kmpSearch(text, pattern):
            n = len(text)
            m = len(pattern)
            lps = computeLPS(pattern)
            indices = []
            i = 0
            j = 0
            while i < n:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                if j == m:
                    indices.append(i - j)
                    j = lps[j - 1]
                elif i < n and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return indices

        indicesA = kmpSearch(s, a)
        indicesB = kmpSearch(s, b)

        ans = []
        bIndex = 0
        lenB = len(indicesB)

        for i in indicesA:
            while bIndex < lenB and indicesB[bIndex] < i - k:
                bIndex += 1
            if bIndex < lenB and abs(indicesB[bIndex] - i) <= k:
                ans.append(i)

        return ans