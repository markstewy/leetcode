class Solution {
public:
    int firstUniqChar(string s) {
        // create a map with char as key and instances as value
        std::unordered_map<char, int> map;
        for (int i = 0; i < s.length(); i++) {
            if (map.find(s[i]) != map.end()) {
                map[s[i]]++;
            } else {
                std::pair<char, int> p;
                p.first = s[i];
                p.second = 1;
                map.insert(p);
            }
        }
        
        // loop over chars again and check if the key has a value of 1
        for (int i = 0; i < s.length(); i++) {
            if (map[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};