# Leetcode 2983: Palindrome Rearrangement Queries
# https://leetcode.com/problems/palindrome-rearrangement-queries/
# Solved on 9th of July, 2025
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        Determines if a string can be made into a palindrome by swapping characters within two specified ranges.

        Args:
            s: The input string.
            queries: A list of queries, where each query is [a, b, c, d] representing two ranges [a, b] and [c, d].

        Returns:
            A list of booleans, where each boolean indicates whether the corresponding query can result in a palindrome.
        """
        n = len(s)
        halfN = n // 2

        sLeft = s[:halfN]
        sRightRev = s[halfN:][::-1]

        prefixMismatch = [0] * (halfN + 1)
        for i in range(halfN):
            prefixMismatch[i + 1] = prefixMismatch[i]
            if sLeft[i] != sRightRev[i]:
                prefixMismatch[i + 1] += 1

        prefixCountsLeft = [[0] * 26 for _ in range(halfN + 1)]
        prefixCountsRight = [[0] * 26 for _ in range(halfN + 1)]

        for i in range(halfN):
            for j in range(26):
                prefixCountsLeft[i + 1][j] = prefixCountsLeft[i][j]
                prefixCountsRight[i + 1][j] = prefixCountsRight[i][j]
            prefixCountsLeft[i + 1][ord(sLeft[i]) - ord('a')] += 1
            prefixCountsRight[i + 1][ord(sRightRev[i]) - ord('a')] += 1

        def getCountsInRange(prefixCounts, start, end):
            if start > end:
                return [0] * 26
            res = [0] * 26
            for i in range(26):
                res[i] = prefixCounts[end + 1][i] - prefixCounts[start][i]
            return res

        answer = []
        for a, b, c, d in queries:
            cPrime = n - 1 - d
            dPrime = n - 1 - c

            intersectStart = max(a, cPrime)
            intersectEnd = min(b, dPrime)

            mismatchesInA = prefixMismatch[b + 1] - prefixMismatch[a]
            mismatchesInB = prefixMismatch[dPrime + 1] - prefixMismatch[cPrime]
            mismatchesInIntersection = 0
            if intersectStart <= intersectEnd:
                mismatchesInIntersection = prefixMismatch[intersectEnd + 1] - prefixMismatch[intersectStart]
            mismatchesInUnion = mismatchesInA + mismatchesInB - mismatchesInIntersection
            totalMismatches = prefixMismatch[halfN]

            if totalMismatches - mismatchesInUnion > 0:
                answer.append(False)
                continue

            poolA = getCountsInRange(prefixCountsLeft, a, b)
            poolB = getCountsInRange(prefixCountsRight, cPrime, dPrime)

            neededForA = getCountsInRange(prefixCountsRight, a, b)
            countsInIntersectionR = getCountsInRange(prefixCountsRight, intersectStart, intersectEnd)
            for i in range(26):
                neededForA[i] -= countsInIntersectionR[i]

            remPoolA = list(poolA)
            for i in range(26):
                remPoolA[i] -= neededForA[i]
            if any(count < 0 for count in remPoolA):
                answer.append(False)
                continue

            neededForB = getCountsInRange(prefixCountsLeft, cPrime, dPrime)
            countsInIntersectionL = getCountsInRange(prefixCountsLeft, intersectStart, intersectEnd)
            for i in range(26):
                neededForB[i] -= countsInIntersectionL[i]

            remPoolB = list(poolB)
            for i in range(26):
                remPoolB[i] -= neededForB[i]
            if any(count < 0 for count in remPoolB):
                answer.append(False)
                continue

            if remPoolA == remPoolB:
                answer.append(True)
            else:
                answer.append(False)

        return answer