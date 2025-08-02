# Leetcode 828: Count Unique Characters of All Substrings of a Given String
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# Solved on 2nd of August, 2025
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        Calculates the total contribution of each character to the sum of unique letter counts
        for all substrings of a given string `s`.
        :param s: The input string.
        :return: The total sum of unique letter counts across all substrings.
        """
        n = len(s)
        # For each of the 26 uppercase letters, maintain a list of positions,
        # with sentinel -1 at the front and n at the end.
        pos = [[-1] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('A')].append(i)
        for lst in pos:
            lst.append(n)

        total = 0
        for lst in pos:
            # We skip the first sentinel and the last sentinel
            for j in range(1, len(lst) - 1):
                prev_idx = lst[j - 1]
                cur_idx = lst[j]
                next_idx = lst[j + 1]
                total += (cur_idx - prev_idx) * (next_idx - cur_idx)
        
        return total