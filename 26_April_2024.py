"""
1289. Minimum Falling Path Sum II

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
Input: grid = [[7]]
Output: 7

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""

class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n = grid.length;
        
        // Initialize dp array to store minimum falling path sums
        int[][] dp = new int[n][n];
        
        // Copy the first row from the grid to dp array
        System.arraycopy(grid[0], 0, dp[0], 0, n);
        
        // Iterate through each row starting from the second row
        for (int i = 1; i < n; i++) {
            // Iterate through each column
            for (int j = 0; j < n; j++) {
                // Find the minimum previous path sum in the adjacent columns
                int minPrev = Integer.MAX_VALUE;
                for (int k = 0; k < n; k++) {
                    if (k != j) {
                        minPrev = Math.min(minPrev, dp[i - 1][k]);
                    }
                }
                // Update the current cell in dp array with the minimum path sum
                dp[i][j] = grid[i][j] + minPrev;
            }
        }
        
        // Find the minimum path sum in the last row of dp array
        int minPathSum = Integer.MAX_VALUE;
        for (int num : dp[n - 1]) {
            minPathSum = Math.min(minPathSum, num);
        }
        
        return minPathSum;
    }
}
