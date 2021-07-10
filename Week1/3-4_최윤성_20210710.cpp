#include <iostream>

using namespace std;

int main() {
    int testcases;
    bool door;
    cin >> testcases >> door;
    if(testcases > 5)
        cout << "Love is open door" << endl;
    else {
        for(int i = 0; i < testcases - 1; i++) {
            door = !door;
            cout << (int)door << "\n";
        }
    }
}