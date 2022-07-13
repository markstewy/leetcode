class Solution {
public:
    int count = 0;
    int numIslands(vector<vector<char>>& grid) {
        int islandCount = 0;
        for (int i = 0; i <= grid.size() - 1; i++) {
            for(int j = 0; j <= grid[i].size() - 1; j++) {
                if (grid[i][j] == '1') {
                    markIsland(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
private:
    void markIsland(vector<vector<char>>& grid, int i, int j) {
        // base case
        if (grid[i][j] == '0') {
            return;
        } else {
            // must mark 0 first to avoid infinite loops
            grid[i][j] = '0';
            if (i != 0) { // check up
                markIsland(grid, i -1, j);
            }
            if (i != grid.size() - 1) { // check down
                markIsland(grid, i + 1, j);
            }
            if (j != grid[i].size() - 1) { // check right
                markIsland(grid, i, j + 1);
            }
            if (j != 0) { // check left
                markIsland(grid, i, j - 1);
            }
        }
    }
};