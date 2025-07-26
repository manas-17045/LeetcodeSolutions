# Leetcode 1307: Verbal Arithmetic Puzzle
# https://leetcode.com/problems/verbal-arithmetic-puzzle/
# Solved on 26th of July, 2025
class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        """
        Determines if a given cryptarithmetic puzzle is solvable.

        Args:
            words: A list of strings representing the addends.
            result: A string representing the sum.
        Returns:
            True if the puzzle is solvable, False otherwise.
        """
        # Quick reject: result must be at least as long as the longest addend
        maxw = max(map(len, words))
        if len(result) < maxw or len(result) > maxw + 1:
            return False

        # Reverse for easy least-significant-first indexing
        words_rev = [w[::-1] for w in words]
        result_rev = result[::-1]
        n = len(words_rev)
        max_col = len(result_rev)

        # Leading letters that cannot be zero
        non_zero = set()
        for w in words:
            if len(w) > 1:
                non_zero.add(w[0])
        if len(result) > 1:
            non_zero.add(result[0])

        # Current mapping and used digits
        assign = {}  # char -> digit
        used = [False] * 10  # digit -> taken?

        def dfs(col: int, row: int, carry: int, col_sum: int) -> bool:
            # Finished all columns
            if col == max_col:
                return carry == 0

            # Still summing the addends in this column
            if row < n:
                w = words_rev[row]
                # No letter at this position: treat as 0
                if col >= len(w):
                    return dfs(col, row + 1, carry, col_sum)
                ch = w[col]
                if ch in assign:
                    # Already assigned: add its value
                    return dfs(col, row + 1, carry, col_sum + assign[ch])
                # Try every possible digit
                for d in range(10):
                    if used[d]:
                        continue
                    # Leading-zero check
                    if d == 0 and ch in non_zero:
                        continue
                    # Assign & recurse
                    assign[ch] = d
                    used[d] = True
                    if dfs(col, row + 1, carry, col_sum + d):
                        return True
                    # Backtrack
                    del assign[ch]
                    used[d] = False
                return False

            # Now, handle the result column
            total = col_sum + carry
            target_digit = total % 10
            next_carry = total // 10

            if col >= len(result_rev):
                # Result too short to hold the sum digit
                return False

            ch = result_rev[col]
            if ch in assign:
                # Must match
                if assign[ch] != target_digit:
                    return False
                return dfs(col + 1, 0, next_carry, 0)

            # Try to assign the result letter
            if used[target_digit]:
                return False
            if target_digit == 0 and ch in non_zero:
                return False

            assign[ch] = target_digit
            used[target_digit] = True
            if dfs(col + 1, 0, next_carry, 0):
                return True
            del assign[ch]
            used[target_digit] = False
            return False

        return dfs(0, 0, 0, 0)