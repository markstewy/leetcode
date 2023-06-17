class Codec {
public:
    char unit_separator = '\x1F';

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded;
        for (string s : strs) {
            encoded.append(s);
            encoded.push_back(unit_separator);
        }
        return encoded;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> solution;
        string str;
        for (char c : s) {
            if (c == unit_separator) {
                solution.push_back(str);
                str = "";
            } else {
                str.push_back(c);
            }
        }
        return solution;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
