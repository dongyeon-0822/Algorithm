#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int distance(int num, int hand) {
    int num_i, num_j;
    int hand_i, hand_j;
    int arr[4][3]={{1,2,3},{4,5,6},{7,8,9},{'*',0,'#'} };
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] == num) {
                num_i = i; num_j = j;
            }
            if (arr[i][j] == hand) {
                hand_i = i; hand_j = j;
            }
        }
    }
    return abs(num_i - hand_i) + abs(num_j - hand_j);
}
string solution(vector<int> numbers, string hand) {
    string answer = "";
    int left_lc = '*';
    int right_lc = '#';
    int left_dis, right_dis;

    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
            answer += "L";
            left_lc = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
            answer += "R";
            right_lc = numbers[i];
        }
        else {
            left_dis = distance(numbers[i], left_lc);
            right_dis = distance(numbers[i], right_lc);
            
            if (left_dis < right_dis) {
                answer += "L";
                left_lc = numbers[i];
            }
            else if (left_dis > right_dis) {
                answer += "R";
                right_lc = numbers[i];
            }
            else {
                if (hand == "right") {
                    answer += "R";
                    right_lc = numbers[i];
                }
                else {
                    answer += "L";
                    left_lc = numbers[i];
                }
            }
        }
    }
    return answer;
}
int main() {
    vector<int> numbers{ 1,3,4,5,8,2,1,4,5,9,5 };
    string hand = "right";

    cout << solution(numbers, hand);
}