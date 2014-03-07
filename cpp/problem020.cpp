#include <cstdlib>
#include <gmpxx.h>
#include <string>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 100;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    mpz_t total;
    mpz_init(total);
    mpz_t result;
    mpz_init(result);
    mpz_t temp;
    mpz_init(temp);
    mpz_add_ui(total, total, 1);
    int i;
    for (i = 1; i <= upperlimit; i++) {
        mpz_mul_ui(total, total, i);
    }
    while (int mpz_cmp_ui(total, 0)) {
        mpz_tdiv_qr_ui(total, temp, total, 10);
        mpz_add(result, result, temp);
    }
    cout << "020: " << result << endl;
}
