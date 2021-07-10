#include <iostream>

int main() {
    int date;
    bool unhappy;
    float proba[4];
    std::cin >> date >> unhappy;
    std::cin >> proba[0] >> proba[1] >> proba[2] >> proba[3];

    float happy[2] = {(unhappy?proba[2]:proba[0]), (unhappy?proba[3]:proba[1])};
    for(int i = 0; i < date - 1; i++) {
        float gg = happy[0] * proba[0];
        float gb = happy[0] * proba[1];
        float bg = happy[1] * proba[2];
        float bb = happy[1] * proba[3];

        happy[0] = gg + bg;
        happy[1] = gb + bb;
    }
    std::cout << std::fixed;
    std::cout.precision(0);
    std::cout << happy[0] * 1000 << " " << happy[1] * 1000 << std::endl;
}