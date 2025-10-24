# Leetcode 3458: Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/
# Solved on 24th of October, 2025
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        """
        Determines if it's possible to select k disjoint "special" substrings from string s.
        A substring is "special" if all characters within it appear for the first time
        within that substring, and all subsequent occurrences of those characters are also
        within that substring.
        :param s: The input string.
        :param k: The number of disjoint special substrings to find.
        :return: True if k disjoint special substrings can be found, False otherwise.
        """
        n = len(s)
        if k == 0:
            return True

        first = {}
        last = {}
        for i, char in enumerate(s):
            last[char] = i
            if char not in first:
                first[char] = i

        memoFind = {}

        def findInterval(start):
            if start == n:
                return -1
            if start in memoFind:
                return memoFind[start]

            charStart = s[start]
            if first[charStart] < start:
                memoFind[start] = -1
                return -1

            end = last[charStart]
            j = start + 1
            while j <= end:
                charJ = s[j]
                if first[charJ] < start:
                    memoFind[start] = j
                    return -1
                if last[charJ] > end:
                    end = last[charJ]
                j += 1

            if end - start + 1 == n:
                memoFind[start] = -1
                return -1

            memoFind[start] = end
            return end

        memoDp = {}

        def solve(i):
            if i >= n:
                return 0
            if i in memoDp:
                return memoDp[i]

            res = solve(i + 1)

            end = findInterval(i)
            if end != -1:
                res = max(res, 1 + solve(end + 1))

            memoDp[i] = res
            return res

        return solve(0) >= k