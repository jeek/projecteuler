#include "problem006.h"
#include "abs.h"
#include <iostream>
using namespace std;

void problem006(int upperlimit = 100) {
    long long squareofsums = 0;
    long long sumofsquares = 0;
    long long i = 1;
    while (i <= upperlimit) {
        squareofsums += i;
        sumofsquares += i * i;
        i++;
    }
    cout << "006: " << abs(squareofsums * squareofsums - sumofsquares) << endl;
}
