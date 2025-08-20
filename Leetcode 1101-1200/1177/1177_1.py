# Leetcode 1177: Can Make Palindrome from Substring
# https://leetcode.com/problems/can-make-palindrome-from-substring/
# Solved on 20th of August, 2025
class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        Given a string s and an array of queries, where each query queries[i] = [left, right, k],
        return an array of boolean results, where result[i] is true if you can make a palindrome
        from the substring s[left...right] by changing at most k characters.

        :param s: The input string.
        :param queries: A list of queries, where each query is [left, right, k].
        :return: A list of booleans indicating whether each query can form a palindrome.
        """
        strLength = len(s)
        prefixMasks = [0] * (strLength + 1)

        currentMask = 0
        for i in range(strLength):
            charIndex = ord(s[i]) - ord('a')
            currentMask ^= (1 << charIndex)
            prefixMasks[i + 1] = currentMask

        answer = []
        for currentQuery in queries:
            left, right, k = currentQuery[0], currentQuery[1], currentQuery[2]

            substringMask = prefixMasks[right + 1] ^ prefixMasks[left]

            oddCount = bin(substringMask).count('1')

            changesNeeded = oddCount // 2

            answer.append(changesNeeded <= k)

        return answer