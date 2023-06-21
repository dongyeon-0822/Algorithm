#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    long long temp;
    switch (n & 0x0f) {
    case 0:
    case 1:
    case 4:
    case 9:
        temp = (long long)(sqrt((double)n) + 0.5);
        if (temp * temp == n)
            return (temp + 1) * (temp + 1);
        else return -1;
    default:
        return -1;
    }

    return answer;
}