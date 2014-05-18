#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 1000;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    int i = 0;
    int total = 0;
    for (i = 0 ; i < upperlimit ; i++) {
        if ((i % 3 == 0) | (i % 5 == 0)) {
            total += i;
        }
    }
    cout << "001: " << total << "\n";
}
