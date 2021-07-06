#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    unordered_map<char, int> count;
    bool surrender = true;
    string name;
    int testcase;

    cin >> testcase;
    for(int i = 0; i < testcase; i++) {
        cin >> name;
        count[name[0]]++;
    }

    name = "";
    for(unordered_map<char, int>::iterator iter = count.begin(); iter != count.end(); iter++)
        if(iter->second >= 5) {
            name += iter->first;
            surrender = false;
        }
    sort(name.begin(), name.end());
    cout << (surrender?"PREDAJA":name) << endl;
}