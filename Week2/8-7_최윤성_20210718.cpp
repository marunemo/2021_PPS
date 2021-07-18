#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, bool> n;
    vector<bool> m;
    int N,M;
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> M;
        n[M] = true;
    }
    cin >> M;
    for(int i = 0; i < M; i++) {
        cin >> N;
        m.push_back(n[N]);
    }
    for(bool b : m)
        cout << (int)b << "\n";
    return 0;
}