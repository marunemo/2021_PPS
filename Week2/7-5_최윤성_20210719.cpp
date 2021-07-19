#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string s;
    cin >> s;
    sort(s.begin(), s.end());
    for(auto c = s.rbegin(); c != s.rend(); c++)
        cout << *c;
    endl(cout);
    return 0;
}