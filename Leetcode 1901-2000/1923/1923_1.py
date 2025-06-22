# Leetcode 1923: Longest Common Subpath
# https://leetcode.com/problems/longest-common-subpath/
# Solved on 22nd of June, 2025
class Solution:
    _BASE1 = 100003
    _BASE2 = 100007
    _MOD1 = 10**9 + 7
    _MOD2 = 10**9 + 9

    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        """
        Finds the length of the longest common subpath among all given paths.

        This problem is solved using binary search on the length of the common subpath
        combined with a Rabin-Karp rolling hash approach to efficiently check if a
        subpath of a given length `k` exists in all paths.

        Args:
            n: The number of distinct cities (not directly used in the solution logic,
               but part of the problem statement).
            paths: A list of lists, where each inner list represents a path of cities.
        """
        paths.sort(key=len)

        minPathLen = len(paths[0])
        if minPathLen == 0:
            return 0

        longestLenFound = 0
        low = 1
        high = minPathLen

        while low <= high:
            candidateLen = low + (high - low) // 2
            if self.check(candidateLen, paths):
                longestLenFound = candidateLen
                low = candidateLen + 1
            else:
                high = candidateLen - 1

        return longestLenFound

    def check(self, k: int, paths: list[list[int]]) -> bool:
        # Calculate Base^(k - 1) % Mod for hash rolling
        powerBase1KMinus1 = pow(self._BASE1, (k - 1), self._MOD1)
        powerBase2KMinus1 = pow(self._BASE2, (k - 1), self._MOD2)

        # Process the first path (which is the shortest after sorting)
        path0 = paths[0]

        commonHashes = set()
        currentHash1, currentHash2 = 0, 0
        # Calculate hash for the first window of path0
        for j in range(k):
            city = path0[j]
            currentHash1 = (currentHash1 * self._BASE1 + city) % self._MOD1
            currentHash2 = (currentHash2 * self._BASE2 + city) % self._MOD2
        commonHashes.add((currentHash1, currentHash2))

        # Roll hash for the remaining subpaths of path0
        for j in range(k, len(path0)):
            cityToRemove = path0[j - k]
            cityToAdd = path0[j]

            # Update hash1
            termToSubtract1 = (cityToRemove * powerBase1KMinus1) % self._MOD1
            # Ensure positive
            currentHash1 = (currentHash1 - termToSubtract1 + self._MOD1) % self._MOD1
            currentHash1 = (currentHash1 * self._BASE1 + cityToAdd) % self._MOD1

            # Update hash2
            termToSubtract2 = (cityToRemove * powerBase2KMinus1) % self._MOD2
            # Ensure positive
            currentHash2 = (currentHash2 - termToSubtract2 + self._MOD2) % self._MOD2
            currentHash2 = (currentHash2 * self._BASE2 + cityToAdd) % self._MOD2

            commonHashes.add((currentHash1, currentHash2))

        if not commonHashes:
            return False

        # Process subsequent paths
        for i in range(1, len(paths)):
            path = paths[i]

            hashesInThisPath = set()
            currentHash1, currentHash2 = 0, 0
            # Calculate hash for the first window of the current path
            for j in range(k):
                city = path[j]
                currentHash1 = (currentHash1 * self._BASE1 + city) % self._MOD1
                currentHash2 = (currentHash2 * self._BASE2 + city) % self._MOD2

            # Optimization: Only consider this subpath if its hash is in commonHashes
            if (currentHash1, currentHash2) in commonHashes:
                hashesInThisPath.add((currentHash1, currentHash2))

            # Roll hash for the remaining subpaths of the current path
            for j in range(k, len(path)):
                cityToRemove = path[j - k]
                cityToAdd = path[j]

                termToSubtract1 = (cityToRemove * powerBase1KMinus1) % self._MOD1
                currentHash1 = (currentHash1 - termToSubtract1 + self._MOD1) % self._MOD1
                currentHash1 = (currentHash1 * self._BASE1 + cityToAdd) % self._MOD1

                termToSubtract2 = (cityToRemove * powerBase2KMinus1) % self._MOD2
                currentHash2 = (currentHash2 - termToSubtract2 + self._MOD2) % self._MOD2
                currentHash2 = (currentHash2 * self._BASE2 + cityToAdd) % self._MOD2

                if (currentHash1, currentHash2) in commonHashes:
                    hashesInThisPath.add((currentHash1, currentHash2))

            commonHashes.intersection_update(hashesInThisPath)
            # If intersection is empty, no common subpath of length k
            if not commonHashes:
                return False

        # commonHashes is non-empty, so a common subpath of length k exists.
        return True