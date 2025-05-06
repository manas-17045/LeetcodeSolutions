# Leetcode 1920: Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        """
        Builds a new array based on a permutation rule where each element in the output
        array is determined by the value of the input array at the index specified by
        the value at the same index.

        This function takes an input list of integers and returns a new list of the
        same length. Each element in the new list is specified by the permutation
        rule: `ans[i] = nums[nums[i]]`. This is achieved by iterating over the length
        of the array and permuting using the given logic.

        :param nums: The input list of integers used to derive the new array. Each element
            in the list must specify valid indices within the range of the list.
        :type nums: list[int]

        :return: A new array built based on the permutation rule `ans[i] = nums[nums[i]]`.
        :rtype: list[int]
        """
        # Create a new array to store the result
        ans = [0] * len(nums)

        # Fill the array according to the rule: ans[i] = nums[nums[i]]
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans