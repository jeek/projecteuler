#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int upperlimit = 500;
    if (argc == 2) {
        upperlimit = atoi(argv[1]);
    }
    int r = 0, x = 0, y = 0, z = 0;
    while(r < upperlimit) { 
        y += x++;
        r = 0;
        for (z = 1 ; z * z < y ; z ++) {
            if (y % z == 0) {
                r += 2; 
            }
        }
        if (z * z == y) {
            r++;
        }
    }
    cout << "012: " << y << endl;
}