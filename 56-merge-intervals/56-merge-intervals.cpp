class Solution {
public:
    static bool compareIntervals(vector<int> i1, vector<int> i2) {
        return i1[0] < i2[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end(), compareIntervals);
        
        vector<vector<int>> merged{};
        vector<int> interval = intervals[0];
        
        // if overlapp of any kind
        for (int i = 1; i <= intervals.size() - 1; i++) {
            
            vector<int> intervalNext = intervals[i];
            // expand if overlapping
            if ((intervalNext[0] <= interval[1] && intervalNext[0] >= interval[0])
                ||
                (intervalNext[1] <= interval[1] && intervalNext[1] >= interval[0])
                ||
                (intervalNext[0] <= interval[0] && intervalNext[1] >= interval[1])) {
                interval[0] = std::min(interval[0], intervals[i][0]);
                interval[1] = std::max(interval[1], intervals[i][1]);
                continue;
            }
            // if not overlapping add the interval and reset for next
            merged.push_back(interval);
            interval = intervalNext;
            continue;
        }
        merged.push_back(interval);
        return merged;
    }
};