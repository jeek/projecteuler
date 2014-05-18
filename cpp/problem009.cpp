#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    for (a = 1 ; a <= 1000 ; a++) {
        for (b = a + 1 ; a + b < 1000 ; b++) {
            for (c = 1000 - b - a; (a + b + c) == 1000 and c > b ; c++) {
                if (a * a + b * b == c * c) {
                    cout << "009: " << (a * b * c) << endl;
                }
            }
        }
    }
}
