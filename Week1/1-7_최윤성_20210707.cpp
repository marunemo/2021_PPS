#include <iostream>

int main() {
    int row, column;
    std::cin >> column >> row;

    int type[5] = {0};
    std::string blind, blinded;
    std::cin >> blind;
    for(int i = 0; i < column; i++) {
        int open = row;
        for(int shut = 0; shut < 4; shut++) {
            blinded = blind;
            std::cin >> blind;
            for(int window = 0; window < row; window++) {
                if(blinded[5 * window + 1] == '*' && blind[5 * window + 1] == '.') {
                    open--;
                    type[shut]++;
                }
            }
        }
        for(int window = 0; window < row; window++) {
            if(blind[5 * window + 1] == '*') {
                open--;
                type[4]++;
            }
        }
        std::cin >> blind;
        type[0] += open;
    }

    for(int i : type) {
        std::cout << i << " ";
    }
    std::endl(std::cout);
    return 0;
}