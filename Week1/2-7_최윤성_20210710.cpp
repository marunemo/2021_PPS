#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<string> computer;
    int testcases;
    cin >> testcases;
    for(int i = 0; i < testcases; i++) {
        string word;
        cin >> word;
        computer.push_back(word);
    }
    for(int i = 0; i < testcases; i++) {
        cout << "String #" << i + 1 << "\n";
        for(char alpha : computer[i])
            cout << (char)((alpha == 'Z')?'A':alpha + 1);
        if(i != testcases - 1)
            cout << "\n";
        endl(cout);
    }
}