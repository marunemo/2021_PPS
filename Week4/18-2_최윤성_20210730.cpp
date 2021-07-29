#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, int> count;
    int n;
    cin >> n;
    count[1] = 1;
    count[2] = 1;
    count[3] = 2;
    count[4] = 2;
    count[5] = 1;
    count[6] = 2;
    count[7] = 1;
    for(int i = 8; i <= n; i++) {
        int minCount = i;
        if(minCount > count[1] + count[i - 1])
            minCount = count[1] + count[i - 1];
        if(minCount > count[2] + count[i - 2])
            minCount = count[2] + count[i - 2];
        if(minCount > count[5] + count[i - 5])
            minCount = count[5] + count[i - 5];
        if(minCount > count[7] + count[i - 7])
            minCount = count[7] + count[i - 7];
        count[i] = minCount;
    }
    cout << count[n] << endl;
    return 0;
}