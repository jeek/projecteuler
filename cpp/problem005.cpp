#include <cstdlib>
#include <iostream>
#include "lcm.h"
using namespace std;

int main (int argc, char* argv[]) {
    int upperlimit = 20;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    long long i = 1;
    long long answer = 1;
    while (i <= upperlimit) {
        answer = lcm(answer, i);
        i++;
    }
    cout << "005: " << answer << "\n";
}
