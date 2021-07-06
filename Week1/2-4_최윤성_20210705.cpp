#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<char, int> dial;
    for(int i = 0, j = 0; i < 26; i++) {
        dial[65 + i] = j + 3;
        if(i < 'Q' - 'A' && i % 3 == 2)
            j++;
        else if(i > 'Q' - 'A' && i != 24 && i % 3 == 0)
            j++;
    }

    std::string dialLog;
    std::cin >> dialLog;
    int time = 0;
    for(char log : dialLog) {
        time += dial[log];
    }

    std::cout << time << std::endl;
    return 0;
}