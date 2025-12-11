// Leetcode 2350: Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
// Solved on 11th of December, 2025
import java.util.HashSet;
import java.util.Set;

class Solution {
    /**
     * Given an array of `rolls` representing a sequence of dice rolls and an integer `k` representing the number of faces on the die.
     * The goal is to find the length of the shortest impossible sequence of rolls.
     * An impossible sequence is a sequence of rolls that cannot be formed by concatenating subsequences of the given `rolls`.
     * @param rolls An array of integers representing the sequence of dice rolls.
     * @param k An integer representing the number of faces on the die.
     * @return The length of the shortest impossible sequence.
     */
    public int shortestSequence(int[] rolls, int k) {
        int length = 1;
        Set<Integer> collected = new HashSet<>();
        
        for (int roll : rolls) {
            collected.add(roll);
            if (collected.size() == k) {
                length++;
                collected.clear();
            }
        }
        
        return length;
    }
}