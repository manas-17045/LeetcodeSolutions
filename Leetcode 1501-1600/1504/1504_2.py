# Leetcode 1504: Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/
# Solved on 21st of August, 2025
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        """
        Calculates the total number of submatrices of all 1s in a given binary matrix.
        :param mat: A list of lists of integers representing the binary matrix.
        :return: An integer, the total number of submatrices of all 1s.
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0

        # For each row, update heights and compute how many submatrices end at this row
        for i in range(m):
            # Update histogram heights
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Use monotonic non-decreasing stack of (height, count)
            stack = []
            # Sum of (min_height * width) for all subarrays ending at current column
            sum_for_row = 0
            for h in heights:
                count = 1
                # Pop taller heights and merge their counts
                while stack and stack[-1][0] > h:
                    prev_h, prev_count = stack.pop()
                    sum_for_row -= prev_h * prev_count
                    count += prev_count

                stack.append((h, count))
                sum_for_row += h * count
                # All submatrices that end at this row and this column
                ans += sum_for_row

        return ans