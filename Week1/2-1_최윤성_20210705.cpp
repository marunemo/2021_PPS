#include <iostream>
#include <vector>

using namespace std;

inline bool isVowel(char x) {
    return (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u');
}

int main() {
    vector<pair<string, bool> > password;
    string passGen = "";

    while(passGen != "end") {
        bool onVowel = false;
        bool continued = false;
        bool isContinue = false;
        bool isSame = false;
        cin >> passGen;
        if(passGen != "end") {
            for(int i = 0; i < passGen.length(); i++) {
                if(isVowel(passGen[i]))
                    onVowel = true;
                if(i > 0) {
                    if(passGen[i] == passGen[i - 1] && passGen[i] != 'e' && passGen[i] != 'o')
                        isSame = true;
                    if((isVowel(passGen[i]) && isVowel(passGen[i - 1])) || (!isVowel(passGen[i]) && !isVowel(passGen[i - 1]))) {
                        if(continued)
                            isContinue = true;
                        continued = true;
                    }
                    else
                        continued = false;
                }
            }
            password.push_back(make_pair(passGen, !onVowel | isContinue | isSame));
        }
    }

    for(vector<pair<string, bool> >::iterator iter = password.begin(); iter != password.end(); iter++)
        cout << "<" << iter->first << "> is " << (iter->second?"not ":"") << "acceptable." << endl;
}