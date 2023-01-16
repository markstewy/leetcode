#include<unordered_map>

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char, int> m {
            {'b', 0},
            {'a', 0},
            {'l', 0},
            {'o', 0},
            {'n', 0}
        };
        
        for (char c : text) {
            (m[c])++;
        }
        
        int singles = min(m['b'], min(m['a'], m['n']));
        int doubles = min(m['l'], m['o']);
        
        return min(singles, (doubles / 2));
        
    }
};
