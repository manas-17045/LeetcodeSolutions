// Leetcode 4059: Lexicographically Largest Power Array
// https://leetcode.com/problems/lexicographically-largest-power-array/
// Solved on 27th of October, 2026
class Solution {
    /**
     * Calculates the lexicographically largest possible power array from a given array of numbers.
     * The function determines the maximum length of a valid prefix for each bit position
     * from 14 down to 0, rearranging elements within bounded groups to maximize the count.
     *
     * @param nums an integer array representing the initial numbers to be rearranged
     * @return an integer array of size 15 representing the lexicographically largest power array
     */
    public int[] largestPower(int[] nums) {
        int[] powerArray = new int[15];
        int[] groupStarts = new int[32];
        int[] groupEnds = new int[32];
        int[] nextStarts = new int[32];
        int[] nextEnds = new int[32];
        int groupCount = 1;
        
        groupStarts[0] = 0;
        groupEnds[0] = nums.length;
        
        for (int currentBit = 14; currentBit >= 0; currentBit--) {
            int prefixCount = 0;
            boolean splitOccurred = false;
            int nextCount = 0;
            
            for (int i = 0; i < groupCount; i++) {
                int start = groupStarts[i];
                int end = groupEnds[i];
                
                if (splitOccurred) {
                    nextStarts[nextCount] = start;
                    nextEnds[nextCount] = end;
                    nextCount++;
                    continue;
                }
                
                int left = start;
                int right = end - 1;
                
                while (left <= right) {
                    if ((nums[left] & (1 << currentBit)) != 0) {
                        left++;
                    } else if ((nums[right] & (1 << currentBit)) == 0) {
                        right--;
                    } else {
                        int temp = nums[left];
                        nums[left] = nums[right];
                        nums[right] = temp;
                        left++;
                        right--;
                    }
                }
                
                if (left == end) {
                    prefixCount += (end - start);
                    nextStarts[nextCount] = start;
                    nextEnds[nextCount] = end;
                    nextCount++;
                } else {
                    prefixCount += (left - start);
                    
                    if (left > start) {
                        nextStarts[nextCount] = start;
                        nextEnds[nextCount] = left;
                        nextCount++;
                    }
                    
                    if (left < end) {
                        nextStarts[nextCount] = left;
                        nextEnds[nextCount] = end;
                        nextCount++;
                    }
                    
                    splitOccurred = true;
                }
            }
            
            powerArray[14 - currentBit] = prefixCount;
            
            int[] tempStarts = groupStarts;
            groupStarts = nextStarts;
            nextStarts = tempStarts;
            
            int[] tempEnds = groupEnds;
            groupEnds = nextEnds;
            nextEnds = tempEnds;
            
            groupCount = nextCount;
        }
        
        return powerArray;
    }
}