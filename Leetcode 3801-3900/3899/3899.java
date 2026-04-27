// Leetcode 3899: Angles of a Triangle
// https://leetcode.com/problems/angles-of-a-triangle/
// Solved on 27th of April, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the internal angles of a triangle given its side lengths.
     * 
     * @param sides An array of three integers representing the lengths of the sides.
     * @return A sorted array of three doubles representing the internal angles in degrees, or an empty array if the sides do not form a valid triangle.
     */
    public double[] internalAngles(int[] sides) {
        Arrays.sort(sides);
        if (sides[0] + sides[1] <= sides[2]) {
            return new double[0];
        }
        
        double sideA = sides[0];
        double sideB = sides[1];
        double sideC = sides[2];
        double[] angles = new double[3];
        
        angles[0] = Math.toDegrees(Math.acos((sideB * sideB + sideC * sideC - sideA * sideA) / (2.0 * sideB * sideC)));
        angles[1] = Math.toDegrees(Math.acos((sideA * sideA + sideC * sideC - sideB * sideB) / (2.0 * sideA * sideC)));
        angles[2] = Math.toDegrees(Math.acos((sideA * sideA + sideB * sideB - sideC * sideC) / (2.0 * sideA * sideB)));
        
        Arrays.sort(angles);
        
        return angles;
    }
}