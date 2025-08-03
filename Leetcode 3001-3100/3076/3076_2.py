# Leetcode 3076: Shortest Uncommon Substring in an Array
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/
# Solved on 3rd of August, 2025
class Solution:
    def shortestSubstrings(self, arr: list[str]) -> list[str]:
        """
        Finds the shortest unique substring for each string in a given list.
        A substring is considered unique if it appears only once across all strings in the input list.
        If multiple shortest unique substrings exist for a string, the lexicographically smallest one is chosen.

        Args:
            arr: A list of strings.
        Returns:
            A list of strings, where each element is the shortest unique substring for the corresponding input string.
        """
        n = len(arr)
        freq = {}
        subs_list = [set() for _ in range(n)]

        # Build each subs_list[i] and update global freq
        for i, s in enumerate(arr):
            L = len(s)
            seen = subs_list[i]
            # Generate all substrings of s
            for start in range(L):
                for end in range((start + 1), (L + 1)):
                    seen.add(s[start:end])

            # Update frequencies
            for sub in seen:
                freq[sub] = freq.get(sub, 0) + 1

        # For each string, pick the shortest substring with freq == 1
        ans = []
        for i in range(n):
            # Sort substrings by (length, lex) so that we see shortest & then lexicographically smallest first
            candidates = sorted(subs_list[i], key=lambda st: (len(st), st))

            # Find first candidate that occurs in no other string
            found = ""
            for sub in candidates:
                if freq[sub] == 1:
                    found = sub
                    break

            ans.append(found)

        return ans