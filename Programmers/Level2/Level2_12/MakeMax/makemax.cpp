#include <iostream>
#include <string>
#include <vector>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    int length = number.size() - k;
    while (k > 0) {
        int max = number[0];
        int len = k;
        int index = 0;
        for (int i = 0; i < len + 1; i++) {
            if (number[i] > max)
                max = number[i];
        }
        for (int i = 0; i < len + 1; i++) {
            if (number[i] == max) {
                index = i;
                answer += number[i];
                break;
            }
            else k -= 1;
        }
        number = number.substr(index + 1);
        if (answer.size() == length)
            return answer;
    }
    answer += number;
    return answer;
}
int main() {
    cout << solution("1111", 2);
}