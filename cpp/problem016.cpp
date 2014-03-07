#include <cstdlib>
#include <gmpxx.h>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 1000;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    mpz_t result;
    mpz_init(result);
    mpz_t temp;
    mpz_init(temp);
    mpz_t answer;
    mpz_init_set_ui(answer, 1);
    int i = 0;
    for (i = 0; i < upperlimit; i++) {
        mpz_mul_ui(answer, answer, 2);
    }
    while (int mpz_cmp_ui(answer, 0)) {
        mpz_tdiv_qr_ui(answer, temp, answer, 10);
        mpz_add(result, result, temp);
    }
    cout << "016: " << result << endl;
}