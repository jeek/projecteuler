#include <iostream>
using namespace std;

int main() {
    long long answer = 0, max = 0;
    int distance[1000000];
    long long i = 0, j = 0;
    for (i = 0; i < 1000000; i++) {
        distance[i] = -1;
    }
    distance[1] = 0;
    for (i = 0; i < 1000000; i++) {
        j = i;
        while (j != 1) {
            if (j % 2 == 0) {
                j /= 2;
            } else {
                j = j * 3 + 1;
            }
            if (j >= 1000000) {
                distance[i]++;
            } else {
                if (distance[j] == -1) {
                    distance[i]++;
                } else {
                    distance[i] += distance[j];
                    j = 1;
                }
            }
        }
        if (distance[i] > max) {
            max = distance[i];
            answer = i;
        }
    }
    cout << "014: " << answer << endl;
}