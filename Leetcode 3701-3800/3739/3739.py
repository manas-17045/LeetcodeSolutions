# Leetcode 3739: Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
# Solved on 7th of December, 2025
class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        """
        Counts the number of subarrays where the `target` element is a majority element.

        Args:
            nums: A list of integers.
            target: The integer element to check for majority.
        Returns:
            The total count of subarrays where `target` is the majority element.
        """
        n = len(nums)
        limit = 2 * n + 2
        bitArray = [0] * limit

        def update(index, val):
            while index < limit:
                bitArray[index] += val
                index += index & (-index)

        def query(index):
            total = 0
            while index > 0:
                total += bitArray[index]
                index -= index & (-index)
            return total

        resultCount = 0
        currentSum = 0
        offset = n + 1

        update(offset, 1)

        for num in nums:
            if num == target:
                currentSum += 1
            else:
                currentSum -= 1

            count = query(currentSum + offset - 1)
            resultCount += count

            update(currentSum + offset, 1)

        return resultCount