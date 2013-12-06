#include "abs.h"

long long abs(long long x) {
    if (x < 0) {
        return 0 - x;
    }
    return x;
}
