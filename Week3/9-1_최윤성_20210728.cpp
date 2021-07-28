#include <iostream>
#include <vector>

using namespace std;

vector<int> v;

void postfix(int start, int end) {
    if(start > end)
        return;
    
    int root = v[start];
    int idx = start + 1;

    while(idx <= end && v[idx] < root) idx++;

    postfix(start + 1, idx - 1);
    postfix(idx, end);
    cout << root << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int node;
    while(cin >> node)
        v.push_back(node);
    postfix(0, v.size() - 1);
}