#include <iostream>
#include <vector>

using namespace std;

int main() {
    int testcase;
    cin >> testcase;
    vector<float> ratio;
    for(int i = 0; i < testcase; i++) {
        int count, stud = 0;
        cin >> count;
        float sum = 0;
        vector<int> scores;
        for(int j = 0; j < count; j++) {
            int score;
            cin >> score;
            scores.push_back(score);
            sum += score;
        }
        sum /= count;
        for(int score : scores)
            if(score > sum) stud++;
        ratio.push_back((float)stud / count);
    }

    for(float stud : ratio) {
        cout << fixed;
        cout.precision(3);
        cout << stud * 100 << "%" << endl;
    }
}