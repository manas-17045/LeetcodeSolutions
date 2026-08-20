# Leetcode 3069: Distribute Elements Into Two Arrays I
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
# Solved on 20th of August, 2026
class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        """
        Distributes elements into two subarrays based on comparing their last appended
        elements and returns their concatenation.

        Parameters:
            nums (List[int]): An array of integers with a length of at least 2.

        Returns:
            List[int]: The concatenated array of the first subarray followed by the
                       second subarray.
        """
        fA = [nums[0]]
        sA = [nums[1]]

        for num in nums:
            if fA[-1] > sA[-1]:
                fA.append(num)
            else:
                sA.append(num)

        return fA + sA