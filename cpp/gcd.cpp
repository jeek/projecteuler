long long gcd(long long x, long long y) {
    long long temp;
    while (y > 0) {
        temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}

