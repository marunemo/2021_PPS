#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> p;
    string result = "<";
    int n,k;
    cin >> n >> k;
    for(int i = 0; i < n; i++)
        p.push_back(i + 1);
    
    int len = p.size();
    for(int i = k - 1; !p.empty(); i += k - 1) {
        i %= p.size();
        vector<int>::iterator iter = p.begin() + i;
        result += to_string(*iter) + ", ";
        p.erase(iter);
    }
    cout << result.substr(0, result.length() - 2) << ">" << endl;
    return 0;
}