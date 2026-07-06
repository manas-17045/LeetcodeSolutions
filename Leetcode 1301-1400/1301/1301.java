// Leetcode 1301: Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/
// Solved on 5th of July, 2026
class Solution {
    /**
     * Calculates the maximum score and the number of paths to achieve it in a grid.
     * 
     * @param board The grid represented as an array of strings.
     * @return An array containing the maximum score and the number of paths.
     */
    public int[] pathsWithMaxScore(String[] board) {
        int mod = 1000000007;
        int n = board.size();
        
        int[] prevScore = new int[n];
        int[] prevWays = new int[n];
        int[] currScore = new int[n];
        int[] currWays = new int[n];
        
        for (int i = 0; i < n; i++) {
            prevScore[i] = -1;
            currScore[i] = -1;
        }
        
        prevScore[n - 1] = 0;
        prevWays[n - 1] = 1;
        
        for (int r = n - 1; r >= 0; r--) {
            String rowStr = board.get(r);
            for (int c = n - 1; c >= 0; c--) {
                if (r == n - 1 && c == n - 1) {
                    currScore[c] = 0;
                    currWays[c] = 1;
                    continue;
                }
                
                char ch = rowStr.charAt(c);
                if (ch == 'X') {
                    currScore[c] = -1;
                    currWays[c] = 0;
                    continue;
                }
                
                int maxS = -1;
                int paths = 0;
                
                if (c + 1 < n && currScore[c + 1] != -1) {
                    if (currScore[c + 1] > maxS) {
                        maxS = currScore[c + 1];
                        paths = currWays[c + 1];
                    } else if (currScore[c + 1] == maxS) {
                        paths = (paths + currWays[c + 1]) % mod;
                    }
                }
                
                if (r + 1 < n && prevScore[c] != -1) {
                    if (prevScore[c] > maxS) {
                        maxS = prevScore[c];
                        paths = prevWays[c];
                    } else if (prevScore[c] == maxS) {
                        paths = (paths + prevWays[c]) % mod;
                    }
                }
                
                if (r + 1 < n && c + 1 < n && prevScore[c + 1] != -1) {
                    if (prevScore[c + 1] > maxS) {
                        maxS = prevScore[c + 1];
                        paths = prevWays[c + 1];
                    } else if (prevScore[c + 1] == maxS) {
                        paths = (paths + prevWays[c + 1]) % mod;
                    }
                }
                
                if (maxS != -1) {
                    int val = (ch == 'E') ? 0 : (ch - '0');
                    currScore[c] = maxS + val;
                    currWays[c] = paths;
                } else {
                    currScore[c] = -1;
                    currWays[c] = 0;
                }
            }
            
            for (int i = 0; i < n; i++) {
                prevScore[i] = currScore[i];
                prevWays[i] = currWays[i];
            }
        }
        
        if (currScore[0] == -1) {
            return new int[]{0, 0};
        }
        
        return new int[]{currScore[0], currWays[0]};
    }
}