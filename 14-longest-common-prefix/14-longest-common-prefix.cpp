class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int commonPrefixLength = 0;
        if (strs.size() == 1) {
            return strs[0];
        }
        for (int letter = 0; letter < strs[0].length(); letter++) {
            for (int word = 1; word < strs.size(); word++) {
                if (letter > (int)strs[word].length() - 1) {
                    return strs[0].substr(0, commonPrefixLength);
                }
                if (strs[word][letter] != strs[word - 1][letter]) {
                    return strs[0].substr(0, commonPrefixLength);
                }
            }
            commonPrefixLength++;
        }
        return strs[0].substr(0, commonPrefixLength);
    }
};