#include "gcd.h"

long long lcm(long long x, long long y) {
    return x * y / gcd(x, y);
}
