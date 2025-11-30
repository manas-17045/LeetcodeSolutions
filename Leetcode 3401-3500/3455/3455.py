# Leetcode 3455: Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/
# Solved on 30th of November, 2025
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        """
        Finds the shortest substring in `s` that matches the pattern `p`.

        Args:
            s (str): The main string to search within.
            p (str): The pattern string, which can contain at most two '*' wildcards.
        Returns:
            int: The length of the shortest matching substring, or -1 if no such substring exists.
        """
        n = len(s)
        parts = p.split('*')
        p1, p2, p3 = parts[0], parts[1], parts[2]
        len1, len2, len3 = len(p1), len(p2), len(p3)

        # Helper to get all start indices of a pattern in text using KMP
        def getMatches(pattern):
            if not pattern:
                return range(n + 1)

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

            matches = []
            i = 0
            j = 0
            while i < n:
                if pattern[j] == s[i]:
                    i += 1
                    j += 1
                if j == m:
                    matches.append(i - m)
                    j = lps[j - 1]
                elif i < n and pattern[j] != s[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return matches

        # Precompute nearest valid end index for p1
        # nearestEnd1[i] = max end_index of p1 such that end_index <= i
        nearestEnd1 = [-1] * (n + 1)
        if not p1:
            for i in range(n + 1):
                nearestEnd1[i] = i
        else:
            matches1 = getMatches(p1)
            for start in matches1:
                end = start + len1
                nearestEnd1[end] = end

            currentMax = -1
            for i in range(n + 1):
                if nearestEnd1[i] != -1:
                    currentMax = nearestEnd1[i]
                else:
                    nearestEnd1[i] = currentMax

        # Precompute nearest valid start index for p3
        # nextStart3[i] = min start_index of p3 such that start_index >= i
        nextStart3 = [float('inf')] * (n + 1)
        if not p3:
            for i in range(n + 1):
                nextStart3[i] = i
        else:
            matches3 = getMatches(p3)
            for start in matches3:
                nextStart3[start] = start

            currentMin = float('inf')
            for i in range(n, -1, -1):
                if nextStart3[i] != float('inf'):
                    currentMin = nextStart3[i]
                else:
                    nextStart3[i] = currentMin

        # Iterate through all occurrences of p2 and find optimal p1 and p3
        matches2 = getMatches(p2)
        minLen = float('inf')

        for start2 in matches2:
            end2 = start2 + len2

            # Find closest p1 ending before or at start of p2
            p1End = nearestEnd1[start2]
            if p1End == -1:
                continue

            # Find closest p3 starting after or at end of p2
            if end2 > n:
                continue

            p3Start = nextStart3[end2]
            if p3Start == float('inf'):
                continue

            # Calculate total length: (end of p3) - (start of p1)
            p1Start = p1End - len1
            p3End = p3Start + len3
            currentLen = p3End - p1Start

            if currentLen < minLen:
                minLen = currentLen

        return minLen if minLen != float('inf') else -1