#include <iostream>
#include <stdlib.h>
#include "problem001.h"
#include "problem002.h"
#include "problem003.h"
#include "problem004.h"
#include "problem005.h"
#include "problem006.h"
#include "problem007.h"
#include "problem008.h"
#include "problem009.h"
#include "problem010.h"
using namespace std;

int main(int argc, char* argv[]) {
    int problemnumber = 0;
    if (argc >= 2) {
        problemnumber = atoi(argv[1]);
    }   
    if (problemnumber == 0 or problemnumber == 1) {
        if (argc == 3) {
            problem001(atoi(argv[2]));
        } else {
            problem001(1000);
        }
    }
    if (problemnumber == 0 or problemnumber == 2) {
        problem002();
    }
    if (problemnumber == 0 or problemnumber == 3) {
        if (argc == 3) {
            problem003(atoi(argv[2]));
        } else {
            problem003(600851475143);
        }
    }
    if (problemnumber == 0 or problemnumber == 4) {
        if (argc == 3) {
            problem004(atoi(argv[2]));
        } else {
            problem004(3);
        }
    }
    if (problemnumber == 0 or problemnumber == 5) {
        if (argc == 3) {
            problem005(atoi(argv[2]));
        } else {
            problem005(20);
        }
    }
    if (problemnumber == 0 or problemnumber == 6) {
        if (argc == 3) {
            problem006(atoi(argv[2]));
        } else {
            problem006(100);
        }
    }
    if (problemnumber == 0 or problemnumber == 7) {
        if (argc == 3) {
            problem007(atoi(argv[2]));
        } else {
            problem007(10001);
        }
    }
    if (problemnumber == 0 or problemnumber == 8) {
        problem008();
    }
    if (problemnumber == 0 or problemnumber == 9) {
        problem009();
    }
    if (problemnumber == 0 or problemnumber == 10) {
        if (argc == 3) {
            problem010(atoi(argv[2]));
        } else {
            problem010(2000000);
        }
    }
}
