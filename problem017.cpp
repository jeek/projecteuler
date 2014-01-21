#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 1000;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    int i = 1, total = 0;
    while (i <= upperlimit) {
        switch (i % 10) {
            case 1: total += 3; break;
            case 2: total += 3; break;
            case 3: total += 5; break;
            case 4: total += 4; break;
            case 5: total += 4; break;
            case 6: total += 3; break;
            case 7: total += 5; break;
            case 8: total += 5; break;
            case 9: total += 4; break;
            default: break;
        }
        switch ((i - i % 10) % 100) {
            case 10: switch (i % 100) {
                 case 10: total += 3; break;
                 case 11: total += 3; break;
                 case 12: total += 3; break;
                 case 13: total += 3; break;
                 case 14: total += 3; break;
                 case 15: total += 3; break;
                 case 16: total += 4; break;
                 case 17: total += 4; break;
                 case 18: total += 4; break;
                 case 19: total += 4; break;
                 default: break;
            } break;
            case 20: total += 6; break;
            case 30: total += 6; break;
            case 40: total += 5; break;
            case 50: total += 5; break;
            case 60: total += 5; break;
            case 70: total += 7; break;
            case 80: total += 7; break;
            case 90: total += 5; break;
            default: break;
        }
        if ((i > 100) and (i % 100 != 0)) {
            total += 3;
        }
        switch (i - (i % 100)) {
            case 100: total += 10; break;
            case 200: total += 10; break;
            case 300: total += 12; break;
            case 400: total += 11; break;
            case 500: total += 11; break;
            case 600: total += 10; break;
            case 700: total += 12; break;
            case 800: total += 12; break;
            case 900: total += 11; break;
            default: break;
        }
        if (i == 1000) {
            total += 11;
        }
        i++;
    }
    cout << "017: " << total << endl;
}