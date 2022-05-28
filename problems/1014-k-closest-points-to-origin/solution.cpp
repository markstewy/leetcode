class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::sort(points.begin(), points.end(), compare);
        points.erase(points.begin() + k, points.end());
        return points;
    }
    
    static bool compare(vector<int> x, vector<int> y) {
        bool z = (getDistance(x) < getDistance(y));
        return z;
    }
    
    static double getDistance(vector<int> x) {
        double a = abs(x[0]);
        double b = abs(x[1]);
        if (a == 0) return b;
        if (b == 0) return a;
        return sqrt(pow(a, 2) + pow(b, 2));
    }
};
