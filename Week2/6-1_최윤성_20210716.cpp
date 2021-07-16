#include <iostream>
#include <queue>

using namespace std;

int main() {
    queue<int> q;
    int testcases;
    cin >> testcases;

    for(int i = 0; i < testcases; i++)
        q.push(i+1);
    
    for(bool back = false; q.size() != 1; back = !back) {
        int temp = q.front();
        q.pop();
        if(back)
            q.push(temp);
    }
    cout << q.front() << endl;
    return 0;
}