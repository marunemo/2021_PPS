#include <iostream>

int main() {
    char tune[8];
    bool isasc = false, isdes = false;

    for(int i = 0; i < 8; i++) {
        std::cin >> tune[i];
        if(i != 0) {
            if(tune[i] > tune[i-1])
                isasc = true;
            else if(tune[i] < tune[i-1])
                isdes = true;
        }
    }

    if(isasc && isdes)
        std::cout << "mixed" << std::endl;
    else if(isasc)
        std::cout << "ascending" << std::endl;
    else if(isdes)
        std::cout << "descending" << std::endl;

    return 0;
}