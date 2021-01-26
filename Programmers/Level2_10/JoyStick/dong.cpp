#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int move = 0;
    int left, right;
    int left_move, right_move;
    int sum = 0;

    vector<int> updown(name.size());
    for (int i = 0; i < name.size(); i++) {
        if (name[i] <= 'N') 
            updown[i] = name[i] - 'A';
        else
            updown[i] = 'Z' - name[i] + 1;
        answer += updown[i];
        sum += updown[i];
    }

    while (1) {
        sum -= updown[move];
        updown[move] = 0;
        if (sum <= 0) break;

        left = right = 0;
        left_move = right_move = move;
        do {
            if (left_move == 0) left_move = name.size();
            left++;
        } while (updown[--left_move] == 0);
        do {
            if (right_move == name.size() - 1) right_move = -1;
            right++;
        } while (updown[++right_move] == 0);
        
        if (left < right) {
            answer += left;
            if (move - left < 0)
                move = name.size() - (move - left) - 2;
            else move -= left;
        }
        else {
            answer += right;
            if (move + right > name.size() - 1)
                move = (move + right) - name.size() + 1;
            else move += right;
        }
    }
    
    return answer;
}
int main() {
    cout << solution("AABAAAAAAAB");
}