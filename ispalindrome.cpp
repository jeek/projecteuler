bool ispalindrome(int original) {
    int result = 0;
    int number = original;
    while (number) {
        result *= 10;
        result += (number % 10);
        number /= 10;
    }
    return (result == original);
}
