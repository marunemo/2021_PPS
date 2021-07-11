#include <iostream>

using namespace std;

int main() {
    string n1, n2;
    cin >> n1 >> n2;
    string result = "";
    int len1 = n1.length(), len2 = n2.length();
    int carry = 0;
    for(int i = 1; (len1 - i >= 0) || (len2 - i >= 0); i++) {
        int num1 = (len1 - i < 0)?0:n1[len1 - i] - '0';
        int num2 = (len2 - i < 0)?0:n2[len2 - i] - '0';
        int add = num1 + num2 + carry;
        carry = add / 10;
        result = (char)(add % 10 + '0') + result;
    }
    if(carry)
        result = '1' + result;
    cout << result << endl;
    return 0;
}