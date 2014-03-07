#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
    int i, j = 0, row = 0, rows = 1;
    vector<vector<int> > triangle;
    int upperlimit = 1000;
    
    if (argc < 2) {
        cout << "018: Put array on command line." << endl;
        exit(EXIT_FAILURE);
    }

    triangle.resize(1);
    for (i = 1 ; i < argc ; i++) {
        triangle[row].push_back(atoi(argv[i]));
        if (++j >= rows) {
            j = 0;
            row++;
            rows++;
            triangle.resize(rows);
        }
    } 
    if (j != 0) {
        cout << "018: Not a triangle." << endl;
        exit(EXIT_FAILURE);
    }
    for (i = rows - 3 ; i >= 0 ; i--) {
        for (j = 0 ; j <= i ; j++) {
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }
    cout << "018: " << triangle[0][0] << endl;
}