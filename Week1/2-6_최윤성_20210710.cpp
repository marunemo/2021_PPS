#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    int testcases, group = 0;
    cin >> testcases;
    for(int i = 0; i < testcases; i++) {
        unordered_map<char, bool> log;
        string word;
        cin >> word;

        bool isGroup = true;
        for(int i = 0; i < word.length() && isGroup; i++) {
            if(i == 0 || word[i] != word[i - 1]) {
                if(!log[word[i]])
                    log[word[i]] = true;
                else
                    isGroup = false;
            }
        }

        if(isGroup) group++;
    }
    cout << group << endl;
}