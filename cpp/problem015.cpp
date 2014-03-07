#include <cstdlib>
#include <gmpxx.h>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 20;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    mpz_t answer;
    mpz_init_set_ui(answer, 1);
    int i;
    for (i = 1 ; i <= upperlimit * 2 ; i++) {
        mpz_mul_ui(answer, answer, i);
    }
    for (i = 1 ; i <= upperlimit ; i++) {
        mpz_tdiv_q_ui(answer, answer, i);
        mpz_tdiv_q_ui(answer, answer, i);
    }
    cout << "015: " << answer << endl;
}
