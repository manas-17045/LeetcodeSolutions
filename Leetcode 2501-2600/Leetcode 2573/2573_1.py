# Leetcode 2573: Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/
# Solved on 18th of May, 2025

class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        """
        Finds a string with the given Longest Common Prefix (LCP) matrix.

        Args:
            lcp: A list of lists representing the LCP matrix. lcp[i][j] is the length of the longest common prefix of the suffixes starting at indices i and j.

        Returns:
            A string that corresponds to the given LCP matrix, or an empty string if no such string exists.

        Algorithm:
            1. Validate the input LCP matrix for basic consistency.
            2. Greedily construct the string, assigning characters based on LCP values.
            3. Fully validate the constructed string against the given LCP matrix.
        """
        n = len(lcp)

        # Initial LCP Matrix Validation
        for r in range(n):
            if lcp[r][r] != n - r:
                return ""
            for c in range(r + 1, n):
                if lcp[r][c] != lcp[c][r]:
                    return ""

                # LCP value bound check: lcp[r][c] <= length of shorter suffix
                # Suffixes are word[r:] (len n-r) and word[c:] (len n-c).
                # Since c > r, (n - c) is shorter or equal. So, lcp[r][c] <= (n - c).
                if lcp[r][c] > n - c:
                    return ""

        # Greedy String construction
        ans = [''] * n
        char_code = 0

        for i in range(n):
            # If char for ans[i] is not yet determined
            if ans[i] == '':
                # Need more than 26 distinct characters
                if char_code >= 26:
                    return ""

                current_char = chr(ord('a') + char_code)
                ans[i] = current_char

                # Propagate this char to other positions j where lcp[i][j] > 0
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        if ans[j] == '':
                            ans[j] = current_char
                        elif ans[j] != current_char:
                            # Contradiction: ans[j] was set by a previous group
                            # to a different char, but lcp[i][j] > 0 requires
                            # ans[j] == ans[i] (current_char). This implies an
                            # inconsistency in the LCP matrix.
                            return ""

                char_code += 1  # Next available character for a new group

        # Full Validation of Constructed string
        for r in range(n):
            # Check upper triangle (r <= c)
            for c in range(r, n):
                expected_lcp_at_rc = lcp[r][c]
                actual_lcp_at_rc = 0

                if ans[r] == ans[c]:
                    if r == n - 1 or c == n - 1:    # One or both suffixes is a single char
                        actual_lcp_at_rc = 1
                    else:
                        # Recursive LCP definition: lcp(S1, S2) = 1 + lcp(S1[1:], [S2[1:])
                        # If S1[0] == S2[0]. Here, S1[1:] means suffix from (r + 1), S2[!] means suffix from (c + 1).
                        actual_lcp_at_rc = 1 + lcp[r + 1][c + 1]
                else:   # ans[r] != ans[c]
                    actual_lcp_at_rc = 0

                if actual_lcp_at_rc != expected_lcp_at_rc:
                    return ""

        return "".join(ans)
