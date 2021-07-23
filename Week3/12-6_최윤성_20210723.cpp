#include <iostream>

using namespace std;

int main() {
    string a = "1";
    string b = "1";
    int f;
    cin >> f;
    for(int i = 1; i < f; i++) {
        int carry = 0;
        string t = "";
        int lenA = a.length();
        int lenB = b.length();
        for(int l = 0; l < lenA || l < lenB; l++) {
            int ia = (l >= lenA)?0:(a[lenA - l - 1] - 48);
            int ib = (l >= lenB)?0:(b[lenB - l - 1] - 48);
            t.insert(0, to_string((ia + ib + carry) % 10));
            carry = (ia + ib + carry)/10;
        }
        if(carry)
            t = "1" + t;
        a = b;
        b = t;
    }
    cout << a << endl;
    return 0;
}