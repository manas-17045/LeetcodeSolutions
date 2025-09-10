# Leetcode 2151: Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/
# Solved on 10th of September, 2025
class Solution:
    def maximumGood(self, statements: list[list[int]]) -> int:
        """
        Determines the maximum number of "good" people possible given a set of statements.

        Args:
            statements: A list of lists of integers representing statements.
                        statements[i][j] = 0 means person i says person j is bad.
                        statements[i][j] = 1 means person i says person j is good.
                        statements[i][j] = 2 means person i made no statement about person j.

        Returns:
            The maximum number of good people that can exist consistently with the statements.
        """
        n = len(statements)
        if n == 0:
            return 0

        best = 0
        full = 1 << n

        for mask in range(full):
            # Quick prune: if current number of goods can't beat best, skip checking
            cnt = mask.bit_count()
            if cnt <= best:
                continue

            valid = True
            # Check statements of every person assumed to be good in this mask
            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    # Person i assumed bad: their statements can be arbitrary, ignore
                    continue
                # Person i is assumed good -> all their non-2 statements must match mask
                row = statements[i]
                for j in range(n):
                    s = row[j]
                    if s == 2:
                        continue
                    is_good_j = (mask >> j) & 1
                    if s == 1 and is_good_j == 0:
                        # i says j is good but mask says j is bad -> contradiction
                        valid = False
                        break
                    if s == 0 and is_good_j == 1:
                        # i says j is bad but mask says j is good -> contradiction
                        valid = False
                        break
                if not valid:
                    break

            if valid:
                best = cnt  # cnt > the best due to prune condition

        return best