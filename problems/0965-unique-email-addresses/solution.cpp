#include <set>
// solution in 15 mins
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> uniqueEmails;
        for (string e : emails) {
            string name;
            for (char c : e) {
                if (c == '@' || c == '+') break;
                if (c == '.') continue;
                name += c;
            }
            string domain = e.substr(e.find('@'));
            name += domain;
            uniqueEmails.insert((name));
        }
        return uniqueEmails.size();
    }
};
