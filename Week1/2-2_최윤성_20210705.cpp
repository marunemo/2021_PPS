#include <iostream>
#include <vector>

using namespace std;

int main() {
    int testcase;
    cin >> testcase;

    vector<int> scores;
    for(int i = 0; i < testcase; i++) {
        int score = 0, grade = 1;
        string ox;
        cin >> ox;
        for(char pro : ox) {
            if(pro == 'X')
                grade = 1;
            else
                score += grade++;
        }
        scores.push_back(score);
    }

    for(int i = 0; i < testcase; i++)
        cout << scores[i] << endl;
}