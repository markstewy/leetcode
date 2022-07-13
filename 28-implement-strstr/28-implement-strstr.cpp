class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") {
            return 0;
        }
        
        int l = haystack.length();
        
        for (int i = 0; i < l; i++) {
            char hf = haystack[i];
            char nf = needle[0];
            bool enoughSpace = (l - i - 1) >= needle.length() - 1;
            if (hf == nf && enoughSpace) {
                char he = haystack[i + needle.length() - 1];
                char ne = needle[needle.length() - 1];
                if (he == ne) {
                    string potentialNeedle = haystack.substr(i, needle.length());
                    if (potentialNeedle.compare(needle) == 0) {
                        return i;
                    } 
                }
            }
        }
        return -1;
    }
};