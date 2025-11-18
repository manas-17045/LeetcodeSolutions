// Leetcode 717: 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/
// Solved on 18th of November, 2025
class Solution {
    /**
     * Checks if the last character in a sequence of bits can be a one-bit character.
     * @param bits An array of integers representing the bits.
     * @return True if the last character can be a one-bit character, false otherwise.
     */
    public boolean isOneBitCharacter(int[] bits) {
        int index = 0;
        while (index < bits.length - 1) {
            if (bits[index] == 1) {
                index += 2;
            } else {
                index++;
            }
        }
        return index == bits.length - 1;
    }
}