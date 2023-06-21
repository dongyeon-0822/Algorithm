#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    int count = 0;
    while (count <= 500 && num != 1) {
        count++;
        if (num % 2 == 0)
            num /= 2;
        else if (num % 2 == 1) {
            num *= 3;
            num += 1;
        }

        if (num == 1) {
            break;
        }
        else
            continue;
    }
    if (count > 500) {
        answer = -1;
    }
    else answer = count;

    return answer;
}