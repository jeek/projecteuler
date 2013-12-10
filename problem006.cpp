#include <cstdlib>
#include "problem006.h"
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 100;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
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
