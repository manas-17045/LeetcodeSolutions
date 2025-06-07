# Leetcode 3474: Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/
# Solved on 6th of June, 2025

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        """
        Generates a string of length n + m - 1 based on two input strings str1 and str2.

        The generated string must satisfy the following conditions:
        1. For each 'T' at index i in str1, the substring of the generated string
           starting at index i and of length m must be equal to str2.
        2. For each 'F' at index i in str1, the substring of the generated string
           starting at index i and of length m must NOT be equal to str2.

        Args:
            str1: A string consisting of 'T' and 'F' characters.
            str2: A string consisting of lowercase English letters.

        Returns:
            The generated string if a valid string exists, otherwise an empty string.

        """
        n = len(str1)
        m = len(str2)
        L = n + m - 1

        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and str2[k] != str2[q]:
                k = pi[k - 1]
            if str2[k] == str2[q]:
                k += 1
            pi[q] = k

        borders = set()
        b = pi[m - 1]
        while b > 0:
            borders.add(b)
            b = pi[b - 1]
        validPeriods = set((m - b_len) for b_len in borders)
        validPeriods.add(0)

        B = 0
        for i, ch in enumerate(str1):
            if ch == 'T':
                B |= (1 << i)

        for d in range(1, m):
            if d not in validPeriods:
                if (B & (B >> d)) != 0:
                    return ""

        BF = 0
        mask_n = (1 << n) - 1
        for d in range(1, m):
            if d not in validPeriods:
                BF |= (B >> d)
                BF |= ((B << d) & mask_n)

        forcedChar = [None] * L
        covered = [0] * L

        last_T = -10**18
        for pos in range(L):
            if pos < n and str1[pos] == 'T':
                last_T = pos
            dist = pos - last_T
            if 0 <= dist < m:
                forcedChar[pos] = str2[dist]
                covered[pos] = 1

        covered_ps = [0] * L
        run = 0
        for i in range(L):
            run += covered[i]
            covered_ps[i] = run

        last_unforced = [-1] * L
        last_free = -1
        for i in range(L):
            if covered[i] == 0:
                last_free = i
            last_unforced[i] = last_free

        critical_lists = [[] for _ in range(L)]
        for i, ch in enumerate(str1):
            if ch == 'F':
                if ((BF >> i) & 1) == 1:
                    continue

                start = i
                end = i + m - 1

                total_cov = covered_ps[end] - (covered_ps[start - 1] if start > 0 else 0)
                if total_cov == m:
                    return ""

                k_tree = last_unforced[end]
                if k_tree >= start:
                    ok_suffix = True
                    for j in range(k_tree + 1, end + 1):
                        if forcedChar[j] != str2[j - i]:
                            ok_suffix = False
                            break
                    if ok_suffix:
                        critical_lists[k_tree].append(i)
                else:
                    all_match = True
                    for j in range(start, end + 1):
                        if forcedChar[j] != str2[j - i]:
                            all_match = False
                            break
                    if all_match:
                        return ""

        base1, mod1 = 29, 10**9 + 7
        base2, mod2 = 31, 10**9 + 9

        # Compute prefix hashes for str2
        hash2a = [0] * (m + 1)
        hash2b = [0] * (m + 1)
        pow2a = [1] * (m + 1)
        pow2b = [1] * (m + 1)
        for i in range(m):
            val = ord(str2[i])
            hash2a[i + 1] = (hash2a[i] * base1 + val) % mod1
            hash2b[i + 1] = (hash2b[i] * base2 + val) % mod2
            pow2a[i + 1] = (pow2a[i] * base1) % mod1
            pow2b[i + 1] = (pow2b[i] * base2) % mod2

        # Helper function to get hash
        def getHash2(l, r):
            ha1 = (hash2a[r] - hash2a[l] * pow2a[r - l]) % mod1
            ha2 = (hash2b[r] - hash2b[l] * pow2b[r - l]) % mod2
            return (ha1 + mod1) % mod1, (ha2 + mod2) % mod2

        res = [''] * L
        rh1 = [0] * (L + 1)
        rh2 = [0] * (L + 1)
        powRa = [1] * (L + 1)
        powRb = [1] * (L + 1)
        for i in range(L):
            powRa[i + 1] = (powRa[i] * base1) % mod1
            powRb[i + 1] = (powRb[i] * base2) % mod2

        def getHashRes(i, j):
            ha1 = (rh1[j] - rh1[i] * powRa[j - i]) % mod1
            ha2 = (rh2[j] - rh2[i] * powRb[j - i]) % mod2
            return (ha1 + mod1) % mod1, (ha2 + mod2) % mod2

        # Build the final string from left to right
        for k in range(L):
            if forcedChar[k] is not None:
                c = forcedChar[k]
            else:
                veto = set()
                for i in critical_lists[k]:
                    lengthPrefix = k - i
                    if lengthPrefix == 0:
                        prefixMatch = True
                    else:
                        (h1_res, h2_res) = getHashRes(i, k)
                        (h1_2, h2_2) = getHash2(0, lengthPrefix)
                        prefixMatch = ((h1_res == h1_2) and (h2_res == h2_2))

                    if prefixMatch:
                        veto.add(str2[k - i])

                c = 'a'
                while c in veto:
                    c = chr(ord(c) + 1)
                    if c > 'z':
                        return ""

            res[k] = c
            val = ord(c)
            rh1[k + 1] = (rh1[k] * base1 + val) % mod1
            rh2[k + 1] = (rh2[k] * base2 + val) % mod2

        return "".join(res)