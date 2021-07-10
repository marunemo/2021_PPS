#include <iostream>

using namespace std;

int main() {
    string s;
    cin >> s;
    while(!s.empty()) {
        cout << s.substr(0, 10) << "\n";
        s = ((s.length() < 10)?"":s.substr(10));
    }
    return 0;
}