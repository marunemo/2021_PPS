#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    priority_queue<int, vector<int>, greater<int> > q;
    int n,k;
    cin >> n >> k;

    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        q.push(a);
    }
    for(int i = 1; i < k; i++)
        q.pop();
    cout << q.top();
    return 0;
}