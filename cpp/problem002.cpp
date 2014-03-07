#include <iostream>
using namespace std;

int main() {
    int a = 0;
    int b = 1;
    int c = 1;
    int total = 0;
    while (c < 4000000) {
        a = b;
        b = c;
        c = a + b;
        if (c % 2 == 0) {
            total += c;
        }
    }
    cout << "002: " << total << "\n";
}

