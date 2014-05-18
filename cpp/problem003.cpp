#include <cstdlib>
#include <iostream>
using namespace std;

int main (int argc, char* argv[]) {
    long long upperlimit = 600851475143;
    if (argc == 2) {
        upperlimit = atoll(argv[1]);
    }
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

