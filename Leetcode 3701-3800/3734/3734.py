# Leetcode 3734: Lexicographically Smallest Palindromic Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
# Solved on 21st of December, 2025
import collections


class Solution:
    def lenPalindromicPermutation(self, s: str, target: str) -> str:
        """
        Finds the lexicographically smallest palindromic permutation of string `s` that is greater than string `target`.

        Args:
            s (str): The input string from which to form a palindromic permutation.
            target (str): The target string to compare against.

        Returns:
            str: The lexicographically smallest palindromic permutation of `s` that is greater than `target`, or an empty string if no such permutation exists.
        """
        n = len(s)
        sCounts = collections.Counter(s)

        oddChar = ""
        oddCounts = 0
        for char, count in sCounts.items():
            if count % 2 == 1:
                oddCounts += 1
                oddChar = char

        if oddCounts > 1:
            return ""

        halfCounts = collections.Counter()
        for char, count in sCounts.items():
            halfCounts[char] = count // 2

        l = n // 2

        def buildPalindrome(half):
            mid = oddChar if n % 2 == 1 else ""
            return half + mid + half[::-1]

        targetHalf = target[:l]
        if not (collections.Counter(targetHalf) - halfCounts):
            candidate = buildPalindrome(targetHalf)
            if candidate > target:
                return candidate

        currReq = collections.Counter(targetHalf)

        for i in range(l - 1, -1, -1):
            charToRemove = target[i]
            currReq[charToRemove] -= 1
            if currReq[charToRemove] == 0:
                del currReq[charToRemove]

            if collections.Counter(currReq) - halfCounts:
                continue

            available = halfCounts - currReq

            foundPivot = None
            for charCode in range(ord(target[i]) + 1, ord('z') + 1):
                char = chr(charCode)
                if available[char] > 0:
                    foundPivot = char
                    break

            if foundPivot:
                prefix = target[:i]

                available[foundPivot] -= 1

                suffixChars = []
                for char in sorted(available.keys()):
                    suffixChars.append(char * available[char])
                suffix = "".join(suffixChars)

                newHalf = prefix + foundPivot + suffix
                return buildPalindrome(newHalf)

        return ""