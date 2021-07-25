#include <iostream>
#include <set>

using namespace std;

struct comp {
    int operator() (string a, string b) const {
        if(a.length() == b.length())
            return a < b;
        return a.length() < b.length();
    }
};

int main() {
    set<string, comp> w;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        string word;
        cin >> word;
        w.insert(word);
    }
    for(string s : w)
        cout << s << "\n";
    return 0;
}