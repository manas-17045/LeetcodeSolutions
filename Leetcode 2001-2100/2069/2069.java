// Leetcode 2069: Walking Simulation II
// https://leetcode.com/problems/walking-simulation-ii/
// Solved on 7th of April, 2026
class Robot {
    int width;
    int height;
    int perimeter;
    int currentPosition;
    boolean hasMoved;

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        this.perimeter = 2 * (width - 1) + 2 * (height - 1);
        this.currentPosition = 0;
        this.hasMoved = false;
    }

    public void step(int num) {
        this.currentPosition = (this.currentPosition + num) % this.perimeter;
        if (num > 0) {
            this.hasMoved = true;
        }
    }

    public int[] getPos() {
        int w1 = this.width - 1;
        int h1 = this.height - 1;

        if (this.currentPosition <= w1) {
            return new int[]{this.currentPosition, 0};
        } else if (this.currentPosition <= w1 + h1) {
            return new int[]{w1, this.currentPosition - w1};
        } else if (this.currentPosition <= 2 * w1 + h1) {
            return new int[]{w1 - (this.currentPosition - (w1 + h1)), h1};
        } else {
            return new int[]{0, h1 - (this.currentPosition - (2 * w1 + h1))};
        }
    }

    public String getDir() {
        if (this.currentPosition == 0) {
            return this.hasMoved ? "South" : "East";
        }
        
        int w1 = this.width - 1;
        int h1 = this.height - 1;

        if (this.currentPosition <= w1) {
            return "East";
        } else if (this.currentPosition <= w1 + h1) {
            return "North";
        } else if (this.currentPosition <= 2 * w1 + h1) {
            return "West";
        } else {
            return "South";
        }
    }
}