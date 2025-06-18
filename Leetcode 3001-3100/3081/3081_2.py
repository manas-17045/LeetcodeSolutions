# Leetcode 3981: Replace Question Marks in String to Minimize Its Value
# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/
# Solved on 18th of June, 2025
import heapq


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        """
        Minimizes the string value by replacing '?' with lowercase letters.

        The string value is defined as the sum of squares of the frequencies
        of each character ('a' through 'z'). The goal is to replace each '?'
        with a lowercase letter such that this sum is minimized.

        Args:
            s: The input string containing lowercase letters and '?'.

        Returns:
            The modified string with '?' replaced to minimize the string value.
            If multiple solutions exist, the lexicographically smallest one is returned.
        """
        # Count fixed letters and question-marks
        freq = [0] * 26
        Q = 0
        for ch in s:
            if ch == '?':
                Q += 1
            else:
                freq[ord(ch) - 97] += 1

        # Distribute the Q question0marks to minimize sum of squares
        heap = [(freq[i], i) for i in range(26)]
        heapq.heapify(heap)
        # How many extra copies assigned to each letter
        add = [0] * 26
        for _ in range(Q):
            f, c = heapq.heappop(heap)
            add[c] += 1
            # New freq for c is (f + 1).
            heapq.heappush(heap, (f + 1, c))

        # Reconstruct result: fill '?' left-to-right with smallest letter still having quota
        res = []
        # Pointer to next letter to use
        cur = 0
        for ch in s:
            if ch != '?':
                res.append(ch)
            else:
                # Find the next x >= cur with ass[c] > 0
                while cur < 26 and add[cur] == 0:
                    cur += 1
                # Must exist, since sum(add) = Q
                res.append(chr(cur + 97))
                add[cur] -= 1

        return "".join(res)