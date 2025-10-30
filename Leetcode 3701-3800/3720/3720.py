# Leetcode 3720: Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/
# Solved on 30th of October, 2025
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        """
        Finds the lexicographically smallest permutation of string 's' that is greater than string 'target'.

        Args:
            s (str): The input string from which to form a permutation.
            target (str): The target string to compare against.
        Returns:
            str: The lexicographically smallest permutation of 's' that is greater than 'target',
                 or an empty string if no such permutation exists.
        """
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        currentPerm = []

        def solve(index):
            if index == n:
                return False

            targetCharIndex = ord(target[index]) - ord('a')

            if counts[targetCharIndex] > 0:
                counts[targetCharIndex] -= 1
                currentPerm.append(target[index])

                if solve(index + 1):
                    return True

                currentPerm.pop()
                counts[targetCharIndex] += 1

            for i in range(targetCharIndex + 1, 26):
                if counts[i] > 0:
                    counts[i] -= 1
                    currentPerm.append(chr(ord('a') + i))

                    for k in range(26):
                        if counts[k] > 0:
                            currentPerm.append(chr(ord('a') + k) * counts[k])

                    return True

            return False

        return "".join(currentPerm) if solve(0) else ""