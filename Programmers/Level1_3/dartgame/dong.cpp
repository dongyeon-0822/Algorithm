#include <iostream>
#include <string>
#include <cctype>
#include <cmath>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int value[3] = { 0, };
    int count = -1;
    for (int i = 0; i < dartResult.size(); i++) {
        if (isdigit(dartResult[i])!=0) {
            count++;
            if (dartResult[i + 1] == '0') {
                value[count] = 10; i++;
            }
            else
                value[count] = dartResult[i] - 48;
        }
        else if (isalpha(dartResult[i]) != 0) {
            switch (dartResult[i]){
            case('S'):
                value[count] = pow(value[count], 1); break;
            case('D'):
                value[count] = pow(value[count], 2); break;                
            case('T'):
                value[count] = pow(value[count], 3); break;
            default:
                break;
            }
        }
        else {
            switch (dartResult[i]){
            case('*'):
                if (count == 0) value[count] *= 2;
                else {
                    value[count - 1] *= 2;
                    value[count] *= 2;
                }
                break;
            case('#'):
                value[count] *= -1; break;
            default:
                break;
            }
        }
    }
    answer = value[0] + value[1] + value[2];
    return answer;
}
int main() {
    string s="1S2D*3T";
    cout << solution(s);
}