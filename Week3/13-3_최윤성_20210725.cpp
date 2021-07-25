#include <iostream>
#include <queue>

using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<int> > q;
    int n,l;
    cin >> n >> l;
    for(int i = 0; i < n; i++) {
        int h;
        cin >> h;
        q.push(h);
    }
    while(!q.empty()) {
        if(l < q.top())
            break;
        q.pop();
        l++;
    }
    cout << l << endl;
    return 0;
}