#include <bits/stdc++.h>
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](vector<int>a, vector<int>b){ return a[0] < b[0];});
        std::priority_queue<int, vector<int>, std::greater<int>> minHeap;
                  
        for (int i = 0; i < intervals.size(); i++) {
            if (minHeap.size() > 0 && intervals[i][0] >= minHeap.top()) {
                minHeap.pop();
            } 
            minHeap.push(intervals[i][1]);
            
        }
        return minHeap.size();
    }
};