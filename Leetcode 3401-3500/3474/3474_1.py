# Leetcode 3474: Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/
# Solved on 6th of June, 2025
import numpy as np


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        """
        Generates the lexicographically smallest string of length len(str1) + len(str2) - 1
        that is consistent with the constraints imposed by str1 and str2.

        Args:
            str1: A string consisting of 'T' and 'F' characters. 'T' at index i means the
                  generated string must have str2 as a substring starting at index i.
            str2: The substring that must appear at certain positions.

        Returns:
            The lexicographically smallest generated string, or "" if no such string exists.
        """
        n = len(str1)
        m = len(str2)
        wordLength = n + m - 1

        isT = np.array([1 if c == 'T' else 0 for c in str1])
        if np.sum(isT) > 1:
            pi = self.computePi(str2)
            borders = set()
            kPi = pi[m - 1]
            while kPi > 0:
                borders.add(kPi)
                kPi = pi[kPi - 1]
            validPeriods = {m - b for b in borders}

            correlation = np.correlate(isT, isT, "full")
            centerIndex = n - 1
            for d in range(1, m):
                if d not in validPeriods:
                    if correlation[centerIndex + d] > 0.5:
                        return ""

        forcedChar = [''] * wordLength
        lastT = -1

        lastTBefore = [-1] * n
        for i in range(n):
            if str1[i] == 'T':
                lastT = i
            lastTBefore[i] = lastT

        for i in range(wordLength):
            lt = -1
            if i < n:
                lt = lastTBefore[i]
            else:
                lt = lastT

            if lt != -1 and i < lt + m:
                forcedChar[i] = str2[i - lt]

        isUnforced = [c is None for c in forcedChar]
        fIndices = [i for i, c in enumerate(str1) if c == 'F']

        lastUnforcedInPrefix = [-1] * wordLength
        last = -1
        for j in range(wordLength):
            if isUnforced[j]:
                last = j
            lastUnforcedInPrefix[j] = last

        criticalFIndices = [[] for _ in range(wordLength)]
        for i in fIndices:
            if i + m > wordLength:
                continue

            k = -1
            if i + m - 1 < wordLength:
                k = lastUnforcedInPrefix[i + m - 1]

            if k != -1 and k >= i:
                suffixMatches = True
                for j in range(k + 1, i + m):
                    if forcedChar[j] is None or forcedChar[j] != str2[j - i]:
                        suffixMatches = False
                        break
                if suffixMatches:
                    criticalFIndices[k].append(i)
            else:
                allForcedMatch = True
                for j in range(i, i + m):
                    if forcedChar[j] is None or forcedChar[j] != str2[j - i]:
                        allForcedMatch = False
                        break
                if allForcedMatch:
                    return ""

        res = [''] * wordLength
        base1, mod1 = 31, 10**9 + 7
        base2, mod2 = 37, 10**9 + 9

        str2Hashes1 = self.computeHashes(str2, base1, mod1)
        str2Hashes2 = self.computeHashes(str2, base2, mod2)
        str2Powers1 = self.computePowers(m, base1, mod1)
        str2Powers2 = self.computePowers(m, base2, mod2)

        resHashes1 = [0] * (wordLength + 1)
        resHashes2 = [0] * (wordLength + 1)
        resPowers1 = self.computePowers(wordLength, base1, mod1)
        resPowers2 = self.computePowers(wordLength, base2, mod2)

        for k in range(wordLength):
            if forcedChar[k] is not None:
                res[k] = forcedChar[k]
            else:
                vetoedChars = set()
                for i in criticalFIndices[k]:
                    match = True
                    prefixLen = k - i
                    if prefixLen > 0:
                        hRes1 = self.getHash(resHashes1, resPowers1, i, k, mod1)
                        hStr21 = self.getHash(str2Hashes1, str2Powers1, 0, prefixLen, mod1)
                        if hRes1 != hStr21:
                            match = False

                        if match:
                            hRes2 = self.getHash(resHashes2, resPowers2, i, k, mod2)
                            hStr22 = self.getHash(str2Hashes2, str2Powers2, 0, prefixLen, mod2)
                            if hRes2 != hStr22:
                                match = False

                    if match:
                        vetoedChars.add(str2[k - i])

                c = 'a'
                while c in vetoedChars:
                    c = chr(ord(c) + 1)
                res[k] = c

            val = ord(res[k])
            resHashes1[k + 1] = (resHashes1[k] * base1 + val) % mod1
            resHashes2[k + 1] = (resHashes2[k] * base2 + val) % mod2

        return "".join(res)

    def computePi(self, s: str):
        m = len(s)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and s[k] != s[q]:
                k = pi[k - 1]
            if s[k] == s[q]:
                k += 1
            pi[q] = k
        return pi

    def computeHashes(self, s, base, mod):
        n = len(s)
        hashes = [0] * (n + 1)
        for i in range(n):
            hashes[i + 1] = (hashes[i] * base + ord(s[i])) % mod
        return hashes

    def computePowers(self, n, base, mod):
        powers = [1] * (n + 1)
        for i in range(n):
            powers[i + 1] = (powers[i] * base) % mod
        return powers

    def getHash(self, hashes, powers, i, j, mod):
        val = (hashes[j] - hashes[i] * powers[j - i]) % mod
        return val if val >= 0 else val + mod