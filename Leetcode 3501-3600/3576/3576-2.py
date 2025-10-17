# Leetcode 3576: Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/
# Solved on 17th of October, 2025
class Solution:
    def canMakeEqual(self, nums: list[int], k: int) -> bool:
        """
        Determines if all elements in the array can be made equal to either 1 or -1
        by performing at most k operations. An operation consists of flipping the signs
        of two adjacent elements.
        :param nums: A list of integers, where each element is either 1 or -1.
        :param k: The maximum number of operations allowed.
        :return: True if all elements can be made equal to 1 or -1 within k operations, False otherwise.
        """
        n = len(nums)
        # Try both targets: 1 and -1
        for target in (1, -1):
            # Make a copy to simulate flips
            arr = nums[:]
            ops = 0

            for i in range(n - 1):
                if arr[i] != target:
                    # Flip arr[i] and arr[i + 1]
                    arr[i] = -arr[i]
                    arr[i + 1] = -arr[i + 1]
                    ops += 1

                    # Early stop if ops already exceed k
                    if ops > k:
                        break

            # After processing, check last element and ops limit
            if ops <= k and arr[-1] == target:
                return True

        return False