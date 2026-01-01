# Leetcode 3366: Minimum Array Sum
# https://leetcode.com/problems/minimum-array-sum/
# Solved on 1st of January, 2026
class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        """
        Calculates the minimum possible sum of elements in the array `nums` after applying at most `op1` operations of type 1
        and at most `op2` operations of type 2.

        Args:
            nums (list[int]): The input array of integers.
            k (int): A threshold value used in operation 2.
            op1 (int): The maximum number of times operation 1 can be applied.
            op2 (int): The maximum number of times operation 2 can be applied.

        Returns:
            int: The minimum possible sum of the array elements.
        """
        dp = [[float('inf')] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0

        for num in nums:
            for i in range(op1, -1, -1):
                for j in range(op2, -1, -1):
                    currentSum = dp[i][j] + num

                    if i > 0:
                        op1Val = (num + 1) // 2
                        currentSum = min(currentSum, dp[i - 1][j] + op1Val)

                    if j > 0 and num >= k:
                        op2Val = num - k
                        currentSum = min(currentSum, dp[i][j - 1] + op2Val)

                    if i > 0 and j > 0:
                        op1First = (num + 1) // 2
                        if op1First >= k:
                            currentSum = min(currentSum, dp[i - 1][j - 1] + op1First - k)

                        if num >= k:
                            op2First = num - k
                            op2FirstVal = (op2First + 1) // 2
                            currentSum = min(currentSum, dp[i - 1][j - 1] + op2FirstVal)

                    dp[i][j] = currentSum

        return int(min(min(row) for row in dp))