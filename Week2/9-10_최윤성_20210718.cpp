#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int range = n / 5;
    int min = 5001;
    for(int i = 0; i <= range; i++) {
        int dummy = n - i * 5;
        if(dummy % 3 == 0) {
            if(min > i + dummy/3)
                min = i + dummy/3;
        }
    }
    cout << ((min==5001)?-1:min) << endl;
    return 0;
}