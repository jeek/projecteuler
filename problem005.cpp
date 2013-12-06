#include <iostream>
#include "lcm.h"
using namespace std;

void problem005(int upperlimit = 20) {
    long long i = 1;
    long long answer = 1;
    while (i <= upperlimit) {
        answer = lcm(answer, i);
        i++;
    }
    cout << "005: " << answer << "\n";
}
