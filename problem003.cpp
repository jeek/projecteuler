#include <iostream>
using namespace std;

void problem003(long long upperlimit = 600851475143) {
    int i = 2;
    while (i < upperlimit) {
        if (upperlimit % i == 0) {
            upperlimit /= i;
        } else {
            i += 1;
        }
    } 
    cout << "003: " << i << "\n";
}

