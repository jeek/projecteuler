#include <iostream>
#include "ispalindrome.h"
using namespace std;

void problem004(int size = 3) {
    int i, j;
    int start = 1, end = 1;
    for (i = 1; i < size ; i++) {
        start *= 10;
    }
    for (i = 0; i < size ; i++) {
        end *= 10;
    }
    int answer = 0;
    i = start;
    while (i < end) {
        j = start;
        while (j < end) {
            if (ispalindrome(i * j)) {
                if (i * j > answer) {
                    answer = i * j;
                }
            }
            j += 1;
        }
        i += 1;
    }
    cout << "004: " << answer << "\n";
}

