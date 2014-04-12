#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char* argv[]) {
    int year = 1900;
    int count = 0;
    int month;
    int day = 1;
    int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    day += 365;
    day %= 7;
    for (year = 1901; year <= 2000; year++) {
        if (year % 4 == 0) {
            months[1] = 29;
        } else {
            months[1] = 28;
        }
        for (month = 0; month < 12; month++) {
            if (day == 0) {
                count++;
            }
            day += months[month];
            day %= 7;
        }
    }
    cout << "019: " << count << endl;
}