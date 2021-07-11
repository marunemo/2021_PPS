#include <iostream>

int main() {
    int max = 0;
    int maxIndex = 0;
    for(int i = 1; i <= 5; i++) {
        int score[4];
        std::cin >> score[0] >> score[1] >> score[2] >> score[3];
        int sum = score[0] + score[1] + score[2] + score[3];
        if(max < sum) {
            max = sum;
            maxIndex = i;
        }
    }
    std::cout << maxIndex << " " << max << std::endl;
    return 0;
}