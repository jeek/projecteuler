#include "problem010.h"
#include <iostream>
using namespace std;

void problem010(int upperlimit = 2000000) {
    int primes[upperlimit];
    long long i, j;
    for (i = 0; i < upperlimit; i++) {
        primes[i] = 1;
    }
    primes[0] = 0;
    primes[1] = 0;
    for (i = 2; i < upperlimit; i++) {
        if (primes[i] == 1) {
            for (j = i * i; j < upperlimit ; j += i) {
                primes[j] = 0;
            }
        }
    }
    j = 0;
    for (i = 0; i < upperlimit; i++) {
        if (primes[i] == 1) {
            j += i;
        }
    }
    cout << "010: " << j << endl;
}
