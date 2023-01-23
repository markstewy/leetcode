// solution in 10 mins
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int>m {
            {'b', 0},
            {'a', 0},
            {'l', 0},
            {'o', 0},
            {'n', 0}
        };
        
        for (char c : text) {
            if (m.find(c) != m.end()) {
                m[c] = m[c] + 1;
            }
        }
        
        int singleMin = min(m['b'], min(m['a'], m['n']));
        int doubleMin = min(m['l'], m['o']);
        
        return min(singleMin, doubleMin / 2);
    }
};
