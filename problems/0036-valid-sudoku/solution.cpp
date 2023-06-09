#include<set>

class Solution {
public:
    bool isSubValid(int row, int col, vector<vector<char>>& board) {
        set<char> cache;

        for (int r = row; r < row + 3; r++) {
            for (int c = col; c < col + 3; c++) {
                char cx = board[r][c];
                if (cx == '.') { continue; }
                if (cache.find(cx) != cache.end()) {
                    return false; // exists more than once in row
                }
                cache.insert(cx);
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {

        // check all rows
        for (vector<char> row : board) {
            set<char> cache;
            for (char c : row) {
                if (c == '.') { continue; }
                if (cache.find(c) != cache.end()) {
                    return false; // exists more than once in row
                }
                cache.insert(c);
            }
        }

        // check all columns
        for (int col = 0; col < board.size(); col++) {
            set<char> cache;
            for (int row = 0; row < board.size(); row++) {
                char c = board[row][col];
                if (c == '.') { continue; }
                if (cache.find(c) != cache.end()) {
                    return false; // exists more than once in col
                }
                cache.insert(c);
            }
        }

        // check sub cubes
        for (int r = 0; r < board.size(); r += 3) {
            for (int c = 0; c < board.size(); c += 3) {
                if (!isSubValid(r, c, board)) {
                    return false;
                }
            }
        }

        return true;
    }
};








