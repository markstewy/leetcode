#include <set>

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        set<string> uniqueEmails;
        for (string e : emails) {
            string domain = e.substr(e.find('@'));
            string cleanE;
            for (char c : e) {
                if (c == '+' || c == '@') break;
                if (c != '.') cleanE.push_back(c);
            }
            cleanE += domain;
            uniqueEmails.insert(cleanE);
        }
        return uniqueEmails.size();
    }
};
