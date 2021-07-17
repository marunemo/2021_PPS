#include <iostream>
#include <set>

using namespace std;

int main() {
    set<int> numset;
    int testcases;
    cin >> testcases;
    for(int i = 0; i < testcases; i++) {
        int n;
        cin >> n;
        numset.insert(n);
    }
    for(int set : numset)
        cout << set << " ";
    endl(cout);
    return 0;
}