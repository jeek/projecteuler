#include <cstdlib>
#include <iostream>
#include "problem007.h"
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 10001;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    long long primes[upperlimit];
    int i = 0, j = 5, k;
    for (i = 0 ; i < upperlimit ; i++) {
        primes[i] = 0;
    }
    primes[0] = 2;
    primes[1] = 3;
    for (i = 2 ; i < upperlimit ; i++) {
        k = 0;
        while ((primes[k] != 0) and (j % primes[k] != 0)) {
            k++;
        }
        if (primes[k] == 0) {
            primes[k] = j;
        } else {
            i--;
        }
        j++;
    }
    cout << "007: " << primes[upperlimit - 1] << endl;
}
