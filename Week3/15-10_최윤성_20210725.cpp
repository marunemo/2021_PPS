#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    unordered_map<string, bool> dj;
    vector<string> dbj;
    int n,m;
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        string name;
        cin >> name;
        dj[name] = true;
    }
    for(int i = 0; i < m; i++) {
        string name;
        cin >> name;
        if(dj[name])
            dbj.push_back(name);
    }
    cout << dbj.size() <<endl;
    sort(dbj.begin(), dbj.end());
    for(string s : dbj)
        cout << s << "\n";
    return 0;
}