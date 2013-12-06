#include <iostream>
using namespace std;

void problem001(int upperlimit = 1000) {
    int i = 0;
    int total = 0;
    for (i = 0 ; i < upperlimit ; i++) {
        if ((i % 3 == 0) | (i % 5 == 0)) {
            total += i;
        }
    }
    cout << "001: " << total << "\n";
}
