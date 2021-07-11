#include <iostream>
#include <vector>

using namespace std;

int count(string str, string del) {
    int c = 0, index = 0;
    while(index != -1) {
        index = str.find(del, index + 1);
        if(index != -1) c++;
    }
    return c;
}

int main() {
    string lyric = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan";
    vector<string> slice;
    while(!lyric.empty()) {
        int index = lyric.find(" ");
        if(index == -1) {
            slice.push_back(lyric);
            lyric = "";
        }
        else {
            slice.push_back(lyric.substr(0, index));
            lyric = lyric.substr(index + 1, lyric.length() - index);
        }
    }
    int num;
    cin >> num;
    num--;
    string word = slice[num % slice.size()];
    if(word == "tururu" || word == "turu") {
        int wc = count(word, "ru");
        if(num / slice.size() + wc > 4)
            cout << "tu+ru*" << num / slice.size() + wc;
        else {
            cout << word;
            for(int i = 0; i < num / slice.size(); i++)
                cout << "ru";
        }
    }
    else
        cout << word;
    endl(cout);
}