// Leetcode 3664: Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/
// Solved on 28th of December, 2025
class Solution {
    /**
     * Calculates the maximum score achievable in a two-letter card game.
     *
     * @param cards An array of strings, where each string represents a two-letter card.
     * @param x The special character for which the score is calculated.
     * @return The maximum possible score.
     */
    public int score(String[] cards, char x) {
        int xxCount = 0;
        int startSum = 0;
        int startMax = 0;
        int endSum = 0;
        int endMax = 0;
        
        int[] startFreq = new int[26];
        int[] endFreq = new int[26];
        
        for (String card : cards) {
            char c0 = card.charAt(0);
            char c1 = card.charAt(1);
            
            if (c0 == x && c1 == x) {
                xxCount++;
            } else if (c0 == x) {
                int index = c1 - 'a';
                startFreq[index]++;
                startSum++;
                if (startFreq[index] > startMax) {
                    startMax = startFreq[index];
                }
            } else if (c1 == x) {
                int index = c0 - 'a';
                endFreq[index]++;
                endSum++;
                if (endFreq[index] > endMax) {
                    endMax = endFreq[index];
                }
            }
        }
        
        int maxPoints = 0;
        
        for (int i = 0; i <= xxCount; i++) {
            int currentStartSum = startSum + i;
            int currentStartMax = Math.max(startMax, i);
            int startPoints = Math.min(currentStartSum / 2, currentStartSum - currentStartMax);
            
            int xxInEnd = xxCount - i;
            int currentEndSum = endSum + xxInEnd;
            int currentEndMax = Math.max(endMax, xxInEnd);
            int endPoints = Math.min(currentEndSum / 2, currentEndSum - currentEndMax);
            
            if (startPoints + endPoints > maxPoints) {
                maxPoints = startPoints + endPoints;
            }
        }
        
        return maxPoints;
    }
}