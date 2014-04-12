#include <cstdlib>
#include <iostream>
#include "ispalindrome.h"
using namespace std;

int main(int argc, char* argv[]) {
    int size = 3;
    if (argc == 2) {
        size = atoi(argv[1]);
    }
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

