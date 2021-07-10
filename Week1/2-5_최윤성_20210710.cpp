#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    string word;
    cin >> word;
    unordered_map<char, int> dict;

    for(char i : word)
        dict[toupper(i)]++;

    int maxNum = 0;
    char maxWord;
    for(auto i = dict.begin(); i != dict.end(); i++) {
        if(maxNum < i->second) {
            maxNum = i->second;
            maxWord = i->first;
        }
        else if(maxNum == i->second)
            maxWord = '?';
    }
    cout << maxWord << endl;
    return 0;
}