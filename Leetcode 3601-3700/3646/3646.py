# Leetcode 3646: Next Special Palindrome Number
# https://leetcode.com/problems/next-special-palindrome-number/
# Solved on 19th of December, 2025
from itertools import permutations, combinations


class Solution:
    def specialPalindrome(self, n: int) -> int:
        """
        Finds the next special palindrome number greater than n.

        Args:
            n: The input integer.
        Returns:
            The next special palindrome number greater than n.
        """
        def generateCandidates(length):
            candidates = []
            digits = range(1, 10)
            for r in range(1, 10):
                for subset in combinations(digits, r):
                    if sum(subset) != length:
                        continue

                    oddDigits = [d for d in subset if d % 2 != 0]

                    if length % 2 == 0:
                        if oddDigits:
                            continue
                        midStr = ""
                    else:
                        if len(oddDigits) != 1:
                            continue
                        midStr = str(oddDigits[0])

                    halfList = []
                    for digit in subset:
                        count = digit
                        if midStr and digit == int(midStr):
                            count -= 1
                        halfList.extend([str(digit)] * (count // 2))

                    distinctPerms = set(permutations(halfList))

                    for perm in distinctPerms:
                        halfStr = "".join(perm)
                        fullStr = halfStr + midStr + halfStr[::-1]
                        candidates.append(int(fullStr))
            return candidates

        currentLength = len(str(n))
        while True:
            candidates = generateCandidates(currentLength)
            validCandidates = [x for x in candidates if x > n]
            if validCandidates:
                return min(validCandidates)
            currentLength += 1