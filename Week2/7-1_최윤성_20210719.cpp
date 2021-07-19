#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    cin >> n;
    unordered_map<int, vector<string> > m;
    set<int> order;

    for(int i = 0; i < n; i++) {
        int age;
        string name;
        cin >> age >> name;
        order.insert(age);
        m[age].push_back(name);
    }

    for(int i : order)
        for(string s : m[i])
            cout << i << " " << s << "\n";
    return 0;
}