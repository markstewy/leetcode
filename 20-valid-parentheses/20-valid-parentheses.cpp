class Solution {
public:
    bool isValid(string s) {
        vector<char> myQueue;
        unordered_map<char, char> openers {
            { '}', '{' },
            { ')', '(' },
            { ']', '[' }
        };
        for (int i = 0; i <= s.length() - 1; i++) {
            char c = s[i];
            if (c == '{' || c == '}' || c == '[' || c == ']' || c == '(' || c == ')') { // change to regex
                myQueue.push_back(c);
                if (openers.find(c) != openers.end()) {
                    int previous = (int)myQueue.size() - 2;
                    if (myQueue.size() > 1 && myQueue[previous] == openers[c]) {
                        myQueue.pop_back();
                        myQueue.pop_back();
                    } else {
                        return false;
                    }
                }
            }
        }
        
        if (myQueue.size() > 0) {
            return false;
        } else {
            return true;
        }
    }
};