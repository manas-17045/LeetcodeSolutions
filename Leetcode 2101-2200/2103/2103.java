// Leetcode 2103: Rinngs and Rods
// https://leetcode.com/problems/rings-and-rods/
// Solved on 8th of March, 2026
class Solution {
    /**
     * Counts the number of rods that have all three colors (Red, Green, Blue) of rings.
     * 
     * @param rings A string describing the rings and their positions on the rods.
     * @return The total number of rods that contain all three colors.
     */
    public int countPoints(String rings) {
        int[] rods = new int[10];
        for (int i = 0; i < rings.length(); i += 2) {
            char color = rings.charAt(i);
            int rodIndex = rings.charAt(i + 1) - '0';
            if (color == 'R') {
                rods[rodIndex] |= 1;
            } else if (color == 'G') {
                rods[rodIndex] |= 2;
            } else if (color == 'B') {
                rods[rodIndex] |= 4;
            }
        }
        
        int count = 0;
        for (int i = 0; i < 10; i++) {
            if (rods[i] == 7) {
                count++;
            }
        }
        
        return count;
    }
}