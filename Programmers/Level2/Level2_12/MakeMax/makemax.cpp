#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    while (k > 0) {
        int max = number[0];
        int len = k;
        for (int i = 0; i < len + 1; i++) {
            if (number[i] > max)
                max = number[i];
        }
        for (int i = 0; i < len + 1; i++) {
            if (number[i] != max)
                k -= 1;
            else {
                answer += number[i];
                if (answer.size() == number.size() - len)
                    break;
            }
        }
        number = number.substr(len + 1);
    }
    answer += number;
    return answer;
}
int main() {
    cout << solution("1111", 2);
}