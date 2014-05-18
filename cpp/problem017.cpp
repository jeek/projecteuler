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
            case 3:
            case 7:
            case 8: total++;
            case 4:
            case 5:
            case 9: total++;
            case 1:
            case 2:
            case 6: total += 3;
            default: break;
        }
        switch ((i - i % 10) % 100) {
            case 10: switch (i % 100) {
                 case 16:
                 case 17:
                 case 18:
                 case 19: total++;
                 case 10:
                 case 11:
                 case 12:
                 case 13:
                 case 14:
                 case 15: total += 3;
                 default: break;
            } break;
            case 70:
            case 80: total++;
            case 20:
            case 30: total++;
            case 40:
            case 50:
            case 60:
            case 90: total += 5;
            default: break;
        }
        if ((i > 100) and (i % 100 != 0)) {
            total += 3;
        }
        switch (i - (i % 100)) {
            case 300:
            case 700:
            case 800: total++;
            case 400:
            case 500:
            case 900: total++;
            case 100:
            case 200:
            case 600: total += 10;
            default: break;
        }
        if (i == 1000) {
            total += 11;
        }
        i++;
    }
    cout << "017: " << total << endl;
}