## Pacific Atlantic Water Flow

### Understanding problem

We know the edges of the input matrix will flow water on sides, and adjacent cell will flow water to the current one. So we need to start from the edges for sure.
It's impossible to to use 1 time iteration, so we will use DFS with queue structure and recursion. Our DFS function should check that we haven't marked the cell with the ocean.

### Thought About Solution

We can run two for loop and check the addition result for each combination & if it matches with the target then keep the indices of two numbers and return it. Time complexity would be O(N²) and Space complexity O(1).

```java
class Solution {
    int dir[][] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if(heights.length == 0 || heights[0].length == 0 || heights == null) 
            return result;
        
        int row = heights.length, col = heights[0].length;
        boolean[][] pacific = new boolean[row][col];
        boolean[][] atlantic = new boolean[row][col];
        
        // Dynamic Frequency Selection
        for(int i = 0; i < col; i++){
            dfs(heights, 0, i, Integer.MIN_VALUE, pacific);
            dfs(heights, row-1, i, Integer.MIN_VALUE, atlantic);
        }
        for(int i = 0; i < row; i++){
            dfs(heights, i, 0, Integer.MIN_VALUE, pacific);
            dfs(heights, i, col-1, Integer.MIN_VALUE, atlantic);
        }
        
        // Before making result
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++) {
                if(pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i,j));
                }
            }
        }
        
        return result;
    }
    
    public void dfs(int[][] heights, int i, int j, int prev, boolean[][] ocean){
        if(i < 0 || i >= ocean.length || j < 0 || j >= ocean[0].length) return;
        if(heights[i][j] < prev || ocean[i][j]) return;
        ocean[i][j] = true;
        for(int[] d : dir){
            dfs(heights, i+d[0], j+d[1], heights[i][j], ocean);
        }
        
    }
}

// TC: O(M*N); SC: O(M*N)
```


## Set Matrix Zeroes

### Understanding problem

Given Matrix

Step 1) 
First row with 0 = true;
First column with 0 = false;

![image](https://user-images.githubusercontent.com/82510378/212084029-db5ef7cc-b77f-4f98-91d1-3c5d22d33287.png)

Step 2)
Mark zero row and column based on first row and column.

![image](https://user-images.githubusercontent.com/82510378/212085001-9eaa6ebb-86da-41e5-bf3b-7560725a5cd4.png)

Step 3)
Set cells with marks in first row and column.

![image](https://user-images.githubusercontent.com/82510378/212085224-04c2a205-8579-4852-a640-194142bed7d1.png)

Step 4) 
Set 1st column and row based on marks of step 1)

![image](https://user-images.githubusercontent.com/82510378/212085411-ccbe8140-2c2e-48ff-bbd7-5c1f89484d87.png)

- Picture reference : https://www.programcreek.com/2012/12/leetcode-set-matrix-zeroes-java/

### Thought About Solution

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int col = matrix.length, row = matrix[0].length;
        boolean firstRow = false;
        boolean firstCol = false;

        for (int i = 0; i < col; i++)
            if (matrix[i][0] == 0)
                firstCol = true;

        for (int j = 0; j < row; j++)
            if (matrix[0][j] == 0)
                firstRow = true;

        for (int i = 1; i < col; i++) {
            for (int j = 1; j < row; j++) {
                if (matrix[i][j] == 0) {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for (int i = 1; i < col; i++) {
            for (int j = 1; j < row; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (firstCol) {
            for (int i = 0; i < col; i++)
                matrix[i][0] = 0;
        }

        if (firstRow) {
            for (int j = 0; j < row; j++)
                matrix[0][j] = 0;
        }
    }
}

// TC : O(M*N); SC : O(1)
```

#### Always welcome any feedbacks & Comments! 😊

