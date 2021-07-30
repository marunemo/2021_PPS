#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > time;
    int maxCount = 0;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;
        time.push(make_pair(end, start));
    }

    for(int next = 0; !time.empty(); time.pop()) {
        if(time.top().second >= next) {
            next = time.top().first;
            maxCount++;
        }
    }
    cout << maxCount << endl;
    return 0;
}